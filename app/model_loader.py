from tensorflow.keras.models import load_model
import os
from google.cloud import storage
import tempfile

GCS_BUCKET_NAME = "api-classifier-bucket-model"
GCS_MODEL_PATH = "tensorfow-model/modelo_placas.h5"

def download_model_from_gcs(bucket_name, gcs_path):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(gcs_path)

    #creando archivo temporal
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".h5")
    blob.download_to_filename(tmp_file.name)
    return tmp_file.name

model_file_path = download_model_from_gcs(GCS_BUCKET_NAME, GCS_MODEL_PATH)
model = load_model(model_file_path)
print("✅ Modelo cargado correctamente!")


