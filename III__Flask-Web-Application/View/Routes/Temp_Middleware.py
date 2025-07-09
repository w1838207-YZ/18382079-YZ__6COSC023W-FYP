#
from flask import session

#
import os




#
def delete_temp_image_data():
    
    #
    app_sub_directory_base = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    
    #
    temp_img_subdir_path = os.path.join(app_sub_directory_base,"Static","TMP")
    
    #
    if (session.get("data_to_prediction_page")):
        session["data_to_prediction_page"] = None
    
    #
    for temporary_image in os.scandir(temp_img_subdir_path):
        if (temporary_image.is_file()):
            os.remove(temporary_image.path)