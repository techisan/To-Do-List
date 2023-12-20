from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import ToDos
import json
from sqlalchemy.sql import func

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST']) # Main page of the website
@login_required
def home():
    if request.method == 'POST':
        item = request.form.get('todo')

        if len(item) < 1:
            flash('Note is too short!', category='error')
        else:
            new_item = ToDos(data=item, user_id=current_user.id)
            db.session.add(new_item)
            db.session.commit()
            flash('Item added!', category='success')
    return render_template("home.html", user = current_user)


@views.route('/edit-item', methods=['POST'])
def edit_item():
    todo_id = request.form.get('noteId')
    todo_object = ToDos.query.get(todo_id)
    
    if todo_object:
        item = request.form.get('txtEdit')
        if len(item) < 1:
            flash('Item is too short!', category='error')
        else:
            todo_object.data = item
            db.session.commit()
            flash('Note Edited!', category='success')
    return jsonify({})


@views.route('/delete-item', methods=['POST'])
def delete_item():
    item = json.loads(request.data)
    itemId = item['itemId']
    item = ToDos.query.get(itemId)
    if item:
        if item.user_id == current_user.id:
            db.session.delete(item)
            db.session.commit()
    return jsonify({})

@views.route('/complete-item', methods=['POST'])
def complete_item():
    todo_id = request.form.get('todoId')
    todo_object = ToDos.query.get(todo_id)
    
    if todo_object:
        completed = request.form.get('completeBtn')
        if completed == "Completed":
            todo_object.completed = True
            todo_object.date = func.now()
            db.session.commit()
            flash('Item Completed!', category='success')
    return jsonify({})