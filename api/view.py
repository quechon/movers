from flask import Blueprint
from movers.form import ReviewForm

api = Blueprint('api', __name__)

@api.route('/review', methods=['POST'])
def review():

    form = ReviewForm()

    if form.validate_on_submit():
        pass
