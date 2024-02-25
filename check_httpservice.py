import requests

def validate_return_body(url, expected_body):
    response = requests.get(url)
    actual_body = response.text

    if response.status_code != 200:
        print(f"Error: Unexpected status code {response.status_code}")
        return False

    if actual_body == expected_body:
        print("Success: Return body is valid")
        return True
    else:
        print(f"Error: Unexpected return body\nExpected: {expected_body}\nActual: {actual_body}")
        return False

# Example usage
url = "https://dev.cart.fabric.inc/v3/carts/health"
expected_body = '{"status":"UP"}'
validate_return_body(url, expected_body)
