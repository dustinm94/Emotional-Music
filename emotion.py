import requests
import spotipy
import random


headers = {
    # Request Headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9b1c907869b64ffdadc4ed2cc3f6596c',
}
#Image url to be analyzed
body = "{'url': 'http://www.swiss-smile-beauty.com/uploads/pics/brand1.jpg'}"

#link to API
r = requests.post(url='https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize',
                  data = body,
                  headers = headers)
scores = r.json()[0].get('scores')
print(*(s for s in scores.items()), sep = '\n')

spotify = spotipy.Spotify()

happy_uri = ['spotify:track:5CtI0qwDJkDQGwXD1H1cLb','spotify:track:3QWjljChcOMkRDYSzF33Qr','spotify:track:39IsH7B5byx8NRlEKlZVg9','spotify:track:3GPI7hYiqD6enLRobhkBm8','spotify:track:0FuTx2s3YH1ppmtiM6l0zI']
anger_uri = ['spotify:track:7GwtlmQVrqyoggPraFXXvJ','spotify:track:4wrZPZpjw4OI348LgWN9ZH','spotify:track:4nUdZ9HaXH02cvAbqf9C5L','spotify:track:2HwtiwV8OgIwNuj1Wq9e0B','spotify:track:5nQ9yhbHTxThaRKQLCr3QO']
contempt_uri = ['spotify:track:0wVPyqumJ4hMOb0Tjg7Qdb','spotify:track:0NVsz5lExNqzVDznhdPlU8','spotify:track:5bP9JMP7HKh1G3sJtTymgT','spotify:track:4Aq7uO12FRC7JnLqY4T7Z7','spotify:track:4RuYDrJ4a2ybcEVkSy1xFB']
disgust_uri = ['']
fear_uri = ['']
neutral_uri = ['']
sadness_uri = ['spotify:track:4h0zU3O9R5xzuTmNO7dNDU','spotify:track:1ZGRG4rjkltlWg6jxcaWKW','spotify:track:4qPtIDBT2iVQv13tjpXMDt','spotify:track:06DaCxeg3IUMcxDkKEyQKf','spotify:track:0zP8BJOamm7Q9aNMwCby55']
surprise = ['']

def keymax(scores):
    v = list(scores.values())
    k = list(scores.keys())
    emotion = k[v.index(max(v))]
    return emotion

print(keymax(scores))

def playlist(emotion):
    if emotion == 'happiness':
        rand_song = random.choice(happy_uri)
        happy_song = spotify.track(rand_song)
        return happy_song['name'], happy_song['uri']

    elif emotion == 'anger':
        rand_song = random.choice(anger_uri)
        anger_song = spotify.track(rand_song)
        return anger_song['name'], anger_song['uri']

    elif emotion == 'contempt':
        rand_song = random.choice(contempt_uri)
        contempt_song = spotify.track(rand_song)
        return contempt_song['name'], contempt_song['uri']
    


print(playlist(keymax(scores)))







