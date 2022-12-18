from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        drink = request.form.get('drink')
        sleephour = request.form.get('sleephour')
        sleepqual = request.form.get('sleepqual')
        tired = request.form.get('tired')
        anxiety = request.form.get('anxiety')
        gloom = request.form.get('gloom')
        
        
    
    
    return render_template('index.html', user=current_user)
