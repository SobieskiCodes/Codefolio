
# Endpoint Layer (API Layer):

# In frameworks like FastAPI, the endpoint layer is where you receive API requests and send responses.
# Here, you typically use Pydantic models to define the structure and validation for the incoming request data and the outgoing response data.
# When a request comes in, FastAPI automatically validates the request data against the defined Pydantic model and passes the validated data to your endpoint function.
# The endpoint layer is often responsible for converting the Pydantic model into a format that the business logic layer can work with, which could be a dictionary,
# a simple Python object, or directly passing the Pydantic model.

from fastapi import Depends, APIRouter, HTTPException, Request, responses
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from fastapi import status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.core.crud.store_crud import create_store, get_all_stores, get_store  # Assuming CRUD operations are in store_crud.py
from app.db.schemas.store_schema import StoreSchema, SuccessResponse  # Assuming Pydantic schemas are in store_schema.py
from typing import Any
router = APIRouter()

def inspect_response_data(data):
    # how to use:
    # response = create_store(db=db, store_data=store)
    # inspect_response_data(response) # this will tell you the data type.
    # TODO: we should move this to a helper in core ;D
    # Log the data for inspection
    print("Inspecting response data:", data)

    # Check if the data is a dict (you can add more checks as needed)
    if not isinstance(data, dict):
        print("Warning: Response data is not a dictionary")

    # You might want to log the type of data as well
    print("Type of response data:", type(data))

    # Return the data (or you could modify it if necessary before returning)
    return data



@router.post("/stores/", response_model=SuccessResponse)
def create_store_endpoint(store: StoreSchema, db: Session = Depends(get_db)):
    try:
        create_new_store = create_store(db=db, store_data=store)
        response_data = {
            "message": "Store created successfully",
            "store": create_new_store, 
        }
        return responses.JSONResponse(content=response_data, status_code=201)

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An internal server error occurred."
        )


@router.get("/stores/", response_model=List[StoreSchema])
def read_all_stores(db: Session = Depends(get_db)):
    stores = get_all_stores(db)
    if store is None:
        return {"detail": "No stores found"}
    return stores

@router.get("/stores/{store_id}", response_model=StoreSchema)
def read_store_by_id(store_id: int, db: Session = Depends(get_db)):
    store = get_store(db, store_id)
    if store is None:
        return {"detail": "Store not found"}
    return store


# todo: move to its own file handler.
# @app.exception_handler(SQLAlchemyError)
# def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
#     detail = f"An error occurred: {exc}"
#     logger.error(detail)

#     # Only include detailed errors in response if in debug mode
#     if app.debug:
#         return JSONResponse(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             content={"detail": detail},
#         )
#     else:
#         return JSONResponse(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             content={"detail": "An internal server error occurred."},
#         )