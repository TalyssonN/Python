from flask import Blueprint, render_template

homepage = Blueprint('home', __name__)

@homepage.route('/')
def home():
    return render_template('site.html')
