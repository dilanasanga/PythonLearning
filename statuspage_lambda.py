import requests
import json

def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    print("From SNS: " + message)

    parsed_message = json.loads(message)
    alarm_name = parsed_message['AlarmName']
    alarm_status = parsed_message['NewStateValue']
    print(f"AlarmName: {alarm_name} , NewStatusValue: {alarm_status}")

# Remote API Configuration
    remote_api_url = "https://api.statuspage.io/v1/pages/xxxxxxxxxxxx/components/2mfxxxxxx"
    remote_api_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# Prepare headers for the remote API
    headers = {
        "Authorization": f"Bearer {remote_api_token}",
        "Content-Type": "application/json"
    }

    if alarm_status == 'ALARM':
    	payload ={
	    	"component": {
		    	"status": "major_outage",
		    }
		}
    elif alarm_status == 'WARNING':
        payload ={
            "component": {
                "status": "partial_outage",
            }
        }
    elif  alarm_status == 'OK':
        payload ={
            "component": {
                "status": "operational",
            }
        }
    else:
         exit()
    # Send PUT request to the remote API
    try:
        response = requests.put(remote_api_url, json=payload, headers=headers)
        if response.status_code == 200:
            print("PUT request to remote API successful")
            print("Response:", response.json())
        else:
            print("PUT request to remote API failed")
            print("Status Code:", response.status_code)
            print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error sending PUT request:", e)

    return message
