# Emotional-Music
Finds a Playlist based on your emotions. Using facial Recognition.

I have used Microsofts Emotion API, which scans pictures and asses the emotion.
This program will use the values given to each emotion to look through a list of songs that are associated with each emotion and choose 
a random song from the corresponding emotion "playlist".

# What I learned
This really taught me how to use API's and things like headers. I used spotipy, and Microsoft Emotion. I also used requests for the first time with python. 

# What I struggled with
My main problem was finding something that would play an actual playlist from spotify, at the moment I have not found an API or library that is cable of doing that so what I did, was use spotipy's "track()" feature to choose a random song from playlists that are associated with moods. The way I did this was take the top five URI's for each mood play list put them in a list and use the random library that is built into python to choose a song from each emotions list.
