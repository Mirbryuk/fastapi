from fastapi import APIRouter, status, Response, Path, Depends
from typing import Union, List
from sql_app import models, schemas, crud
from utils.defaultResponse import DefaultResponse
from sql_app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/api",
    tags=["driver"]
)

responses = {
    status.HTTP_404_NOT_FOUND: {"model": DefaultResponse, "description": "Item not found"}
}


@router.get("/drivers/", response_model=Union[List[schemas.Driver], None], status_code=status.HTTP_200_OK)
def read_drivers(db: Session = Depends(get_db)):
    all_drivers = crud.get_all(models.Driver, db)
    return all_drivers


@router.get("/drivers/{id}", response_model=Union[schemas.Driver, DefaultResponse],
            responses={**responses, status.HTTP_200_OK: {"model": schemas.Driver}})
def get_driver(id: int, response: Response, db: Session = Depends(get_db)):
    driver: models.Driver = crud.get_by_id(models.Driver, id, db)
    if driver == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="Driver not found")

    return driver


@router.post("/drivers", response_model=DefaultResponse, status_code=status.HTTP_200_OK)
def create_driver(driver: schemas.CreateDriver, db: Session = Depends(get_db)):
    crud.create(models.Driver, driver, db)
    return DefaultResponse(success=True, message="Driver successfully created")


@router.put("/drivers", response_model=Union[schemas.UpdateDriver, DefaultResponse],
            responses={**responses, status.HTTP_200_OK: {"model": schemas.Driver}})
def update_driver(driver: schemas.Driver, response: Response, db: Session = Depends(get_db)):
    updated_driver: schemas.Driver = crud.update(models.Driver, driver, db)
    if updated_driver == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="Driver not found")

    return updated_driver


@router.patch("/drivers", response_model=Union[schemas.PatchDriver, DefaultResponse],
              responses={**responses, status.HTTP_200_OK: {"model": schemas.Driver}})
def patch_driver(driver: schemas.PatchDriver, response: Response, db: Session = Depends(get_db)):
    updated_driver: schemas.Driver = crud.update(models.Driver, driver, db)
    if updated_driver == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="Driver not found")

    return updated_driver


@router.delete("/drivers/{id}", response_model=DefaultResponse,
               responses={**responses, status.HTTP_200_OK: {"model": DefaultResponse}})
def remove_driver(id: int, response: Response, db: Session = Depends(get_db)):
    driver: models.Driver = crud.get_by_id(models.Driver, id, db)
    if driver == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="Driver not found")

    crud.delete(models.Driver, id, db)

    return DefaultResponse(success=True, message="Driver successfully removed")