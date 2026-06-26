# Photovoltaic Power Prediction


API desarrollada con FastAPI para predecir la potencia fotovoltaica generada a partir de variables medioambientales.


El proyecto utiliza un modelo de Machine Learning previamente entrenado y guardado con `joblib`. La prediccion se realiza con los siguientes datos de entrada:


- Temperatura ambiente en grados Celsius.
- Irradiancia horizontal global.
- Irradiancia global a 30 grados.
- Velocidad del viento.
- Direccion del viento.


## Tecnologias


- Python
- FastAPI
- SQLAlchemy
- Scikit-learn
- Joblib
- NumPy


## Estructura principal


- `main.py`: configuracion principal de FastAPI.
- `database.py`: conexion a la base de datos.
- `models.py`: modelo de tabla `photovoltaic_power`.
- `schemas.py`: esquemas de entrada y respuesta.
- `ml_model.py`: carga del modelo entrenado y funcion de prediccion.
- `routers/photovoltaic.py`: endpoints para prediccion y CRUD.
- `ml-test.py`: script de prueba manual del modelo.


## Endpoints principales


- `POST /photovoltaic/power`: predice la potencia fotovoltaica sin guardar el registro.
- `POST /photovoltaic/`: predice la potencia fotovoltaica y guarda el registro.
- `GET /photovoltaic/`: lista los registros guardados.
- `GET /photovoltaic/{id}`: obtiene un registro por id.
- `PUT /photovoltaic/{id}`: actualiza un registro y recalcula la prediccion.
- `DELETE /photovoltaic/{id}`: elimina un registro.


## Ejemplo de entrada


```json
{
  "ambient_temperature_c": 25.5,
  "global_horizontal_irradiance_wm2": 850.0,
  "global_irradiance_30deg_wm2": 900.0,
  "wind_speed_ms": 3.5,
  "wind_direction_deg": 180.0
}
```


## Ejecucion


Instalar dependencias:


```bash
pip install -r requirements.txt
```


Levantar el servidor:


```bash
uvicorn main:app --reload
```


La documentacion interactiva estara disponible en:


```text
http://127.0.0.1:8000/docs
```



