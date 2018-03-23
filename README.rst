Serverless Reddit Slack Bot
=====================

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
   :target: https://saythanks.io/to/nshap

.. image:: https://github.com/epsagon/reddit-slackbot/blob/master/screenshot.png
   :align: center

Description
----------
- Serverless Reddit Slack Bot for tracking new submissions
- Deployed as a Python AWS Lambda using the Serverless Framework
- Can be used as a template for other Slack bots

Setup
-----
- Configure config.json with the Reddit client parameters, Slack webhook URL, and the subreddits to track
- Update serverless.yml with your AWS account ID
- Deploy the Lambda function

.. code-block:: bash

    git clone https://github.com/epsagon/reddit-slackbot
    cd reddit-slackbot/
    pip install -r requirements.txt -t packages/
    serverless deploy


