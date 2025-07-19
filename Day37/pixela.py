import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "epsilonstar-02"
TOKEN = "intotheunknown"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}

pixel_data = {
    "quantity": "25"
}


pixel_response = requests.delete(url=f"{PIXEL_ENDPOINT}/20250610", headers=headers)
print(pixel_response.text)