from sqlalchemy.orm import Session
from app.db.models.store_model import Store, Item
from app.db.schemas.store_schema import StoreSchema 

def get_store(db: Session, store_id: int):
    store = db.query(Store).filter(Store.id == store_id).first()
    return store.to_dict() if store else None

def get_all_stores(db: Session):
    return [store.to_dict() for store in db.query(Store).all()]

def create_store(db: Session, store_data: StoreSchema):
    db_store = Store(**store_data.dict())
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store.to_dict()


# Additional CRUD operations for Item and other functionalities can be added here
