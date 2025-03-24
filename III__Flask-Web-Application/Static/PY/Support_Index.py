#
#
import os

#
#
from PIL import Image

#
#
from keras._tf_keras.keras.utils import img_to_array

#
#
from keras._tf_keras.keras.models import load_model

#
#
import numpy as np




#
allowed_extensions = ["jpg","jpeg"]




#
def find_currently_available_models():
    
    #
    paths_for_current_models = []
    project_root_directory = os.path.dirname(os.getcwd())
    parent_subdirectory_for_models = os.path.join(project_root_directory,"II__Deepfake-Detection-Models")

    #
    for folder in os.listdir(parent_subdirectory_for_models):
        folder_path = os.path.join(str(parent_subdirectory_for_models),folder)
        for file in os.listdir(folder_path):
            if (".keras" in file):
                file_path = os.path.join(str(folder_path),file)
                paths_for_current_models.append(file_path)
    
    #
    return paths_for_current_models




#
def is_file_allowed(uploaded_file_name):
    
    #
    return (("." in uploaded_file_name) and (uploaded_file_name.rsplit(".", 1)[1].lower() in allowed_extensions))




#
def image_classification_prediction(uploaded_file,picked_model_path):

    #
    image_original = Image.open(uploaded_file)

    #
    image_resized = image_original.resize((224,224))
    image_array = img_to_array(image_resized)
    image_expanded = np.expand_dims(image_array,axis=0)
    image_divided = image_expanded / 255.

    #
    model_loaded = load_model(picked_model_path)

    #
    prediction = model_loaded.predict(image_divided)
    return prediction




#
def interpret_result(prediction):
    
    #
    interpretation = []

    #
    for value in prediction[0]:
        value_float = float(value) * 100
        value_round = round(value_float,2)
        interpretation.append(f"{value_round:.2f}")
    
    #
    prediction_class_index = int(np.argmax(prediction))
    interpretation.append(prediction_class_index)

    #
    return interpretation