from flask import Flask
import boto3

import os

app=Flask(__name__,static_url_path="")


client = boto3.client('s3', 
         region_name='ap-south-1',
         aws_access_key_id=os.getenv('ACCESS_KEY'),
         aws_secret_access_key=os.getenv('SECRET_KEY')
      )