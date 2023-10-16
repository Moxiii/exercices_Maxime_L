from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()
class Artist(Base):
    __tablename__ = 'Artists'
    ArtistId = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
    albums = relationship("Album", back_populates="artist")

class Album(Base):
    __tablename__ = 'Albums'
    AlbumId = Column(Integer, primary_key=True, index=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('Artists.ArtistId'))
    artist = relationship("Artist", back_populates="albums")

class Track(Base):
    __tablename__ = 'Tracks'
    TrackId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey('Album.AlbumId'))
