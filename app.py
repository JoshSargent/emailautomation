# APP.PY
from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    confirmation_message = None
    confirmation_success = None

    if request.method == 'POST':
        email_sender = request.form['email_sender']
        email_receivers = [email.strip() for email in request.form['email_receiver'].split(',')]
        password = request.form['password']
        subject = request.form['subject']
        message = request.form['message']

        try:
            send_email(email_sender, email_receivers, password, subject, message)
            confirmation_message = "Email sent successfully!"
            confirmation_success = True
        except Exception as e:
            confirmation_message = f"Error sending email: {str(e)}"
            confirmation_success = False

    return render_template('index.html', confirmation_message=confirmation_message, confirmation_success=confirmation_success)

def send_email(email_sender, email_receivers, password, subject, message):
    text = f"Subject: {subject} \n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(email_sender, password)

    for email_receiver in email_receivers:
        server.sendmail(email_sender, email_receiver, text)
        print(f"Email has successfully been sent to {email_receiver} from {email_sender}.")

    server.quit()

if __name__ == '__main__':
    app.run(debug=False)
