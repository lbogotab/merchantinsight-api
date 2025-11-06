from fastapi import APIRouter

router = APIRouter(prefix="/hello", tags=["hello"])

@router.get("/", summary="Hola mundo")
def hello_world():
    return {"message": "Hola Mundo"}