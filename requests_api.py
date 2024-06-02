import requests

# Define the API endpoint
url = 'http://127.0.0.1:5000/hello/'

try:
    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Print the response
        print(f"Response from API: {data}")
    else:
        print(f"Failed to retrieve data from API. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")