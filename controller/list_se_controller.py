from fastapi import APIRouter
from model import model
from services import list_de_services

listde_router = APIRouter(
  prefix="/list"
)

list_de_services = list_de_services.ListServices()

@listde_router.get("/")
async def get_kids_list():
    return list_de_services.get_kid().get_head()


@listde_router.post("/add")
async def add(data : model.Kid):
    list_de_services.get_kid.add(data)
    return {"code":200, "message": "creado"}