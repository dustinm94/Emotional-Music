import requests
import spotipy
import random


headers = {
    # Request Headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '',
}
#Image url to be analyzed
body = "{'url': '#' }"

#request handler / printing of the scores. Can be removed for more user friendly output.
r = requests.post(url='https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize',
                  data = body,
                  headers = headers)
scores = r.json()[0].get('scores')
#print(*(s for s in scores.items()), sep = '\n')

# Spotipy API
spotify = spotipy.Spotify()

#this all of the spotify URI links used below.
happy_uri = ['spotify:track:5CtI0qwDJkDQGwXD1H1cLb','spotify:track:3QWjljChcOMkRDYSzF33Qr','spotify:track:39IsH7B5byx8NRlEKlZVg9','spotify:track:3GPI7hYiqD6enLRobhkBm8','spotify:track:0FuTx2s3YH1ppmtiM6l0zI']
anger_uri = ['spotify:track:7GwtlmQVrqyoggPraFXXvJ','spotify:track:4wrZPZpjw4OI348LgWN9ZH','spotify:track:4nUdZ9HaXH02cvAbqf9C5L','spotify:track:2HwtiwV8OgIwNuj1Wq9e0B','spotify:track:5nQ9yhbHTxThaRKQLCr3QO']
contempt_uri = ['spotify:track:0wVPyqumJ4hMOb0Tjg7Qdb','spotify:track:0NVsz5lExNqzVDznhdPlU8','spotify:track:5bP9JMP7HKh1G3sJtTymgT','spotify:track:4Aq7uO12FRC7JnLqY4T7Z7','spotify:track:4RuYDrJ4a2ybcEVkSy1xFB']
disgust_uri = ['spotify:track:5ch3fw2pNFvMUaanJfIzcZ','spotify:track:7zN3sTaLDfJ7yGj9mDJryA','spotify:track:3yKdQuE97SkmrMLH3kKw56','spotify:track:60qG8XZPxvmnuWeNb5p8Kx','spotify:track:2tjb6V24kf6sDUdEFNf3m9']
fear_uri = ['spotify:track:3elOzp9X3B8vMGhJBWzbIF','spotify:track:3cuRIW5XcYEcWyWpBjIXHP','spotify:track:4gVZhkcsZcwQ4mU1gEeXEO','spotify:track:35ZHHlrMKr7CijbD239b0g','spotify:track:3y7SaLukj7ONKxdZLAoQtH']
neutral_uri = ['spotify:track:3Wwb6lBoMKXTPoB5xdmI7S','spotify:track:7lThKz6CQMfz50qGZLmj8L','spotify:track:5Ag3PsB2ukDCr2qJ2C1Sm8','spotify:track:3G7WHg3QIaximEamRszY8K','spotify:track:1uGXhKyK50NIXNqBKN73DS']
sadness_uri = ['spotify:track:4h0zU3O9R5xzuTmNO7dNDU','spotify:track:1ZGRG4rjkltlWg6jxcaWKW','spotify:track:4qPtIDBT2iVQv13tjpXMDt','spotify:track:06DaCxeg3IUMcxDkKEyQKf','spotify:track:0zP8BJOamm7Q9aNMwCby55']
surprise_uri = ['spotify:track:0vBpyfpW2lARGh3AZFtWRi','spotify:track:6XptOuDraarGwkisvMpZj5','spotify:track:79reBHqpRoWXaQbjBBY3UC','spotify:track:3oZoXyU0SkDldgS7AcN4y4','spotify:track:29Zj1r8cek15xe08vNUOLy']

def keymax(scores):
    '''this function searches through the emotion dictionary looking for the highest value then it returns the emotion associated with the highest value.'''
    v = list(scores.values())
    k = list(scores.keys())
    emotion = k[v.index(max(v))]
    return emotion


def playlist(emotion):
    '''This function finds the emotion related to the picture, it then chooses a random song from the corresponding emotional playlist and suggests it to the user.
    Example: If you are feeling happy you will be suggested a happy song, if you are feeling sad you will be suggested a sad song.'''
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

    elif emotion == 'disgust':
        rand_song = random.choice(disgust_uri)
        disgust_song = spotify.track(rand_song)
        return disgust_song['name'], disgust_song['uri']

    elif emotion == 'fear':
        rand_song = random.choice(fear_uri)
        fear_song = spotify.track(rand_song)
        return fear_song['name'], fear_song['uri']

    elif emotion == 'neutral':
        rand_song = random.choice(neutral_uri)
        neutral_song = spotify.track(rand_song)
        return neutral_song['name'], neutral_song['uri']

    elif emotion == 'sadness':
        rand_song = random.choice(sadness_uri)
        sad_song = spotify.track(rand_song)
        return sad_song['name'], sad_song['uri']

    elif emotion == 'surprise':
        rand_song = random.choice(surprise_uri)
        surprise_song = spotify.track(rand_song)
        return surprise_song['name'], surprise_song['uri']


def main(playlist, keymax):
    keymax(scores)
    playlist(keymax(scores))
    print(playlist(keymax(scores)))

main(playlist, keymax)









