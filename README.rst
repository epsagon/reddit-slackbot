Serverless Reddit Slack Bot
=====================

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
   :target: https://saythanks.io/to/nshap

.. image:: https://github.com/epsagon/reddit-slackbot/blob/master/screenshot.png
   :align: center

Description
----------
- Serverless Reddit Slack Bot
- Can be used as a template for other Slack bots

Setup
-----
- Configure config.json with the Reddit client parameters, Slack webhook URL, and the subreddits to track
- Update serverless.yml with your AWS account ID
- Deploy the Lambda function

.. code-block:: bash

    git clone git@github.com:epsagon/reddit-slackbot.git
    cd reddit-slackbot/
    pip install -r requirements.txt -t packages/
    sls deploy


