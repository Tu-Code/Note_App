from flask import request, Blueprint,  redirect
from flask.json import jsonify
from .models import UserActivity
from . import db
from flask_login import current_user
from flask.helpers import url_for
import json

controllers = Blueprint('controllers', __name__)

@controllers.route('/delete-note/<int:id>', methods=[ 'DELETE' ])
def delete_note(id):
    activity = json.loads( request.data )
      #data = Data.query.get( ' id' )
      #wo zai shi bu an quan
    print(activity)
    activity_id = activity[ 'activity_id' ]
    activity = UserActivity.query.get( activity_id )

    if activity:
        if activity.uid == current_user.id:
            db.session.delete( activity )
            db.session.commit()
    return jsonify({"status": True})