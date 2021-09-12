from fastapi import FastAPI

from .apis.person_api import router as personRouter
from .apis.room_api import router as roomRouter

app = FastAPI()


app.include_router(personRouter)
app.include_router(roomRouter)
