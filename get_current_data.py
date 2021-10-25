import requests

data = requests.get('https://observatory.middlebury.edu/campus/energy/')

print(data.content)