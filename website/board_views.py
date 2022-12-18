from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from .models import Post, Comment
from . import db
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql
import os
from werkzeug.utils import secure_filename

board_views = Blueprint('board_views', __name__)

@board_views.route('/board', methods=['GET', 'POST'])
def board():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from posts")
    
    rows = cur.fetchall()
    return render_template("board.html", rows=rows)
    

@board_views.route('/posts/new')
def new():
    return render_template('board_new.html')

@board_views.route('/posts/create', methods=["POST"])
def create():
    if request.method == 'POST':
        # title = request.args.get('title')
        title = request.form.get('title')
        # content = request.args.get('content')
        content = request.form.get('content')
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
    
        # return render_template('create.html')
        return redirect('/posts/{}'.format(post.id))
    return render_template('board_create.html')
    
@board_views.route('/posts/<int:id>')
def read(id):
    post = Post.query.get(id)
    # SELECT * FROM posts WHERE id=1;
    return render_template('board_read.html',post=post)
    
@board_views.route('/posts/<int:id>/delete', methods=['POST']) 
def delete(id):
    if request.method == 'POST':
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        
        return redirect('/board')
    return render_template('board_delete.html', post=post)
    
@board_views.route('/posts/<int:id>/edit')
def edit(id):
    post = Post.query.get(id)
    return render_template('board_edit.html',post=post)
    
@board_views.route('/posts/<int:id>/update', methods=["POST"])
def update(id):
    post = Post.query.get(id)
    post.title = request.form.get('title')
    post.content = request.form.get('content')
    # post.title = request.args.get('title')
    # post.content = request.args.get('content')
    db.session.commit()
    
    return redirect('/posts/{}'.format(id))
    
@board_views.route('/posts/<int:post_id>/comments',methods=['POST'])
def comments(post_id):
    content = request.form.get('content')
    creator = request.form.get('creator')
    comment = Comment(content,creator)
    post = Post.query.get(post_id)
    post.comments.append(comment)
    db.session.add(comment)
    db.session.commit()
    
    return redirect('/board')
    
@board_views.route('/comment/<int:id>/delete')
def comment_delete(id):
    comment = Comment.query.get(id)
    db.session.delete(comment)
    db.session.commit()
    
    return redirect('/board')
