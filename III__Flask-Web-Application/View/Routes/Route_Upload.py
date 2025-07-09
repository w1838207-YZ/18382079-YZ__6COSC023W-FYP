#
from flask import render_template, flash, redirect, request, session

#
from werkzeug.utils import secure_filename

#
import os

#
from View.Supports import Support_Upload

#
from View.Routes import Temp_Middleware




#
def unsigned_upload_page():

    #
    model_paths_available = Support_Upload.find_currently_available_models()
    model_count_available = len(model_paths_available)

    #
    model_names_available = []
    for path in model_paths_available:
        name = str(path).split("\\")[-1]
        model_names_available.append(name)
    
    #
    if (request.method=="GET"):
        Temp_Middleware.delete_temp_image_data()
        return render_template("Unsigned/Index/Upload.html",model_count_available=model_count_available,model_names_available=model_names_available)
    
    #
    elif (request.method=="POST"):
        
        #
        data_to_prediction_page = {}
        model_paths_picked = []
        
        #
        if ("image" not in request.files):
            flash("Error! In order to submit this form, you need to pick a human JPG/JPEG image and a CNN model to classify with.","error")
            return redirect(request.url)
        
        #
        upload_file = request.files["image"]
        if (upload_file.filename==""):
            flash("Error! In order to submit this form, you need to pick a human JPG/JPEG image and a CNN model to classify with.","error")
            return redirect(request.url)
        
        #
        upload_name = secure_filename(upload_file.filename)
        if (not(Support_Upload.is_file_allowed(upload_name))):
            flash("Error! In order to submit this form, you need to pick a human JPG/JPEG image and a CNN model to classify with.","error")
            return redirect(request.url)
        
        #
        picked_model = request.form.get("model")
        if (not(picked_model)):
            flash("Error! In order to submit this form, you need to pick a human JPG/JPEG image and a CNN model to classify with.","error")
            return redirect(request.url)
        
        #
        if (picked_model == "All"):
            for path in model_paths_available:
                model_paths_picked.append(path)
        
        #
        else:
            for path in model_paths_available:
                if (picked_model in path):
                    model_paths_picked.append(path)
        
        #
        temp_upload_name = upload_name
        app_sub_directory_base = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        path_of_temporary_file = os.path.join(app_sub_directory_base,"Static","TMP",temp_upload_name)
        
        #
        while (os.path.exists(path_of_temporary_file)):
            temp_upload_name = "_" + temp_upload_name
            path_of_temporary_file = os.path.join(app_sub_directory_base,"Static","TMP",temp_upload_name)
        upload_file.save(path_of_temporary_file)
        
        #
        data_to_prediction_page["path_of_temporary_file"] = path_of_temporary_file
        data_to_prediction_page["upload_name"] = upload_name
        data_to_prediction_page["model_paths_picked"] = model_paths_picked
        
        #
        session["data_to_prediction_page"] = data_to_prediction_page
        return redirect("/prediction")




#
def signed_upload_page(signed_user):
    
    #
    model_paths_available = Support_Upload.find_currently_available_models()
    model_count_available = len(model_paths_available)

    #
    model_names_available = []
    for path in model_paths_available:
        name = str(path).split("\\")[-1]
        model_names_available.append(name)
    
    #
    if (request.method=="GET"):
        Temp_Middleware.delete_temp_image_data()
        return render_template("Signed/Index/Upload.html",model_count_available=model_count_available,model_names_available=model_names_available,signed_user=signed_user)
    
    #
    elif (request.method=="POST"):
        
        #
        data_to_prediction_page = {}
        model_paths_picked = []
        
        #
        if ("image" not in request.files):
            flash("Error! In order to submit this form, you need to pick a human JPG/JPEG image and a CNN model to classify with.","error")
            return redirect(request.url)
        
        #
        upload_file = request.files["image"]
        if (upload_file.filename==""):
            flash("Error! In order to submit this form, you need to pick a human JPG/JPEG image and a CNN model to classify with.","error")
            return redirect(request.url)
        
        #
        upload_name = secure_filename(upload_file.filename)
        if (not(Support_Upload.is_file_allowed(upload_name))):
            flash("Error! In order to submit this form, you need to pick a human JPG/JPEG image and a CNN model to classify with.","error")
            return redirect(request.url)
        
        #
        picked_model = request.form.get("model")
        if (not(picked_model)):
            flash("Error! In order to submit this form, you need to pick a human JPG/JPEG image and a CNN model to classify with.","error")
            return redirect(request.url)
        
        #
        if (picked_model == "All"):
            for path in model_paths_available:
                model_paths_picked.append(path)
        
        #
        else:
            for path in model_paths_available:
                if (picked_model in path):
                    model_paths_picked.append(path)
        
        #
        temp_upload_name = upload_name
        app_sub_directory_base = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        path_of_temporary_file = os.path.join(app_sub_directory_base,"Static","TMP",upload_name)
        
        #
        while (os.path.exists(path_of_temporary_file)):
            temp_upload_name = "_" + temp_upload_name
            path_of_temporary_file = os.path.join(app_sub_directory_base,"Static","TMP",temp_upload_name)
        upload_file.save(path_of_temporary_file)
        
        #
        data_to_prediction_page["path_of_temporary_file"] = path_of_temporary_file
        data_to_prediction_page["upload_name"] = upload_name
        data_to_prediction_page["model_paths_picked"] = model_paths_picked
        
        #
        session["data_to_prediction_page"] = data_to_prediction_page
        return redirect("/prediction")