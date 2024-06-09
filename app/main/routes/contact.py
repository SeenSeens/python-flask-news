from flask import render_template, request, redirect, url_for, flash
from app.main import main
from app.email import send_email

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method.__eq__('POST'):
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_email('New Contact Form Submission', 'truongtuan829@gmail.com', f'From: {name}\n\n{email}\n\n{phone}\n\n{message}')
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('main.contact'))
    return render_template('main/contact.html')
