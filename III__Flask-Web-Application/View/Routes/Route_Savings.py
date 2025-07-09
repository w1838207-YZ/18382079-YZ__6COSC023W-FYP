#
from flask import render_template, request

#
from Database.Table_Models import Classification

#
from View.Routes import Temp_Middleware




#
def all_savings_page(signed_user):
    
    #
    every_saving_from_user = Classification.query.filter_by(userID=signed_user["id"]).all()
    
    #
    if (request.method=="GET"):
        Temp_Middleware.delete_temp_image_data()
        return render_template("Signed/Savings/All.html",every_saving_from_user=every_saving_from_user)