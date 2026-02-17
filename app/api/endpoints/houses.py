from fastapi import APIRouter
from fastapi import HTTPException

from typing import List

from app.data import houses_list
from app.schemas.house import HouseDetailSchema, HouseItemSchema

houses_router = APIRouter(prefix="/houses", tags=["houses"])


@houses_router.get("/", response_model=List[HouseItemSchema])
async def houses():
    return houses_list


@houses_router.get("/{house_id}", response_model=HouseDetailSchema)
async def house_detail(house_id: int):
    for house in houses_list:
        if house["id"] == house_id:
            return house

    raise HTTPException(status_code=404, detail="House not found")
