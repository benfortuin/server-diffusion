from fastapi import FastAPI #, Request later to deal with checking method of requests?
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from starlette.responses import FileResponse #, RedirectResponse to redirect?
from pathlib import Path
import os

# create app
app = FastAPI()

# get directory
IMAGEDIR = os.getcwd()

# query object type
class Queries(BaseModel):
    prompt: str


async def Stable_Diffusion(prompt):
    """
    Looks for an image in `./Static/` with name `{prompt}.jpg`

    Will be where Stable Diffusion should go
    """

    img_path = Path(f"./Static/{prompt}.jpg")
    return(img_path)

# root page
@app.get("/")
async def root():
    """
    Root page of the API
    """

    return {
        "message": "hello, world"
    }

# prompt for an image
@app.post("/prompt")
async def post_query(q: Queries):
    """
    Handle a query for an image
    """

    img_path = await Stable_Diffusion(q.prompt)
    return FileResponse(img_path)
