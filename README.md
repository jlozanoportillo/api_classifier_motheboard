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
# uvicorn app.main:app --reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

3. Prueba el endpoint:

```bash
curl -X POST http://localhost:8080/predict \
  -F "file=@ruta/a/una/imagen.jpg"
```
"rua de windows completa por ejemplo"

.
```bash
curl -X POST http://localhost:8080/predict-url \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "url=https://boxparts.pe/wp-content/uploads/2023/10/Placa-madre-H55-coolmark-2.png"
```
## Despliegue automático

Este proyecto se despliega automáticamente en Google Cloud Run usando GitHub Actions.

---

Listo para usar. 🚀

NOTA: i usas en local tienes que authenticarte a gcloud y despues configugrar

PowerShell
```bash
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\Jose Carlos\Desktop\gcp-key.json"
```


CMD
```bash
set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\Jose Carlos\Desktop\gcp-key.json
```

Linux
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/mnt/c/Users/Jose Carlos/Desktop/gcp-key.json"
```
