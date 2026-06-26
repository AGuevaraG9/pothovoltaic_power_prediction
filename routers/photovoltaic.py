from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from ml_model import predict_power
from models import PhotovoltaicPower
from schemas import (
    PhotovoltaicPowerCreate,
    PhotovoltaicPowerPredictionResponse,
    PhotovoltaicPowerResponse,
)


router = APIRouter(
    prefix="/photovoltaic",
    tags=["photovoltaic"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/power", response_model=PhotovoltaicPowerPredictionResponse)
def photovoltaic_power_prediction(data: PhotovoltaicPowerCreate):
    pv_power_watts = predict_power(
        data.ambient_temperature_c,
        data.global_horizontal_irradiance_wm2,
        data.global_irradiance_30deg_wm2,
        data.wind_speed_ms,
        data.wind_direction_deg,
    )

    return {
        "message": "potencia fotovoltaica predicha",
        "pv_power_watts": pv_power_watts,
    }


@router.post("/", response_model=PhotovoltaicPowerResponse)
def create_photovoltaic_power(data: PhotovoltaicPowerCreate, db: Session = Depends(get_db)):
    pv_power_watts = predict_power(
        data.ambient_temperature_c,
        data.global_horizontal_irradiance_wm2,
        data.global_irradiance_30deg_wm2,
        data.wind_speed_ms,
        data.wind_direction_deg,
    )

    new_data = PhotovoltaicPower(
        ambient_temperature_c=data.ambient_temperature_c,
        global_horizontal_irradiance_wm2=data.global_horizontal_irradiance_wm2,
        global_irradiance_30deg_wm2=data.global_irradiance_30deg_wm2,
        wind_speed_ms=data.wind_speed_ms,
        wind_direction_deg=data.wind_direction_deg,
        pv_power_watts=pv_power_watts,
    )

    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data


@router.get("/", response_model=list[PhotovoltaicPowerResponse])
def get_photovoltaic_power(db: Session = Depends(get_db)):
    return db.query(PhotovoltaicPower).all()


@router.get("/{id}", response_model=PhotovoltaicPowerResponse)
def get_photovoltaic_power_by_id(id: int, db: Session = Depends(get_db)):
    photovoltaic_power = db.query(PhotovoltaicPower).filter(PhotovoltaicPower.id == id).first()

    if not photovoltaic_power:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return photovoltaic_power


@router.put("/{id}", response_model=PhotovoltaicPowerResponse)
def update_photovoltaic_power(
    id: int,
    data: PhotovoltaicPowerCreate,
    db: Session = Depends(get_db),
):
    photovoltaic_power = db.query(PhotovoltaicPower).filter(PhotovoltaicPower.id == id).first()

    if not photovoltaic_power:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    pv_power_watts = predict_power(
        data.ambient_temperature_c,
        data.global_horizontal_irradiance_wm2,
        data.global_irradiance_30deg_wm2,
        data.wind_speed_ms,
        data.wind_direction_deg,
    )

    photovoltaic_power.ambient_temperature_c = data.ambient_temperature_c
    photovoltaic_power.global_horizontal_irradiance_wm2 = data.global_horizontal_irradiance_wm2
    photovoltaic_power.global_irradiance_30deg_wm2 = data.global_irradiance_30deg_wm2
    photovoltaic_power.wind_speed_ms = data.wind_speed_ms
    photovoltaic_power.wind_direction_deg = data.wind_direction_deg
    photovoltaic_power.pv_power_watts = pv_power_watts

    db.commit()
    db.refresh(photovoltaic_power)

    return photovoltaic_power


@router.delete("/{id}")
def delete_photovoltaic_power(id: int, db: Session = Depends(get_db)):
    photovoltaic_power = db.query(PhotovoltaicPower).filter(PhotovoltaicPower.id == id).first()

    if not photovoltaic_power:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    db.delete(photovoltaic_power)
    db.commit()

    return {"message": "Registro eliminado correctamente"}
