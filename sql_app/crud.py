from sqlalchemy.orm import Session
from .models import BaseModel
from .schemas import BaseSchema


# base CRUD operations
def get_by_id(model: BaseModel, id: int, db: Session):
    return db.query(model).filter(model.id == id).one_or_none()


def get_all(model: BaseModel, db: Session):
    return db.query(model).all()


def create(model: BaseModel, schema: BaseSchema, db: Session):
    db_model = model(**schema.dict())
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model


def update(model: BaseModel, schema: BaseSchema, db: Session):
    db_model = get_by_id(model, schema.id, db)
    if db_model is None:
        return None

    for var, value in vars(schema).items():
        setattr(db_model, var, value) if value else None

    db.commit()
    db.refresh(db_model)
    return db_model


def delete(model: BaseModel, id: int, db: Session):
    db_user = get_by_id(model, id, db)
    if db_user is None:
        return

    db.delete(db_user)
    db.commit()