import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load saved model
model = load_model("retina_model.keras")

# Class labels (check folder order if needed)
class_labels = ['cataract', 'diabetic_retinopathy', 'glaucoma', 'normal']

# Take image path from user
img_path = input("Enter retina image path: ")

# Load image
img = image.load_img(img_path, target_size=(128, 128))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

# Predict
prediction = model.predict(img_array)
predicted_class = class_labels[np.argmax(prediction)]

print("\nPredicted Disease:", predicted_class)

# Cardiovascular Risk Decision
if predicted_class == "normal":
    print("Result: No Cardiovascular Risk")
else:
    print("Result: Cardiovascular Risk Detected")