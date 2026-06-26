import joblib
import numpy as np


# Cargar el mejor modelo y los escaladores
best_model_loaded = joblib.load('random_forest_opt_5_n=40_d=12_model.pkl')
scaler_X_loaded = joblib.load('scaler_x.pkl')
scaler_y_loaded = joblib.load('scaler_y.pkl')


print("\n--- Ingrese los valores ambientales para la predicción ---")


try:
    # X_cols: ['ambient_temperature_c', 'global_horizontal_irradiance_wm2', 'global_irradiance_30deg_wm2', 'wind_speed_ms', 'wind_direction_deg']
    temp = float(input("Temperatura ambiente en °C: "))
    irradiance_h = float(input("Irradiancia horizontal global en wm2: "))
    irradiance_30 = float(input("Irradiancia global a 30 grados en wm2: "))
    wind_speed = float(input("Velocidad del viento en m/s: "))
    wind_direction = float(input("Dirección del viento en grados: "))


    # Crear un array con los valores ingresados por el usuario
    user_input_values = np.array([
        temp,
        irradiance_h,
        irradiance_30,
        wind_speed,
        wind_direction
    ])


    # Reestructurar para StandardScaler (1 muestra, n_características)
    user_input_arr = user_input_values.reshape(1, -1)


    # Estandarizar el valor de entrada usando el scaler cargado para X
    user_input_scaled = scaler_X_loaded.transform(user_input_arr)


    # Realizar la predicción con el modelo cargado
    predicted_pv_power_scaled = best_model_loaded.predict(user_input_scaled)


    # Asegurar la forma 2D para inverse_transform si es 1D
    if predicted_pv_power_scaled.ndim == 1:
        predicted_pv_power_scaled = predicted_pv_power_scaled.reshape(-1, 1)


    # Invertir la estandarización para obtener el valor real de 'pv_power_watts'
    predicted_pv_power = scaler_y_loaded.inverse_transform(predicted_pv_power_scaled)


    print(f"\nPotencia fotovoltaica predicha: {predicted_pv_power[0][0]:.2f} watts")
except ValueError:
    print("Error: Por favor, ingrese valores numéricos válidos.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

