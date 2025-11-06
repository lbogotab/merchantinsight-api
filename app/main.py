from fastapi import FastAPI
from app.routers import hello, commerce_detail, commerce_observation, commerce_detail_lite
from app.db import engine, Base
from app.seeds.seed_main import run_all_seeds

def create_app() -> FastAPI:
    app = FastAPI(title="MerchantInsight API", version="1.0.0")

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    run_all_seeds()

    app.include_router(hello.router)
    app.include_router(commerce_detail.router)
    app.include_router(commerce_observation.router)
    app.include_router(commerce_detail_lite.router)
    return app

app = create_app()