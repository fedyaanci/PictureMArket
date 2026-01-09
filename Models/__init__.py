from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .Artwork import Artwork
from .User import User
from .Category import Category
from .Listing import Listing
from .Order import Order
from .Rating import Rating

