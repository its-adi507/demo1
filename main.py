import time
import requests
import json

url = "https://ffhx.in/testing/test/test1"

while True:
    try:
        response = requests.get(url)
        response_data = response.json()
        print(f"Response: {json.dumps(response_data, indent=2)}")
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        print(f"Raw response: {response.text}")
    
    time.sleep(3)  # wait for 1 second
