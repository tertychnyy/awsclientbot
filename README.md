=========================
AWS Client Bot for Python
=========================

Use this library to push messages from AWS EC2 instance to Telegram via [@aws_client_bot](https://t.me/aws_client_bot).

Step 1. Obtain AWS Client Bot token
* Go to [@aws_client_bot](https://t.me/aws_client_bot),
* Set AWS credentials (this allows start/stop instances from [@aws_client_bot](https://t.me/aws_client_bot)),
* Send "/token",
* Use token on step 2

Step 2. Set logger
Typical usage looks like this::

    #!/usr/bin/env python

    from awsclientbot import AWSClientBot

    acb = AWSClientBot()
    acb.push(token, "Started")
    my_long_computation_function()
    acb.push(token, "Done")
