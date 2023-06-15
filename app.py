from flask import Flask, render_template, flash, redirect, render_template, url_for, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.debug = True
toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


##########################################################################


@app.route('/')
def home():
    """Home page. Lists all pets"""
    pets = Pet.query.all()
    
    return render_template('pets_list.html', petss=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """For adding a pet to the list."""

    form = AddPetForm()

    if form.validate_on_submit():
        info = {k: v for k, v in form.data.items() if k != "csrf_token"}
        pet = Pet(**info)
        
        db.session.add(pet)
        db.session.commit()
        
        flash(f'{pet.name} has been added!')
        return redirect(url_for('home'))

    else:
        return render_template('add_pet_form.html', form=form)
    
    
@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """For editing a pet."""
    
    pet = Pet.query.get_or_404(pet_id)
    form = form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.commit()
        flash(f'{pet.name} has been updated!')
        return redirect(url_for('home'))
    
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)
    

