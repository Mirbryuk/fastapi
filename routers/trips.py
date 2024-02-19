from fastapi import APIRouter, status, Response, Path, Depends
from typing import Union, List
from sql_app import models, schemas, crud
from utils.defaultResponse import DefaultResponse
from sql_app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/api",
    tags=["trip"]
)

responses = {
    status.HTTP_404_NOT_FOUND: {"model": DefaultResponse, "description": "Item not found"}
}


@router.get("/trips/", response_model=Union[List[schemas.Trip], None], status_code=status.HTTP_200_OK)
def read_trips(db: Session = Depends(get_db)):
    all_trips = crud.get_all(models.Trip, db)
    return all_trips


@router.get("/trips/{id}", response_model=Union[schemas.Trip, DefaultResponse],
            responses={**responses, status.HTTP_200_OK: {"model": schemas.Trip}})
def get_trip(id: int, response: Response, db: Session = Depends(get_db)):
    trip: models.Trip = crud.get_by_id(models.Trip, id, db)
    if trip == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="Trip not found")

    return trip


@router.post(
    "/trips",
    response_model=DefaultResponse,
    responses={status.HTTP_404_NOT_FOUND: {"description": "Driver with such id not found"},
               status.HTTP_200_OK: {"description": "Trip successfully created"}}
)
def create_trip(trip: schemas.CreateTrip, response: Response, db: Session = Depends(get_db)):
    driver: models.Driver = crud.get_by_id(models.Driver, trip.driver_id, db)
    if driver is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="Driver with such id not found")

    crud.create(models.Trip, trip, db)
    return DefaultResponse(success=True, message="Trip successfully created")


@router.put("/trips", response_model=Union[schemas.UpdateTrip, DefaultResponse],
            responses={**responses, status.HTTP_200_OK: {"model": schemas.Trip}})
def update_trip(trip: schemas.Trip, response: Response, db: Session = Depends(get_db)):
    driver: models.Driver = crud.get_by_id(models.Driver, trip.driver_id, db)
    if driver is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="Driver with such id not found")

    updated_trip: schemas.Trip = crud.update(models.Trip, trip, db)
    if updated_trip == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="Trip not found")

    return updated_trip


@router.patch("/trips", response_model=Union[schemas.PatchTrip, DefaultResponse],
              responses={**responses, status.HTTP_200_OK: {"model": schemas.Trip}})
def patch_trip(trip: schemas.PatchTrip, response: Response, db: Session = Depends(get_db)):
    if trip.driver_id is not None:
        driver: models.Driver = crud.get_by_id(models.Driver, trip.driver_id, db)
        if driver is None:
            response.status_code = status.HTTP_404_NOT_FOUND
            return DefaultResponse(success=False, message="Driver with such id not found")

    updated_trip: schemas.Trip = crud.update(models.Trip, trip, db)
    if updated_trip == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="Trip not found")

    return updated_trip


@router.delete("/trips/{id}", response_model=DefaultResponse,
               responses={**responses, status.HTTP_200_OK: {"model": DefaultResponse}})
def remove_trip(id: int, response: Response, db: Session = Depends(get_db)):
    trip: models.Trip = crud.get_by_id(models.Trip, id, db)
    if trip == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="Trip not found")

    crud.delete(models.Trip, id, db)

    return DefaultResponse(success=True, message="Trip successfully removed")