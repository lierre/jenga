from flask import render_template, Blueprint, request

from mailer import Mailer
from mailer import Message

from .extensions import mail

www = Blueprint('www', __name__, )


@www.route('/')
def index():
    return render_template('index.html')


# @www.route('/mail', methods=['POST'])
# def send_mail():
#     email = request.form['email']
#     message = request.form['message']
#     name = request.form['name']
#
#     msg = Message(From=email, To='bmwasaru@gmail.com')
#     msg.Subject = "Message from Jenga"
#     msg.Html = """
#         <p>Hi!</p>
#         This is %s wanted to say %s
#     """.format(name, message)
#     sender = Mailer('smtp.gmail.com')
#     sender.send(msg)
#
#     return render_template('thanks.html')
