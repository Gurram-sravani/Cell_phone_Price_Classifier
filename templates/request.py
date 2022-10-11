import requests, json
url = 'http://localhost:5000/predict'
r = requests.post(url,json={'exp':1.8,})
print(r.json())
