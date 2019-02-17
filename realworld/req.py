import requests


res = requests.get('https://data.nasa.gov/resource/y77d-th95.json', verify=False)
#res = requests.get('http://google.com', verify=False)
print(type(res))
print(res.text)
#print(type(res.json()))
#data = res.json()
#print(data)