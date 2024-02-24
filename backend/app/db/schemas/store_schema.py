# Pydantic Models
# Purpose: Pydantic models are primarily used for data validation and settings management. 
# They are not directly related to the database but are used to validate and parse the data being received, for example, from a web request, 
# or being sent, for instance, in a web response.

# Data Validation and Conversion: Pydantic models ensure that incoming data matches expected types, formats, and constraints. 
# They can automatically handle type conversions, validate data, and produce detailed errors when data is invalid.

# Usage: Often used in web frameworks (like FastAPI) to define the structure and validation for request and response data in APIs. 
# They can also be used to parse and validate configuration files or environment variables.

# Dependency: Pydantic is an independent library for data validation and settings management based on Python type annotations.

from pydantic import BaseModel
from typing import List, Optional


class ItemSchema(BaseModel):
    id: int
    store_id: int
    name: str
    price: float


class StoreCreateSchema(BaseModel):
    name: str
    balance: float
    is_open: bool

class StoreSchema(BaseModel):
    id: int
    name: str
    balance: float
    is_open: bool
    #inventory: Optional[List[ItemSchema]] = []
    
class SuccessResponse(BaseModel):
    message: str
    store: Optional[StoreSchema] = None

class StoreUpdateSchema(BaseModel):
    id: int
    name: Optional[str] = None
    balance: Optional[float] = None
    is_open: Optional[bool] = None
