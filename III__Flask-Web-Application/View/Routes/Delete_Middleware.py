#
from datetime import datetime

#
import os

#
from Database.Table_Models import Classification

#
from Database.Create_DB import db as app_database




#
def old_classification_record_deletion(app):
    
    #
    #folder_for_saved_images = app.config.get("UPLOAD_FOLDER")
    
    #
    current_stamp_datetime = datetime.now()
    
    #
    overdue_classification_records = Classification.query.filter(Classification.dateToDelete<current_stamp_datetime).all()
    
    #
    for record in overdue_classification_records:
        #os.remove(os.path.join(os.path.abspath(folder_for_saved_images),record.uploadedImage))
        app_database.session.delete(record)
    app_database.session.commit()
    
    #
    print(" * The overdue classification records have been successfully deleted!")