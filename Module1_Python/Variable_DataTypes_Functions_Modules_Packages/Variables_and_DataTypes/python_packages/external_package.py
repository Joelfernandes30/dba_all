import requests



response = requests.post("https://www.google.com", data={"key": "value"})


print(response.text)