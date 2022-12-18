from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Post, Comment
from . import db
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os
from werkzeug.utils import secure_filename

board_views = Blueprint('board_views', __name__)

@board_views.route('/board')
def board():
    #myapp.db에 있는 모든 레코드를 불러와 보여준다.
    #SELECT*FROM posts;
    posts = Post.query.all()        #posts는 list type이다.
    comments = Comment.query.all()
    return render_template('board.html', posts = posts, comments = comments) 
    # reversed(posts) -> 글들 반대로 보이게 하는 것
    
@board_views.route('/create')
def create():
    title = request.args.get('title')
    content = request.args.get('content')
    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('board_views.board'))
    # return render_template('create.html', title=title, content=content) -> 이거말고 홈인 index.html로 돌아가게 하자
    
@board_views.route("/edit/<int:id>")
def edit(id):
    # 1. 수정하려고 하는 레코드를 선택하여
    post = Post.query.get(id)
    # 2. 수정을 하고
    # post.title = "수정하셈"
    # post.content = "수정하셈"
    # 3. 커밋한다.
    return render_template('board_edit.html', post=post)

@board_views.route("/update/<int:id>")
def update(id):
    # 1. 수정하려고 하는 레코드를 선택하여
    post = Post.query.get(id)
    # 2. 수정을 하고
    post.title = request.args.get('title')
    post.content = request.args.get('content')
    # 3. 커밋한다.
    db.session.commit()
    return redirect(url_for('board_views.board'))

@board_views.route("/delete/<int:id>")  #동적 변환 <> 사용
def delete(id): #id는 string으로 parse됨 int()이렇게 써도 되지만 위에 <int:id>로 한번에 써도됨
    #1. 지우려고 하는 레코드를 선택하여
    post = Post.query.get(id)    #()안에 해당 data primary
    #2. 지운다.
    db.session.delete(post)
    #3. 확정하고 DB에 반영한다. Commit
    db.session.commit()
    return redirect(url_for('board_views.board'))

@board_views.route("/create_comment")
def comment_content():
    #Comment 테이블에 입력받은 내용을 저장한다.
    content = request.args.get('comment_content') # /comment_content로 날라온 파라미터 잡기
    post_id = int(request.args.get('post_id')) 
    comment = Comment(content=content, post_id = post_id)
    #위에 코드까지 객체 생성을 통해 하나의 행을 만든 것
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('board_views.board')) 