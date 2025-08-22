# backend/app/main.py
from fastapi import FastAPI
from app.core.config import setup_cors
from app.modulo.inmuebles.routes.inmuebles_routes import router as inmuebles_router

app = FastAPI(title="API Inmobiliaria Modular")
setup_cors(app)


app.include_router(inmuebles_router)