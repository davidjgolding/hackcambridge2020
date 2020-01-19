#!/usr/bin/env python

import boto3
bucket_name = 'hackathon18012020'
s3_file_path = 'text.txt'

save_as = 'data.txt'
s3 = boto3.client('s3')
s3.download_file(bucket_name, s3_file_path, save_as)

with open(save_as) as f:
  print(f.read())
