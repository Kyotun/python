import requests
import os
from datetime import datetime


USERNAME = "kyotunn"
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "firstgraph"
DATE = datetime(year=2024, month=1, day=1).strftime("%Y%m%d")
QUANTITY = "20"


# Parameter for using api(our token)
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# CREATE A USER ACCOUNT
pixela_endpoint = "https://pixe.la/v1/users"
# Parameters for user account creation
user_parameters = {
    "username": USERNAME,
    "token": PIXELA_TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# # Give the user datas to the pixela to create a user acc.
# response_user_acc = requests.post(url=pixela_endpoint, json=user_parameters)
# # Print the response text to see if it was successful
# print(response_user_acc.text)


# CREATE A NEW GRAPH
pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# Parameters for creating a new graph
graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Page",
    "type": "float",
    "color": "kuro"
}
# # Get the response for graph if is successful and print the response.
# response_graph = requests.post(url=pixela_graph_endpoint, json=graph_config, headers=headers)
# print(response_graph.text)


# PUT A NEW PIXEL
pixela_record_endpoint = f"{pixela_graph_endpoint}/{GRAPH_ID}"
# # Parameters for recording a new entry for graph
record_config = {
    "date": DATE,
    "quantity": QUANTITY,
}
# response_record = requests.post(url=pixela_record_endpoint, json=record_config, headers=headers)
# print(response_record.text)

# UPDATE A PIXEL
edit_config = {
    "quantity": QUANTITY
}
pixela_edit_endpoint = f"{pixela_record_endpoint}/{DATE}"
# response_edit = requests.put(url=pixela_edit_endpoint, json=edit_config, headers=headers)
# print(response_edit.text)


# DELETE A PIXEL
pixela_delete_pixel_endpoint = f"{pixela_record_endpoint}/{DATE}"
response_delete = requests.delete(url=pixela_delete_pixel_endpoint, headers=headers)
print(response_delete.text)
