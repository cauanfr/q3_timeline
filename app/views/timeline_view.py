from flask import Blueprint, render_template
from data.posts import time_points


bp_timeline = Blueprint('bp_timeline', __name__)


@bp_timeline.route('/')
def timeline():
    return render_template('timeline.html', time_points=time_points)
