from typing import Optional
from typing import List
import sys
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI,File, UploadFile,Request
from pydantic import BaseModel, EmailStr
from fastapi.responses import HTMLResponse
from converstion.Image_To_Text import convert 
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="./templates")


app = FastAPI()



class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

 
class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: Optional[str] = None


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.get("/")
async def root():
    return {"info": "hey this the api for the image to text "}


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

@app.post("/api/imageConversion/")
async def create_files(files: List[bytes] = File(...)):
    for file in files:
        label = convert(file)
        return {"the image output is": label}


@app.post("/api/webversion/")
async def create_files_for_web(request:Request,files: List[bytes] = File(...)):
    for file in files:
        label = convert(file)
        return templates.TemplateResponse("DisplayPage.html",{ "request":request,"file_output":label})

@app.get("/api/main")
async def main(request:Request):
    return templates.TemplateResponse("test2.html", {"request":request})