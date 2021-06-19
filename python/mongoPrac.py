from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

all_songs = list(db.genie.find({'_id' : False}))
for song in all_songs:
    artist = song['artist']
    count = list(db.genie.find({'artist':artist}))
    if count > 1:
        print(artist)