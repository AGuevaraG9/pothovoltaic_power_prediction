import joblib
import numpy as np


# Cargar el mejor modelo y los escaladores
model = joblib.load("./model/random_forest_opt_5_n=40_d=12_model.pkl")
scaler_X = joblib.load("./model/scaler_x.pkl")
scaler_y = joblib.load("./model/scaler_y.pkl")


def predict_power(
    ambient_temperature_c: float,
    global_horizontal_irradiance_wm2: float,
    global_irradiance_30deg_wm2: float,
    wind_speed_ms: float,
    wind_direction_deg: float,
) -> float:
    user_input_values = np.array(
        [
            ambient_temperature_c,
            global_horizontal_irradiance_wm2,
            global_irradiance_30deg_wm2,
            wind_speed_ms,
            wind_direction_deg,
        ]
    )

    user_input_arr = user_input_values.reshape(1, -1)
    user_input_scaled = scaler_X.transform(user_input_arr)
    predicted_pv_power_scaled = model.predict(user_input_scaled)

    if predicted_pv_power_scaled.ndim == 1:
        predicted_pv_power_scaled = predicted_pv_power_scaled.reshape(-1, 1)

    predicted_pv_power = scaler_y.inverse_transform(predicted_pv_power_scaled)
    power = round(float(predicted_pv_power[0][0]), 2)

    return power
