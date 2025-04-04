#import boto3

#boto_client = boto3.client('s3')


# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import requests
import boto3
import os
import json
from botocore.exceptions import ClientError

ACCESS_KEY = os.getenv('aws_access_key_id')
SECRET_KEY = os.getenv('aws_secret_access_key')
git_token = os.getenv('git_token')

def get_secret():

    secret_name = "dev/app/mysecret"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session(
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY
    )
    client = session.client(service_name='secretsmanager', region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']
    print(f'this is the secret value {secret}')
    # Your code goes here.

def get_github_variables():
    git_repo = "aws-terraform-ec2-deployment"
    git_owner = "dilanasanga"
    git_variable_name = "TESTVARIABLE"
#    git_token = ""
    git_url = f"https://api.github.com/repos/{git_owner}/{git_repo}/actions/variables/{git_variable_name}"

    response = requests.get(url=git_url,headers={"Authorization": git_token})
    dict_out = response.json()
    json_out = json.dumps(dict_out)
    print(json_out)
    
    git_respose = response.json()
    print(f"the output is {git_respose}")
    print (f"{dict_out['name']} : {dict_out['value']}")
    

    with open("/tmp/out.data", "w") as output_data:
        output_data.write(json_out)

get_secret()
get_github_variables()


#  https://api.github.com/repos/OWNER/REPO/actions/variables/NAME

#TESTVARIABLE TestVariableValue

