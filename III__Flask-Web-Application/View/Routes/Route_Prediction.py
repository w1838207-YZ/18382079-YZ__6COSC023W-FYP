#
from flask import render_template, flash, redirect, request, session

#
from PIL import Image

#
from io import BytesIO

#
import base64

#
from datetime import datetime, timedelta

#
import os

#
import shutil

#
from Database.Create_DB import db as app_database

#
from Database.Table_Models import Classification

#
from View.Supports import Support_Prediction




#
def unsigned_prediction_page():
    
    #
    if (request.method=="GET"):
        
        #
        if not(session.get("data_to_prediction_page")):
            flash("> Error! lost data, must reupload again","error")
            return redirect("/")
        
        #
        data_to_prediction_page = session["data_to_prediction_page"]
        
        #
        upload_name = data_to_prediction_page["upload_name"]
        model_paths_picked = data_to_prediction_page["model_paths_picked"]
        path_of_temporary_file = data_to_prediction_page["path_of_temporary_file"]
        upload_file = Image.open(path_of_temporary_file)
        
        #
        template_context = Support_Prediction.make_context_for_prediction(upload_name,model_paths_picked,upload_file)
        
        #
        with BytesIO() as image_buffer:
            upload_file.save(image_buffer,"jpeg")
            image_bytes = image_buffer.getvalue()
        image_encoded_string = base64.b64encode(image_bytes).decode()
        upload_file.close()
        
        #
        flash("> prediction here","success")
        return render_template("Unsigned/Index/Prediction.html",template_context=template_context,image_encoded_string=image_encoded_string)




#
def signed_prediction_page(signed_user):
    
    #
    if (request.method=="GET"):
        
        #
        if not(session.get("data_to_prediction_page")):
            flash("> Error! lost data, must reupload again","error")
            return redirect("/")
        
        #
        data_to_prediction_page = session["data_to_prediction_page"]
        
        #
        upload_name = data_to_prediction_page["upload_name"]
        model_paths_picked = data_to_prediction_page["model_paths_picked"]
        path_of_temporary_file = data_to_prediction_page["path_of_temporary_file"]
        upload_file = Image.open(path_of_temporary_file)
        
        #
        template_context = Support_Prediction.make_context_for_prediction(upload_name,model_paths_picked,upload_file)
        
        #
        with BytesIO() as image_buffer:
            upload_file.save(image_buffer,"jpeg")
            image_bytes = image_buffer.getvalue()
        image_encoded_string = base64.b64encode(image_bytes).decode()
        upload_file.close()
        
        #
        name_offset = str(path_of_temporary_file).split("\\")[-1]
        name_offset = name_offset.replace(upload_name,"")
        
        #
        flash("> prediction here","success")
        return render_template("Signed/Index/Prediction.html",template_context=template_context,image_encoded_string=image_encoded_string,name_offset=name_offset)
    
    #
    elif (request.method=="POST"):
        
        #
        if ("no" in request.form):
            flash("Haven't saved to DB","success")
            return redirect("/")
        
        #
        elif ("yes" in request.form):
            
            #
            hidden_offset_upload_name = request.form.get("hidden_offset_upload_name")
            hidden_model_count_picked = int(request.form.get("hidden_model_count_picked"))
            
            #
            app_sub_directory_base = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
            path_to_temporary_file = os.path.join(app_sub_directory_base,"Static","TMP",hidden_offset_upload_name)
            path_for_saved_image = os.path.join(app_sub_directory_base,"Static","IMG",hidden_offset_upload_name)
            
            #
            duration = request.form.get("duration")
            if (not(duration)):
                flash("No selected save duration","error")
                return redirect("/")
            
            #
            date_of_upload = datetime.now()
            
            #
            match duration:
                case "Save for 1 day":
                    date_to_delete_by = date_of_upload + timedelta(days=1)
                case "Save for 1 week":
                    date_to_delete_by = date_of_upload + timedelta(days=7)
                case "Save for 2 weeks":
                    date_to_delete_by = date_of_upload + timedelta(days=14)
                case "Save for 1 month":
                    date_to_delete_by = date_of_upload + timedelta(days=31)
            
            #
            try:
                for x in range(hidden_model_count_picked):
                    get_string_for_model = f"table_model_{x}"
                    get_string_for_result = f"table_result_{x}"
                    get_string_for_percent = f"table_percent_{x}"
                    table_model = request.form.get(get_string_for_model)
                    table_result = request.form.get(get_string_for_result)
                    table_percent = float(request.form.get(get_string_for_percent))
                    percent_remainder = 100.00 - table_percent
                    if (table_result=="Fake"):
                        new_classification = Classification(predictedResult=table_result,uploadedImage=hidden_offset_upload_name,modelUsed=table_model,percentFake=table_percent,percentReal=percent_remainder,dateOfUpload=date_of_upload,dateToDelete=date_to_delete_by,userID=int(signed_user["id"]))
                    elif (table_result=="Real"):
                        new_classification = Classification(predictedResult=table_result,uploadedImage=hidden_offset_upload_name,modelUsed=table_model,percentFake=percent_remainder,percentReal=table_percent,dateOfUpload=date_of_upload,dateToDelete=date_to_delete_by,userID=int(signed_user["id"]))
                    app_database.session.add(new_classification)
                    app_database.session.commit()
                if not(os.path.exists(path_for_saved_image)):
                    shutil.copy(path_to_temporary_file,path_for_saved_image)
                os.remove(path_to_temporary_file)
                flash("Feel like an idiot","success")
                
            #
            except Exception as error:
                print("Here is my problem:  ",error)
                flash("Failed to save prediction(s)","error")
            
            #
            finally:
                return redirect("/")

        #
        else:
            flash("No save decision made","error")
            return redirect("/")