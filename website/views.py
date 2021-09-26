from flask import Blueprint, render_template, redirect
from flask.helpers import url_for
from flask_login import  login_required, current_user
from werkzeug.wrappers import request
from flask import flash, request, jsonify
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        # return redirect(url_for('home.html'))
        note = request.form.get('note')
        Title = request.form.get('title')
        if len(note) < 1:
            flash('Note is too short', category='error')

        else:
            new_note = Note(title=Title, data=note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
            # return render_template('views.html', data=)
    return render_template('home.html', user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})   

# @views.route('/add-to-entry', methods=['POST'])
# def add_to_Entry():
#     noteD = json.loads(request.data)
#     noteData = noteD['noteData']
#     noteD = Note.query.get(noteData)
#     if noteD:
#         if note.
