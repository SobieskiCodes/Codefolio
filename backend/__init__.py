# myapp/
# |-- backend/
#     |-- app/
#         |-- api/
#             |-- endpoints/
#                 |-- user.py
#                 |-- project.py
#         |-- core/
#             |-- config.py
#         |-- crud/
#             |-- crud_user.py
#             |-- crud_project.py
#         |-- db/
#             |-- session.py
#             |-- base_class.py
#         |-- models/
#             |-- user.py
#             |-- project.py
#         |-- schemas/
#             |-- user.py
#             |-- project.py
#         |-- tests/
#             |-- test_main.py
#             |-- test_user.py
#         |-- main.py


# Model Layer (SQLAlchemy Models): 
# This layer, where your StoreModel, ItemModel, etc., are defined, 
# is primarily for defining the database schema and the relationships between different entities. 
# It's best to keep these models focused on what the data is and how it's structured.

# Data Access Layer (CRUD Functions): 
# This layer consists of functions or methods that directly interact with the database to perform 
# Create, Read, Update, Delete (CRUD) operations. 
# These functions typically use the models defined in the model layer to interact with the database.

# Business Logic Layer: This layer contains the core logic of your application, 
#which may include functions and methods that process data, perform calculations, and make decisions.

# Presentation Layer (API Endpoints, Views): 
# This layer handles the interaction with the outside world (like API endpoints in a web application). 
# It calls upon the business logic layer and data access layer to perform actions based on the requests received.