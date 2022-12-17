from flask import Blueprint, redirect, render_template, request, flash, url_for, jsonify
from flask_login import login_required, current_user
from .models import User
from . import db
import sqlite3
import os
from werkzeug.utils import secure_filename

mypage_views = Blueprint('mypage_views', __name__)

# 나의 정보 페이지
@mypage_views.route('/mypage', methods=['GET','POST'])
@login_required
def mypage():
    return render_template('mypage.html')


# 나의 정보 수정 페이지
@mypage_views.route('/mypage/update', methods=['GET','POST'])
@login_required
def mypage_update():
      # 나의 정보 수정 요청 확인
    if request.method == 'POST':
        changed = False # 변경 여부가 있는 지 확인
        
        # 네임, 비밀번호 변경여부 확인
        auth = request.form.get('auth')
        name = request.form.get('name')
        password = request.form.get('password')
        age = request.form.get('age')
        weight = request.form.get('weight')
        gender = request.form.get('gender')
        graduation = request.form.get('graduation')
        hearing = request.form.get('hearing')
        sight = request.form.get('sight')
        
        # 직급 입력 여부 및 유효성 검사
        if auth:
            db_user = User.query.filter_by(auth=auth).first()
            if len(auth) < 2:
                flash("직급을 선택해주세요.", category="error")
                return redirect(request.url)
            else:
                user = User.query.get(current_user.id)
                user.auth = auth
                db.session.commit()
                changed = True
        
        # 닉네임 입력 여부 및 유효성 검사
        if name:
            db_user = User.query.filter_by(name=name).first()
            if len(name) < 2:
                flash("성명은 1글자 이상이어야 합니다.", category="error")
                return redirect(request.url)
            else:
                user = User.query.get(current_user.id)
                user.name = name
                db.session.commit()
                changed = True

         # 패스워드 입력 여부 및 유효성 검사
        if password:
            db_user = User.query.filter_by(password=password).first()
            if len(password) < 6:
                flash("비밀번호가 너무 짧습니다.", category = "error")
                return redirect(request.url)
            else:
                user = User.query.get(current_user.id)
                user.password = password
                db.session.commit()
                changed = True
                
        if age:
            db_user = User.query.filter_by(age=age).first()
            if age == "":
                flash("연령을 입력해주세요.", category = "error")
                return redirect(request.url)
            else:
                user = User.query.get(current_user.id)
                user.age = age
                db.session.commit()
                changed = True
                
        if weight:
            db_user = User.query.filter_by(weight=weight).first()
            if weight == "":
                flash("체중을 입력해주세요", category = "error")
                return redirect(request.url)
            else:
                user = User.query.get(current_user.id)
                user.weight = weight
                db.session.commit()
                changed = True
                
        if gender:
            db_user = User.query.filter_by(gender=gender).first()
            if len(gender) < 1:
                flash("성별을 선택해주세요.", category = "error")
                return redirect(request.url)
            else:
                user = User.query.get(current_user.id)
                user.gender = gender
                db.session.commit()
                changed = True
                
        if graduation:
            db_user = User.query.filter_by(graduation=graduation).first()
            if len(graduation) < 2:
                flash("최종학력을 입력해주세요.", category = "error")
                return redirect(request.url)
            else:
                user = User.query.get(current_user.id)
                user.graduation = graduation
                db.session.commit()
                changed = True
        
        if hearing:
            db_user = User.query.filter_by(hearing=hearing).first()
            if len(hearing) < 2:
                flash("청력 상태를 입력해주세요.", category = "error")
                return redirect(request.url)
            else:
                user = User.query.get(current_user.id)
                user.hearing = hearing
                db.session.commit()
                changed = True
                
        if sight:
            db_user = User.query.filter_by(sight=sight).first()
            if len(sight) < 3:
                flash("시력 상태를 입력해주세요", category = "error")
                return redirect(request.url)
            else:
                user = User.query.get(current_user.id)
                user.sight = sight
                db.session.commit()
                changed = True
        
        

        # 변경사항이 있다면 redirect
        if changed:
            flash('개인정보가 변경 되었습니다', category = "success")
            return redirect(url_for('mypage_views.mypage'))
        else :
            flash('변경 사항이 없습니다.', category = "error")
            return redirect(request.url)

    return render_template('mypage_update.html')