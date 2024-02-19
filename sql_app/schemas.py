from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Union, Annotated


class BaseSchema(BaseModel):
    id: Annotated[int, Field(gt=0)]


# Trip schemas
class Trip(BaseSchema):
    driver_id: Annotated[int, Field(gt=0)]
    departure_time: datetime

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "1",
                "driver_id": "2",
                "departure_time": "2024-01-06 22:01:02"
            }
        }


class CreateTrip(Trip):
    id: None = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "driver_id": "2",
                "departure_time": "2024-01-06 22:01:02"
            }
        }


class UpdateTrip(Trip):
    pass


class PatchTrip(Trip):
    driver_id: Annotated[Union[int, None], Field(gt=0)] = None
    departure_time: Union[datetime, None] = None


# Driver schemas
class Driver(BaseSchema):
    last_name: Annotated[str, Field(max_length=30)]
    first_name: Annotated[str, Field(max_length=30)]
    patronymic: Annotated[str, Field(max_length=30)]
    passport: Annotated[str, Field(max_length=10, min_length=10, pattern=r'^\d*$')]
    experience: date

    trips: list[Trip] = []

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "1",
                "last_name": "Biryuk",
                "first_name": "Mariya",
                "patronymic": "Denisovna",
                "passport": "0123456789",
                "experience": "2023-02-10"
            }
        }


class CreateDriver(Driver):
    id: None = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "last_name": "Biryuk",
                "first_name": "Mariya",
                "patronymic": "Denisovna",
                "passport": "0123456789",
                "experience": "2023-02-10"
            }
        }


class UpdateDriver(Driver):
    pass


class PatchDriver(Driver):
    last_name: Annotated[Union[str, None], Field(max_length=30)] = None
    first_name: Annotated[Union[str, None], Field(max_length=30)] = None
    patronymic: Annotated[Union[str, None], Field(max_length=30)] = None
    passport: Annotated[Union[str, None], Field(max_length=10, min_length=10, pattern=r'^\d*$')] = None
    experience: Union[date, None] = None


# User schemas
class User(BaseSchema):
    last_name: Annotated[str, Field(max_length=30)]
    first_name: Annotated[str, Field(max_length=30)]
    patronymic: Annotated[str, Field(max_length=30)]
    group: Annotated[str, Field(max_length=10)]

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "1",
                "last_name": "Biryuk",
                "first_name": "Mariya",
                "patronymic": "Denisovna",
                "group": "4.105-1"
            }
        }


class CreateUser(User):
    id: None = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "last_name": "Biryuk",
                "first_name": "Mariya",
                "patronymic": "Denisovna",
                "group": "4.105-1"
            }
        }


class UpdateUser(User):
    pass


class PatchUser(User):
    last_name: Annotated[Union[str, None], Field(max_length=30)] = None
    first_name: Annotated[Union[str, None], Field(max_length=30)] = None
    patronymic: Annotated[Union[str, None], Field(max_length=30)] = None
    group: Annotated[Union[str, None], Field(max_length=10)] = None