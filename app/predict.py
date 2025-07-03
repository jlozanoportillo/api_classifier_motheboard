from tensorflow.keras.preprocessing import image
import numpy as np
from app.labels import labels

def predict_image(model, img_file):
    img = image.load_img(img_file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    pred = model.predict(img_array)
    class_index = int(np.argmax(pred))
    confidence = float(np.max(pred))

    if confidence < 0.3:
        raise ValueError(f"La predicción no es confiable (confianza: {confidence:.2f})")

    return {
        "predicciones": pred.tolist(),
        "clase_predicha": class_index,
        "nombre_clase": labels.get(class_index,"Desconocido"),
        "confianza": round(confidence, 4)
    }




