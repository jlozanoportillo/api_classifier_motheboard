from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from io import BytesIO
import requests

from app.labels import labels
from app.model_loader import model
from app.predict import predict_image
\

app = FastAPI(
    title="Clasificador de Placas Electrónicas",
    description="API REST para clasificar placas usando un modelo .h5",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "mensaje": "API para clasificar placas electrónicas",
        "clases_disponibles": labels,
        "cantidad_clases": len(labels)
    }

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Guardar archivo temporal en memoria
        contents = await file.read()
        img_bytes = BytesIO(contents)
        result = predict_image(model, img_bytes)
        return result
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

@app.post("/predict-url")
async def predict_from_url(url: str = Form(...)):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_bytes = BytesIO(response.content)
        result = predict_image(model, img_bytes)
        return result
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
