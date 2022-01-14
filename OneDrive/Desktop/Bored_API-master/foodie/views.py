from flask import Blueprint, render_template, redirect
from flask.helpers import url_for
from flask_login import  login_required, current_user
from werkzeug.wrappers import request
from flask import flash, request, jsonify
from .models import Activity, UserActivity
from . import db
import json
from flask import Flask, render_template, request
import requests, json
# app = Flask(__name__, static_url_path='/static')
 
types= ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]
views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        chosen = request.form.get("activity")
        print(chosen)
        url = 'http://www.boredapi.com/api/activity?type=' + str(chosen)
        Url = requests.get(url)
        data = json.loads(Url.content)
        print( data )
        activity = data['activity']
        type = data['type'] 
        participants = data['participants'] 
        price = data['price'] 
        link = data['link']
        new_activity = Activity(activity=activity, type=type, participants=participants, price = price, link=link)
        db.session.add(new_activity)
        db.session.commit()
    else:
        new_activity = None

            # return render_template('views.html', data=)
    
    return render_template('home.html', user=current_user, data=new_activity)

# @views.route('/saved', methods=['GET', 'POST'])
@views.route('/saved', methods=['GET', 'POST'])
@login_required
def saved():
    if 'aid' in request.args:
        aid = int( request.args.get('aid') )
        ua = UserActivity( uid = current_user.id, aid = aid )
        db.session.add( ua )
        db.session.commit()
    print("yippie")
    return render_template( 'saved.html', user=current_user, data= UserActivity.query.all() )

