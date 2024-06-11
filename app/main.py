from fastapi import FastAPI
from app.api import users
from app.database import engine, Base

# Create all tables in the database.
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the user routes.
app.include_router(users.router, prefix="/users", tags=["users"])
