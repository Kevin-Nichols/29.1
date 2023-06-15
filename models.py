from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

default_photo = 'https://media.istockphoto.com/id/1193052429/vector/photo-coming-soon-image-icon-vector-illustration-isolated-on-white-background-no-website.jpg?s=612x612&w=0&k=20&c=_FCj_ZJe1VdvwfUUGgdJqJSnGlTDWG6vsIMLczcSg1s='

def connect_db(app):
    db.app = app
    db.init_app(app)
    app.app_context().push()
    
    
class Pet(db.Model):
    """Pet for adoption."""
    __tablename__ = 'pets'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, 
                          nullable=False, 
                          default=True)
    
    def pet_photo(self):
        """Returns photo of pet"""
        return self.photo_url or default_photo