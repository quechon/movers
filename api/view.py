from flask import Blueprint, request, jsonify
from movers.form import ReviewForm
from flask_mail import Message
from movers.app import mail



api = Blueprint('api', __name__)

@api.route('/mail', methods=['POST'])
def review():

    form = ReviewForm()

    if form.validate_on_submit():

        msg = Message('Message from movers', sender='el.quechon2@gmail.com',
                                            recipients=[request.form['email']])
        msg.body = request.form['message']
        msg.html = '<p>' + request.form['message'] + '<p>'

        mail.send(msg)

        return jsonify({'message': 'success'})
    return jsonify({'message': 'error'})
