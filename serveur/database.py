from sqlalchemy import create_engine , MetaData 
from sqlalchemy.orm import sessionmaker
from models import Album, Artist , Track
engine = create_engine("sqlite:///../chinook.db")
cur = engine.connect()
metadata = MetaData()
metadata.reflect(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_all_artists():
    db = SessionLocal()
    try:
        artists = db.query(Artist).all()
        return artists
    finally:
        db.close()

def search_artists(name):
    db = SessionLocal()
    try:
        artists = db.query(Artist).filter(Artist.Name.like(f"%{name}%")).all()
        return artists
    finally:
        db.close()

def get_tracks_by_album(album_id: int):
    db = SessionLocal()
    try:
        tracks = db.query(Track).filter(Track.AlbumId == album_id).all()
        
        return tracks
    finally:
        db.close()

def get_albums_by_artist(artist_id: int):
    db = SessionLocal()
    try:
        albums = db.query(Album).filter(Album.ArtistId == artist_id).all()
        return albums
    finally:
        db.close()
