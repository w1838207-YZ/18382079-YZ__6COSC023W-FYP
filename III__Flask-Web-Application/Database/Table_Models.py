#
from sqlalchemy import Column, Integer, String, DateTime, Double, ForeignKey

#
from datetime import datetime

#
from Database.Connection import app_database




#
class User(app_database.Model):
    
    #
    __tablename__ = "Users"
    
    #
    userID = Column(Integer,primary_key=True)
    userEmail = Column(String(35),unique=True,nullable=False)
    userPassword = Column(String(35),nullable=False)
    userFirstName = Column(String(50),nullable=False)
    userLastName = Column(String(50),nullable=False)
    userCreatedAt = Column(DateTime,default=datetime.now(),nullable=False)
    userLastLogged = Column(DateTime,nullable=True)
    
    #
    classifications = app_database.relationship("Classification",backref="user")
    
    #
    def __repr__(self):
        return f"A user named '{self.userFirstName} {self.userLastName}'"




#
class Classification(app_database.Model):
    
    #
    __tablename__ = "Classifications"
    
    #
    classifyID = Column(Integer,primary_key=True)
    predictedResult = Column(String(4),nullable=False)
    uploadedImage = Column(String(50),nullable=False)
    percentReal = Column(Double,nullable=False)
    percentFake = Column(Double,nullable=False)
    dateOfUpload = Column(DateTime,default=datetime.now(),nullable=False)
    dateToDelete = Column(DateTime,nullable=True)
    
    #
    userID = Column(Integer,ForeignKey("Users.userID"))
    
    #
    def __repr__(self):
        return f"A classification of '{self.predictedResult}' for the image '{self.uploadedImage}'"