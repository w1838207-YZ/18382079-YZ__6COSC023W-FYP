#
#
from flask import render_template, request, flash, redirect

#
#
from werkzeug.utils import secure_filename

#
#
from PIL import Image

#
#
import base64

#
#
from io import BytesIO

#
#
from Static.PY import Support_Index




#
#
def make_context_for_prediction(model_paths_picked,uploaded_file):

    #
    template_context = []

    #
    for model in model_paths_picked:

        #
        context_piece = {}

        #
        context_piece["model_name"] = str(model).split("\\")[-1]

        #
        model_prediction = Support_Index.image_classification_prediction(model,uploaded_file)

        #
        context_piece["prediction_interpretation"] = Support_Index.interpret_result(model_prediction)

        #
        template_context.append(context_piece)

    #
    return template_context




#
#
def index_page():

    #
    model_paths_available = Support_Index.find_currently_available_models()
    model_count_available = len(model_paths_available)

    #
    model_names_available = []
    for path in model_paths_available:
        name = str(path).split("\\")[-1]
        model_names_available.append(name)
    
    #
    if (request.method=="GET"):

        #
        return render_template("Unsigned/Index/Upload.html",model_count_available=model_count_available,model_names_available=model_names_available)
    
    #
    elif (request.method=="POST"):

        #
        if ("image" not in request.files):
            flash(">","error")
            return redirect(request.url)
        
        #
        uploaded_file = request.files["image"]
        if (uploaded_file.filename==""):
            flash(">","error")
            return redirect(request.url)
        
        #
        uploaded_file_name = secure_filename(uploaded_file.filename)
        if (not(Support_Index.is_file_allowed(uploaded_file_name))):
            flash(">","error")
            return redirect(request.url)
        
        #
        picked_model = request.form.get("model")
        if (not(picked_model)):
            flash(">","error")
            return redirect(request.url)
        
        #
        model_paths_picked = []
        
        #
        if (picked_model == "All"):

            #
            for path in model_paths_available:
                model_paths_picked.append(path)
        
        #
        else:

            #
            for path in model_paths_available:
                if (picked_model in path):
                    model_paths_picked.append(path)
        
        #
        template_context = make_context_for_prediction(model_paths_picked,uploaded_file)
        
        #
        image_open = Image.open(uploaded_file.stream)
        with BytesIO() as image_buffer:
            image_open.save(image_buffer,"jpeg")
            image_bytes = image_buffer.getvalue()
        image_encoded_string = base64.b64encode(image_bytes).decode()
        
        #
        flash(">","success")
        return render_template("Unsigned/Index/Prediction.html",context=template_context,model_count_picked=len(template_context),image_data=image_encoded_string,hide=uploaded_file)