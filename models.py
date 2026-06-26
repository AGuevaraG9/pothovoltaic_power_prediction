from sqlalchemy import Column, Float, Integer

from database import Base


class PhotovoltaicPower(Base):
    __tablename__ = "photovoltaic_power"

    id = Column(Integer, primary_key=True, index=True)
    ambient_temperature_c = Column(Float, nullable=False)
    global_horizontal_irradiance_wm2 = Column(Float, nullable=False)
    global_irradiance_30deg_wm2 = Column(Float, nullable=False)
    wind_speed_ms = Column(Float, nullable=False)
    wind_direction_deg = Column(Float, nullable=False)
    pv_power_watts = Column(Float, nullable=False)
