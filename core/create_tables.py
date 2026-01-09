import sys
import os
from sqlalchemy import create_engine, text

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir) 
sys.path.append(parent_dir)

DATABASE_URL = "postgresql://postgres:3214@localhost:5432/art_db"
engine = create_engine(DATABASE_URL)

from Models import Base
from Models.Artwork import Artwork
from Models.User import User
from Models.Category import Category
from Models.Listing import Listing
from Models.Order import Order
from Models.Rating import Rating

Base.metadata.create_all(bind=engine)
    
