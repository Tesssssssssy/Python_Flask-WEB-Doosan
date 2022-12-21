from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_login import login_required, current_user
from . import db 
from .models import User, Info
import os
import sqlite3
    
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
        
        if len(drink) < 2:
            flash('음주 정도를 선택하세요!.', category='error')
        elif len(sleephour) < 2:
            flash('수면 시간을 선택하세요!', category='error')
        elif len(sleepqual) < 2:
            flash('수면의 질을 선택하세요!.', category='error')
        elif len(tired) < 2:
            flash('피로도를 선택하세요!', category='error')
        elif len(anxiety) < 2:
            flash('불안감을 선택하세요!', category='error')
        elif len(gloom) < 2:
            flash('우울감을 선택하세요!', category='error')
        else:
            new_info = Info(
                drink=drink,
                sleephour=sleephour,
                sleepqual=sleepqual,
                tired=tired,
                anxiety=anxiety,
                gloom=gloom
                )
            db.session.add(new_info)
            db.session.commit()
            flash('오늘의 정보가 저장되었습니다!', category='success')
            return redirect(url_for('views.home'))
        
    return render_template('index.html', user=current_user)
