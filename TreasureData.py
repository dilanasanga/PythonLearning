
"""
Purpose

Collect secret scanner alerts we have in our Github org
"""
import os
import logging
import requests
import boto3 
import json 

client = boto3.client('secretsmanager')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ALERTS_FILE = "/tmp/alerts.json"


def get_secrets():

    try:
        response = client.get_secret_value(
            SecretId='DatabaseProdSecrets'
        )

        github_alerts_secrets = json.loads(response['SecretString'])

        return github_alerts_secrets
    except Exception as err:
        logger.error(err)


def collect_alerts(gh_token):
    ord_id = os.getenv('ORG_ID')

    try:
        url = f"https://api.github.com/orgs/{ord_id}/code-scanning/alerts?per_page=100&page=1"
        response = requests.get(url,headers={"Authorization": gh_token})
        alerts = response.json()
        while 'next' in response.links.keys():
            response=requests.get(response.links['next']['url'],headers={"Authorization": gh_token})
            alerts.extend(response.json())
        
        ```
        response:
        	...
        	links:
          	next:
            	url: BLAHBALHLAH  # https://api.github.com/orgs/{ord_id}/code-scanning/alerts?per_page=100&page=2"
          ...
        ```

        with open(ALERTS_FILE, 'w') as outfile:
            outfile.write(alerts)

    except requests.exceptions.HTTPError as errh:
        logger.error(errh)
    except requests.exceptions.ConnectionError as errc:
        logger.error(errc)
    except requests.exceptions.Timeout as errt:
        logger.error(errt)
    except requests.exceptions.RequestException as err:
        logger.error(err)


def upload_to_td(data_file, td_token):
    # pass, not part of interview
    pass


def lambda_handler(event, context):
    secrets = get_secrets()
    logger.info(f'Secrets returned from Secrets Manager')
    collect_alerts(secrets['gh_token'])
    logger.info(f'Github Security alerts returned')
    upload_to_td(secrets['td_token'])
    logger.info(f'Github data uploaded to Treasure Data')

