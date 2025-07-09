#
from flask import render_template, request, session

#
from sqlalchemy import and_

#
import os

#
from PIL import Image

#
from io import BytesIO

#
import base64

#
from Run_App import app

#
from Database.Table_Models import Classification

#
from View.Routes import Temp_Middleware




#
def single_saving_page(savingID):
    
    #    
    single_saving_from_user = Classification.query.filter_by(classifyID=savingID).first()
    
    #
    path_to_saved_image = os.path.join(app.config["UPLOAD_FOLDER"],single_saving_from_user.uploadedImage)
    opened_image = Image.open(path_to_saved_image)
    
    #
    with BytesIO() as image_buffer:
        opened_image.save(image_buffer,"jpeg")
        image_bytes = image_buffer.getvalue()
    image_encoded_string = base64.b64encode(image_bytes).decode()
    opened_image.close()
    
    #
    if (request.method=="GET"):
        Temp_Middleware.delete_temp_image_data()
        return render_template("Signed/Savings/Single.html",single_saving_from_user=single_saving_from_user,image_encoded_string=image_encoded_string)