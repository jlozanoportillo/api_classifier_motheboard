# API Clasificador de Placas Electrónicas

API REST en FastAPI que permite predecir la clase de una placa electrónica usando un modelo `.h5`.

## Cómo usar

1. Construye el entorno virtual e instala dependencias:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Ejecuta localmente:

```bash
uvicorn app.main:app --reload
```

3. Prueba el endpoint:

```bash
curl -X POST http://localhost:8000/predict \
  -F "file=@ruta/a/una/imagen.jpg"
```
.
```bash
curl -X POST http://localhost:8000/predict-url \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "url=https://boxparts.pe/wp-content/uploads/2023/10/Placa-madre-H55-coolmark-2.png"
```
## Despliegue automático

Este proyecto se despliega automáticamente en Google Cloud Run usando GitHub Actions.

---

Listo para usar. 🚀