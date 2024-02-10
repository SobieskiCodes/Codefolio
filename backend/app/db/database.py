import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy.exc import OperationalError

SQLALCHEMY_DATABASE_URL = "sqlite:///app/db/app.db"
check_same_thread = True
if SQLALCHEMY_DATABASE_URL.startswith("sqlite:///"):
    # only matters for sqlite
    check_same_thread = False

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": check_same_thread})

# Check if the database file exists for SQLite
if SQLALCHEMY_DATABASE_URL.startswith("sqlite:///"):
    db_file = SQLALCHEMY_DATABASE_URL.replace("sqlite:///", "")
    if not os.path.exists(db_file):
        print("Database didn't exist, creating it.")
        # Create the database file by creating all tables
        Base = declarative_base()
        Base.metadata.create_all(bind=engine)
    else:
        # Check if the tables are created
        try:
            inspector = Inspector.from_engine(engine)
            if not inspector.get_table_names():
                # Create tables if they do not exist
                print("Tables didn't exist, creating them.")
                Base = declarative_base()
                Base.metadata.create_all(bind=engine)
        except OperationalError:
            print("Couldn't connect to the database. Please check the database configuration.")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
