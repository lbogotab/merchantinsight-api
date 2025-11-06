from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.commerce import Commerce
from app.models.commerce_observation import CommerceObservation

router = APIRouter(prefix="/commerces", tags=["Observations"])


@router.post("/observation/{commerce_code}")
def add_observation(commerce_code: str, comment: str, db: Session = Depends(get_db)):
    """
    Agrega una observación al comercio identificado por su código.
    """
    commerce = db.query(Commerce).filter(Commerce.code == commerce_code).first()
    if not commerce:
        raise HTTPException(status_code=404, detail=f"Comercio {commerce_code} no encontrado")

    new_obs = CommerceObservation(
        commerce_id=commerce.id,
        comment=comment
    )
    db.add(new_obs)
    db.commit()
    db.refresh(new_obs)

    return {
        "mensaje": "Observación agregada correctamente",
        "observacion": {
            "id": new_obs.id,
            "comercio": commerce.code,
            "comentario": new_obs.comment,
            "fecha": new_obs.created_at
        }
    }


@router.get("/observation/{commerce_code}")
def get_observations(commerce_code: str, db: Session = Depends(get_db)):
    """
    Lista todas las observaciones registradas para un comercio.
    """
    commerce = db.query(Commerce).filter(Commerce.code == commerce_code).first()
    if not commerce:
        raise HTTPException(status_code=404, detail=f"Comercio {commerce_code} no encontrado")

    observations = db.query(CommerceObservation).filter(CommerceObservation.commerce_id == commerce.id).all()
    return [
        {
            "id": o.id,
            "comentario": o.comment,
            "fecha": o.created_at
        }
        for o in observations
    ]