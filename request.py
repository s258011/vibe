import requests
url = 'https://vibe-3vw6grlt2q-lz.a.run.app/image'
files = {'file': open('rock1.png', 'rb')}
resp = requests.post(url, files=files)
print(resp.text)
