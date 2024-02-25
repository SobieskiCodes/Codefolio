from fastapi import FastAPI
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db.database import SessionLocal, engine
from app.db.models import store_model
from app.api.endpoints.store_endpoint import router as store_router  
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
store_model.Base.metadata.create_all(bind=engine)
from dotenv import load_dotenv


# Load the environment variables from .env file
load_dotenv('/workspaces/.codespaces/shared/.env')

# Now, you can directly access the variables
CODESPACE_NAME = os.getenv('CODESPACE_NAME')

origins = [
    f"https://{CODESPACE_NAME}-3000.app.github.dev", 
    "localhost"
]
# ^ another reason to need a url lol


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(store_router, prefix="/api/classwork/store")  # You can specify a prefix if desired


# @app.exception_handler(ValidationError)
# async def validation_exception_handler(request: Request, exc: ValidationError):
#     # Format the validation errors as you like
#     errors = []
#     for error in exc.errors():
#         error_item = {
#             "location": error['loc'],
#             "message": error['msg'],
#             "type": error['type']
#         }
#         errors.append(error_item)

#     # Return a JSON response with the error details and a 422 Unprocessable Entity status
#     return JSONResponse(
#         status_code=422,
#         content={
#             "detail": errors,
#             "body": await request.json()  # Including the original body can be helpful
#         },
#     )

@app.get("/")
def read_root():
    return {"Hello": f"{CODESPACE_NAME}"}

if __name__ == "__main__":
    uvicorn.run(app)