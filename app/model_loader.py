from tensorflow.keras.models import load_model
import os
model_path = os.path.join(os.path.dirname(__file__), "modelo_placas.h5")
model = load_model(model_path)
print("✅ Modelo cargado correctamente")


