import json
import urllib.parse
import boto3

----
import os
import sys
import uuid
import json
import requests
import time
from urllib.parse import unquote_plus

print('Loading function')

s3_client = boto3.client('s3')
sns_client = boto3.client('sns')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3_client.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']

        # checking object size
        if record['s3']['object']['size'] > (10*1024*1024):
            return

        key = unquote_plus(record['s3']['object']['key'])
        tmpkey = key.replace('/', '')
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
        
        print("DEBUG#######\n{}\n{}\n{}\nDEBUG##### END".format(bucket, tmpkey, download_path))
        
        s3_client.download_file(bucket, key, download_path)
        #s3_client.upload_file(upload_path, '{}-resized'.format(bucket), key)
        if is_file_infected(download_path):
            publish_to_sns(record['s3']['object'])


def publish_to_sns(data):
    topic_arn = sns_client.list_topics['ListTopicsResponse']['ListTopicsResult']['Topics'][0]['TopicArn']
    response = sns_client.publish(
                                 TopicArn=topic_arn,    
                                 Message="Infected file detected!\n{0}".format(data),
                                 )










