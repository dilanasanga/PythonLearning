import requests
import boto3

# AWS Route 53 Health Check Configuration
health_check_id = "9b4653e6-71fb-4c64-99ee-47687e880110"

# Remote API Configuration
remote_api_url = "https://api.statuspage.io/v1/pages/6z7rsdlfvd1h/components/2mf3ytrcm7df"
remote_api_token = "22824f84-0a96-4621-8b41-81fda4120e45"

# Check Route 53 Health Check Status
route53 = boto3.client('route53')
response = route53.get_health_check_status(HealthCheckId=health_check_id)

print(response)
status = response['HealthCheckObservations'][0]['Status']




if status == 'Failure':
    # Prepare payload for the remote API
    payload = {
                "component": {
                "description": "Test",
                "status": "Down",
                "name": "string",
                "only_show_if_degraded": true,
                "group_id": "string",
                "showcase": true,
                "start_date": "2023-08-18"
                }
}

    # Prepare headers for the remote API
    headers = {
        "Authorization": f"Bearer {remote_api_token}",
        "Content-Type": "application/json"
    }

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
else:
    print("Health check status is not 'Failure'")
