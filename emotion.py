import requests

headers = {
    # Request Headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'INSERT API KEY',
}
#Image url to be analyzed
body = "{'url': 'http://www.swiss-smile-beauty.com/uploads/pics/brand1.jpg'}"

r = requests.post(url='https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize',
                  data = body,
                  headers = headers)
scores = r.json()[0].get('scores')
print(*(s for s in scores.items()), sep = '\n')
