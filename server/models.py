from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
# Edit server/models.py to add new model class named Earthquake that inherits from both db.Model and SerializerMixin
# Add the following attributes to the Earthquake model:

# a string named __tablename__ assigned to the value "earthquakes".
# a column named id to store an int that is the primary key.
# a column named magnitude to store a float.
# a column named location to store a string.
# A column named year to store an int.

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"
    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

# Add a __repr__ method to return a string that formats the attributes id, magnitude, location, and year as a comma-separated 
# string, e.g. 1, 9.5, Chile, 1960

    def __repr__(self):
        return f"{self.id}, {self.magnitude}, {self.location}, {self.year}"