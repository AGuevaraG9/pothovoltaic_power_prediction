from pydantic import BaseModel, Field


class PhotovoltaicPowerCreate(BaseModel):
    ambient_temperature_c: float = Field(..., example=25.5)
    global_horizontal_irradiance_wm2: float = Field(..., example=850.0)
    global_irradiance_30deg_wm2: float = Field(..., example=900.0)
    wind_speed_ms: float = Field(..., example=3.5)
    wind_direction_deg: float = Field(..., example=180.0)


class PhotovoltaicPowerPredictionResponse(BaseModel):
    message: str
    pv_power_watts: float


class PhotovoltaicPowerResponse(BaseModel):
    id: int = Field(..., example=1)
    ambient_temperature_c: float = Field(..., example=25.5)
    global_horizontal_irradiance_wm2: float = Field(..., example=850.0)
    global_irradiance_30deg_wm2: float = Field(..., example=900.0)
    wind_speed_ms: float = Field(..., example=3.5)
    wind_direction_deg: float = Field(..., example=180.0)
    pv_power_watts: float = Field(..., example=1200.5)
