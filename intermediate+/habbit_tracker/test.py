import requests

response = requests.head(url=("https://pixe.la/v1/users/kyotunn/graphs/firstgraph.html"))
print(response.status_code)
print("SAD")
