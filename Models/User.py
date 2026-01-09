from sqlalchemy import Integer, String, Boolean, Column, TIMESTAMP
from sqlalchemy.orm import relationship  
from datetime import datetime
from . import Base

class User(Base):
    __tablename__ = "user"  
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_artist = Column(Boolean, default=False)
    avatar_url = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.now)

    artworks = relationship("Artwork", backref="seller", foreign_keys="[Artwork.artist_id]")
    ratings_given = relationship("Rating", backref="reviewer")
    orders = relationship("Order", backref="buyer")
    listings = relationship("Listing", backref="seller")  