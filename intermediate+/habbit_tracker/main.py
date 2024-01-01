import requests
import os

USERNAME = "kyotunn"
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"
pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_parameters = {
    "username": USERNAME,
    "token": PIXELA_TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# # Give the user datas to the pixela to create a user acc.
# response = requests.post(url=pixela_endpoint, json=user_parameters)

# # Print the response text to see if it was successful
# print(response.text)

# Set the config for graph
graph_config = {
    "id": "firstgraph",
    "name": "Reading Graph",
    "unit": "Page",
    "type": "float",
    "color": "kuro"
}

# Get the response for graph if is successful and print the response.
response_graph = requests.post(url=pixela_graph_endpoint, json=graph_config, headers=headers)
print(response_graph.text)