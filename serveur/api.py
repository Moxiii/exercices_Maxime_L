from fastapi import FastAPI , Query
from fastapi.middleware.cors import CORSMiddleware
from database import get_all_artists , search_artists , get_tracks_by_album , get_albums_by_artist

app = FastAPI()

@app.get("/")
async def bdd():
    artists = get_all_artists()
    return {"artists": [artist.Name for artist in artists]}

@app.get('/artist/{artist_id}')
async def get_album(artist_id:int):
    '''
we pass ID on artist URL and that search on DB the artist with the id 
'''
    albums = get_albums_by_artist(artist_id)
    return {"album" : [album.Title for album in albums]}

@app.get("/artist/search/{artist_name}")
async def get_artist(name:str = Query(..., title="Artist Name")):
    '''
Passing name on artist url and search on DB the artists with the string in their name
'''
    artists = search_artists(name)
    return {"artists": [artist.Name for artist in artists]}

@app.get("/tracks/{album_id}")
async def get_title(album_id:int):
    '''
passsing ID on album url for fetch all title on the album by their ID 
'''
    tracks = get_tracks_by_album(album_id)
    return{"tracks":[track.Name for track in tracks]}