#
import os

#
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

#
from keras._tf_keras.keras.utils import img_to_array

#
from keras._tf_keras.keras.models import load_model

#
import numpy as np




#
allowed_extensions = ["jpg","jpeg"]




#
def image_classification_prediction(model_path,upload_file):

    #
    image_resized = upload_file.resize((224,224))
    image_array = img_to_array(image_resized)
    image_expanded = np.expand_dims(image_array,axis=0)
    image_divided = image_expanded / 255.

    #
    model_loaded = load_model(model_path)
    prediction = model_loaded.predict(image_divided)
    
    #
    return prediction




#
def interpret_result(model_prediction):
    
    #
    interpretation = []

    #
    for value in model_prediction[0]:
        value_float = float(value) * 100
        value_round = round(value_float,2)
        interpretation.append(f"{value_round:.2f}")
    
    #
    prediction_class_index = int(np.argmax(model_prediction))
    if (prediction_class_index==0):
        interpretation.append("Fake")
    elif (prediction_class_index==1):
        interpretation.append("Real")

    #
    return interpretation




#
def make_context_for_prediction(upload_name,model_paths_picked,upload_file):
    
    #
    template_context = {}
    
    #
    prediction_outcomes = []
    
    #
    for model_path in model_paths_picked:
        individual_result = {}
        individual_result["model"] = str(model_path).split("\\")[-1]
        individual_result["model"] = individual_result["model"].replace(".keras","")
        model_prediction = image_classification_prediction(model_path,upload_file)
        individual_result["result"] = interpret_result(model_prediction)
        prediction_outcomes.append(individual_result)
    
    #
    template_context["upload_name"] = upload_name
    template_context["prediction_outcomes"] = prediction_outcomes
    
    #
    return template_context