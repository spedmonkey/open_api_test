import requests

# Define the URLs for JSON and YAML OpenAPI specs
json_url = 'http://127.0.0.1:5000/swagger.json'
yaml_url = 'http://127.0.0.1:5000/swagger.yaml'

# Fetch and save the JSON OpenAPI spec
try:
    json_response = requests.get(json_url)
    if json_response.status_code == 200:
        with open('openapi_spec.json', 'w') as json_file:
            json_file.write(json_response.text)
        print("Saved JSON OpenAPI spec to 'openapi_spec.json'")
    else:
        print(f"Failed to retrieve JSON OpenAPI spec. Status code: {json_response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching JSON OpenAPI spec: {e}")

# Fetch and save the YAML OpenAPI spec
try:
    yaml_response = requests.get(yaml_url)
    if yaml_response.status_code == 200:
        with open('openapi_spec.yaml', 'w') as yaml_file:
            yaml_file.write(yaml_response.text)
        print("Saved YAML OpenAPI spec to 'openapi_spec.yaml'")
    else:
        print(f"Failed to retrieve YAML OpenAPI spec. Status code: {yaml_response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching YAML OpenAPI spec: {e}")