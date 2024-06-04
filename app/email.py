from flask_mail import Message
from app import mail, app

def send_email(subject, recipient, body):
    msg = Message(subject, recipients=[recipient])
    msg.body = body
    with app.app_context():
        mail.send(msg)