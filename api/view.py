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
                                            recipients=['el.quechon@gmail.com'])
        msg.body = request.form['message'] + ' ' + request.form['email']
        msg.html = '<p>' + request.form['message'] + ' ' + request.form['email'] + '<p>'

        mail.send(msg)

        return jsonify({'message': 'success'})
    return jsonify({'message': 'error'})
