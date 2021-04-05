from flask import Blueprint, render_template


bp_timeline = Blueprint('bp_timeline', __name__)

@bp_timeline.route('/pote3q')
def timeline():
    return render_template('index.html')