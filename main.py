from fastapi import FastAPI
from database import create_tables
from controllers import router

app = FastAPI()
app.include_router(router)
create_tables()

