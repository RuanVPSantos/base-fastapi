from fastapi import APIRouter, Depends
from app.modules.module1.schemas import ExampleSchema
from app.modules.module1.services import example_service

router = APIRouter()

@router.get("/")
async def get_example():
    return {"message": "Module 1 works"}

@router.post("/create")
async def create_example(data: ExampleSchema):
    return example_service(data)
