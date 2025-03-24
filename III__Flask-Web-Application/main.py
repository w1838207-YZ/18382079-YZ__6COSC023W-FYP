# The Python library 'OS' gets imported.
# It is needed so environment variables can be set to configure the below web app.
import os

# Here is where one environment variable is set.
# It suppresses TensorFlow logs, so information and warnings do not get displayed.
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# Several imports are made from the Python Flask framework.
# The class 'Flask' allows for the creation of web apps, as objects of said class.
# The function 'render_template()' lets page templates be rendered on the screen.
# The object 'request' enables access to data that a client sends to the server.
# The function 'flash()' lets messages be shown on- screen for visual feedback.
# The function 'redirect()' allows for users to be automatically sent to URLs.
from flask import Flask, render_template, request, flash, redirect

# The function 'secure_filename()', from the library 'Werkzeug', get imported.
# It sanitizes uploaded file names, avoiding harm to a server's filesystem.
from werkzeug.utils import secure_filename

# All contents, from the static file 'Support_Index.py', get imported.
# This script contains functions which are used by the 'index' route function.
from Static.PY.Support_Index import *

# The Python library 'Secrets' gets imported.
# A specific function, '.token_hex()', can generate random hexadecimal characters.
import secrets




# An instance of the Flask class is created.
# It represents my web application for Deepfake Detection.
app = Flask(__name__)

# The web app is given a secret key, made of 16 random hexadecimal characters.
# It allows, for example, message flashing to be possible.
app.config["SECRET_KEY"] = secrets.token_hex(16)




# This is a route decorator, for the home / index / landing page of the web app.
# The route can answer to HTTP 'Get' and 'Post' requests.
@app.route("/", methods=["GET","POST"])
def index_page():

    # A called function finds available classification models.
    # A count of these models is stored into a separate variable.
    model_paths = find_currently_available_models()
    model_count = len(model_paths)

    # The names of the found models are taken, and stored into a separate list.
    # This will be useful for a dropdown list in a form on the index page.
    model_names = []
    for path in model_paths:
        name = str(path).split("\\")[-1]
        model_names.append(name)

    # This if statement checks any request for whether it is a HTTP Get request.
    # If so, the page where users upload images to classify is rendered.
    if (request.method=="GET"):
        return render_template("Unsigned/Index/Upload.html",model_count=model_count,model_names=model_names)
    
    # This else clause checks any request for whether it is a HTTP Post request.
    # If so, a series of operations make/display a predicted image classification.
    elif (request.method=="POST"):
        # An error message flashes if a request does not have a 'file' part.
        if ("image" not in request.files):
            flash(">\tA! Error! A 'file' attribute was not found in the body of your request.","error")
            return redirect(request.url)
        # An error message flashes if a user does not upload a file to predict on.
        uploaded_file = request.files["image"]
        if (uploaded_file.filename==""):
            flash(">\tB! Error! No image file was uploaded on the previous HTML form for deepfake detection.","error")
            return redirect(request.url)
        # An error message flashes if a user picks no model to predict with.
        picked_model = request.form.get("model")
        if (not(picked_model)):
            flash(">\tC! Error! No model file was selected on the previous HTML form for deepfake detection.","error")
            return redirect(request.url)
        # An error message flashes if a user uploads a file of a disallowed type.
        uploaded_file_name = secure_filename(uploaded_file.filename)
        if (not(is_file_allowed(uploaded_file_name))):
            flash(">\tD! Error! The uploaded file is not a compatible extension (either '.jpg' or '.jpeg').","error")
            return redirect(request.url)
        # The file path to a selected model is stored into a variable.
        for path in model_paths:
            if (picked_model in path):
                picked_model_path = path
        # A variable stores an image classification, formed by a called function.
        prediction = image_classification_prediction(uploaded_file,picked_model_path)
        # A variable stores a result's interpretation, made by a called function.
        interpretation = interpret_result(prediction)
        # The page where users see results is rendered, with a success message.
        flash(">\tYes! Your previous HTML form for deepfake detection was sent successfully.","success")
        return render_template("Unsigned/Index/Prediction.html",interpretation=interpretation)




# This is a route decorator, for the login page of the web app.
# The route only by default handles HTTP 'Get' requests.
@app.route("/login")
def login_page():
    # The page where users log into the web application is rendered.
    return render_template("Unsigned/Login.html")




# This is a route decorator, for the register page of the web app.
# The route only by default handles HTTP 'Get' requests.
@app.route("/register")
def register_page():
    # The page where users register for a new account on the web app is rendered.
    return render_template("Unsigned/Register.html")