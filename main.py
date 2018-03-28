"""
Reddit submissions Slack bot
"""

import os
import time
import json
import boto3
import packages
import requests
import praw

# Constants
TWO_HOURS = 7200
TEN_HOURS = 36000

config = json.load(open('config.json'))

reddit = praw.Reddit(
    client_id=config['reddit']['client-id'],
    client_secret=config['reddit']['client-secret'],
    user_agent='bot'
)

lambda_client = boto3.client('lambda')


def get_submissions():
    """
    Listing submissions from subreddits
    :return: new submissions
    """

    submissions = []
    last_submission_time = float(os.environ['LAST_SUBMISSION'])
    print 'Last submission time: {}'.format(last_submission_time)

    for subreddit_data in config['subreddits'].split('|'):
        subreddit_name, query = subreddit_data.split('^')
        subreddit = reddit.subreddit(subreddit_name)

        # Get only updated submissions
        subs = subreddit.search(query, sort='new', limit=100)
        submissions.extend(
            [s for s in subs if s.created_utc > last_submission_time]
        )

    return submissions


def update_slack(submissions):
    """
    Updating Slack with new submissions.
    :param submissions: new submissions
    """

    for submission in submissions:
        submission_date = time.strftime(
            '%H:%M %d/%m', time.gmtime(int(submission.created_utc) + TWO_DAYS)
        )

        message = '*<{}|{}>*\n*Subreddit*: {}\n*Date*: {}\n{}'.format(
            submission.url,
            submission.title,
            submission.subreddit.display_name,
            submission_date,
            '-' * 20,
        )
        
        requests.post(
            config['slack-hook-url'],
            headers={'Content-type': 'application/json'},
            data=json.dumps({'text': message})
        )


def handler(_, context):
    """
    Lambda handler
    :param _: event (unused)
    :param context: context
    :return: ''
    """

    submissions = get_submissions()
    if submissions:
        update_slack(submissions)

        last_submission = str(max([submission.created_utc for submission in submissions]))
        print 'Updated last submission: {}'.format(last_submission)

        lambda_client.update_function_configuration(
            FunctionName=context.function_name,
            Environment={
                'Variables': {
                    'LAST_SUBMISSION': last_submission,
                }
            }
        )

    return ''


# For testing and running locally
if __name__ == '__main__':
    os.environ['LAST_SUBMISSION'] = str(time.time() - TEN_DAYS)

    class Context(object):
        """ Mock context """
        def __init__(self):
            self.function_name = 'test'

    handler(None, Context())
