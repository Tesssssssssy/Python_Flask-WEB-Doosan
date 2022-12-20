from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Post
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from sqlalchemy import desc
from flask_login import login_user, login_required, logout_user, current_user
import pandas as pd

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('로그인 성공!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('비밀번호가 올바르지 않습니다. 다시 입력해주세요.', category='error')
        else:
            flash('이메일이 존재하지 않습니다.', category='error')
        
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('로그아웃되었습니다.', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        auth = request.form.get('auth')
        name = request.form.get('name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        age = request.form.get('age')
        weight = request.form.get('weight')
        gender = request.form.get('gender')
        graduation = request.form.get('graduation')
        hearing = request.form.get('hearing')
        sight = request.form.get('sight')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('이메일이 이미 존재합니다.', category='error')
        elif len(auth) < 2:
            flash('직급을 선택하세요.', category='error')
        elif len(email) < 4:
            flash('이메일이 4글자 이상이어야 합니다.', category='error')
        elif len(name) < 2:
            flash('성명이 2글자 이상이어야 합니다.', category='error')
        elif password1 != password2:
            flash('비밀번호가 일치하지 않습니다.', category='error')
        elif len(password1) < 6:
            flash('비밀번호가 6글자 이상이어야 합니다.', category='error')
        elif age == '':
            flash('연령을 입력해주세요', category='error')
        elif weight == '':
            flash('체중을 입력해주세요', category='error')
        elif len(gender) < 1:
            flash('성별을 선택해주세요', category='error')
        elif len(graduation) < 2:
            flash('최종학력을 선택해주세요', category='error')
        elif len(hearing) < 2:
            flash('청력 상태를 선택해주세요', category='error')
        elif len(sight) < 2:
            flash('시력 상태를 선택해주세요', category='error')
        else:
            new_user = User(
                auth=auth,
                name=name,
                email=email,
                password=generate_password_hash(password1, method='sha256'),
                age=age,
                weight=weight,
                gender=gender,
                graduation=graduation,
                hearing=hearing,
                sight=sight
                )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('축하합니다! 회원가입이 완료되었습니다.', category='success')
            return redirect(url_for('views.home'))
        
    return render_template("register.html", user=current_user)

@auth.route('/mypage')
@login_required
def mypage():
    return render_template("mypage.html")

@auth.route('/board', methods=['GET', 'POST'])
def board():
    posts = Post.query.order_by(desc(Post.created_at)).all()
    return render_template("board.html", posts=posts)

@auth.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    auth = current_user.auth
    if auth == "관리자":
        flash ("관리자로 접근 성공!", category='success')
        users = User.query.all() 
        
        return render_template("admin.html", users=users)
    else:
        flash("죄송합니다. 관리자만 접근할 수 있습니다.", category='error')
        return redirect(url_for('auth.login'))
    
    
    #업로드 파일 보기 
@auth.route('/admin_data', methods=['GET', 'POST'])
@login_required
def admin_data():
    if request.method == 'POST':
        file = request.form['upload-file']
        data = pd.read_excel(file)
        return render_template("admin_data.html", data=data.to_html())
        
    


