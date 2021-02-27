from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scheme import *
from SQLighter import *
import json

app = FastAPI()

origins = [
    "http://194.58.122.45:6537/",
    "https://194.58.122.45:6537/",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/User/")
async def createUser(user: User):
    db_worker = SQLighter("maindatabase.db")
    db_worker.send_user(user.SberId, user.Name, user.Age, user.Gender, user.Active)
    db_worker.close()
    return user

@app.post('/SberId/')
async def createSberId(sber_id: int):
    db_worker = SQLighter("maindatabase.db")
    db_worker.send_sber_id(sber_id)
    db_worker.close()
    #uvicorn main:app --port 6536 --host 194.58.122.45
    return sber_id

@app.post('/CategoryExercises/')
async def createCategoryExercises(categ: Categoriya):
    db_worker = SQLighter("maindatabase.db")
    db_worker.send_category(categ.Name)
    db_worker.close()
    return categ

@app.post("/ProgressAchieve/")
async def createProgressAchieve(achiv: Progres):
    db_worker = SQLighter("maindatabase.db")
    db_worker.send_progres(achiv.UserId, achiv.Date, achiv.Completed)
    db_worker.close()
    return achiv

@app.get("/UsersBySberId/")
async def getUsersBySberId(sber_id: int):
    db_worker = SQLighter("maindatabase.db")
    user = db_worker.get_users_by_sberid(sber_id)
    db_worker.close()
    return user

@app.get("/AllCategoriesExirc/")
async def getAllCategoriesExirc():
    db_worker = SQLighter("maindatabase.db")
    Categ = db_worker.get_all_category()
    db_worker.close()
    return Categ

@app.get("/CategoryById/")
async def getCategoryById(category_id: int):
    db_worker = SQLighter("maindatabase.db")
    categById = db_worker.get_category_by_id(category_id)
    db_worker.close()
    return categById

@app.get("/AllGroupsExercises/")
async def getAllGroupsExercises():
    db_worker = SQLighter("maindatabase.db")
    group = db_worker.get_all_group()
    db_worker.close()
    return group

@app.get("/ExircicesfromGroup/")
async def getExircicesfromGroup(group_id: int):
    db_worker = SQLighter("maindatabase.db")
    Exircices = db_worker.get_exircices_from_group(group_id)
    db_worker.close()
    return Exircices

@app.get("/ProgressByUser/")
async def getProgressByUser(user_id: int):
    db_worker = SQLighter("maindatabase.db")
    progres = db_worker.get_progres_by_user(user_id)
    db_worker.close()
    return progres

@app.get("/Phrase/")
async def getMotivationalPhrase(motivation_id: int):
    db_worker = SQLighter("maindatabase.db")
    Phras = db_worker.get_motivations_id(motivation_id)
    db_worker.close()
    return Phras
