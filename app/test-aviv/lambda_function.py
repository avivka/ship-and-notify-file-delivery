import urllib.parse
import boto3
import os
import json
from urllib.parse import unquote_plus

print('Loading function')

s3_client = boto3.client('s3')
ses_client = boto3.client('ses')


def send_email(sender, to, subject, body):
        """
        Send email.
        Note: The emails of sender and receiver should be verified.
        PARAMS
        @sender: sender's email, string
        @to: list of receipient emails eg ['a@b.com', 'c@d.com']
        @subject: subject of the email
        @body: body of the email
        """
        try:
            response = ses_client.send_email(
                Destination={
                    'ToAddresses': to,
                },
                Message={
                    'Body': {
                        'Text': {
                            'Charset': 'UTF-8',
                            'Data': body,
                        },
                    },
                    'Subject': {
                        'Charset': 'UTF-8',
                        'Data': subject,
                    },
                },
                Source=sender,
            )

        except Exception as e:
            raise ("Error while sending mail %s" % e)


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    filename, file_ext = os.path.splitext(key) 
    body = f"Key {key} was added to bucket {bucket} with file extetion {file_ext}"
    send_email("avivka8@gmail.com", "avivka8@gmail.com", f"New File input into bycket {bucket}")

