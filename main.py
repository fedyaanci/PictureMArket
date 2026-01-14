import uvicorn
from api.api import app
from core.database_config import Base, engine
import asyncio
from utils.load_artworks_to_bd import LoadArtworksBegin

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="127.0.0.1", 
        port=8000, 
        reload=True
    )

#asyncio.run(LoadArtworksBegin())