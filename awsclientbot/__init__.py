import requests

__author__ = 'it@chatfirst.co (Ivan Tertychnyy)'


class AWSClientBot():
    def __init__(self):
        self.base_url = "https://b45599xxme.execute-api.us-west-2.amazonaws.com/prod/awsclientbot_push"
        r = requests.get("http://169.254.169.254/latest/meta-data/instance-id")
        self.instance_id = r.text

    def push(self, token, message):

        data = {
            "token": token,
            "message": "{i} says\n\n{m}".format(i=self.instance_id, m=message)
        }
        r = requests.post(self.base_url, json=data)
