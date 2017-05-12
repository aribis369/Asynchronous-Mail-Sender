from smtplib import SMTP
from email.mime.text import MIMEText as text
from flask import Flask, redirect, url_for, request, render_template
import os
import json
from celery import Celery
#from mail import make_celery
from a import usermail


app = Flask(__name__)
#app.config['CELERY_BROKER_URL']='amqp://localhost//'
#app.config['CELERY_RESULT_BACKEND']='amqp://localhost:6379'

#celery = make_celery(app)
#celery = Celery(app.name, backend='amqp://localhost//',
#                    broker='amqp://localhost:6379')

@app.route('/mail', methods=['POST'])
def mail():
    form_data = request.form['msg']
    sender_name = request.form['name']
    sender_email = str(request.form['email'])
    #usermail.delay(sender_email, sender_name, form_data)
    usermail.delay(sender_email, sender_name, form_data)
    return ("sent",200,{'Access-Control-Allow-Origin':'*'})


'''@celery.task
def usermail(sender_mail, sender_name, msg):
    s = SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()

    s.login('dibyadasiscool@gmail.com', 'samsunghp')

    mu = text("Hi "+sender_name+",\n\n"+"Your message has been recieved by us and we will responded to it soon."+"\nThank-you for communicating with us, hope your query will cleared by our team."+"\n\n\nKOSS IIT Kharagpur")

    mu['Subject'] = "KOSS:query recieved will be responded soon"
    mu['From'] = 'dibyadasiscool@gmail.com'
    mu['To'] = "aribis369@gamil.com"

    mk = text("Query from "+sender_name+",\n\n"+msg+"\n\nRespond to the email-id below:\n"+sender_mail)

    mk['Subject'] = "Query"
    mk['From'] = 'dibyadasiscool@gmail.com'
    mk['To'] = "aribis369@gamil.com"

    try:
        s.sendmail('dibyadasiscool@gmail.com', "aribis369@gmail.com", mu.as_string())
        s.sendmail('dibyadasiscool@gmail.com', "aribis369@gmail.com", mk.as_string())
    except:
        print("email failed")

    s.quit()'''

if __name__ == "__main__":  # This is for local testing
    app.run(host='localhost', port=3453, debug=True)
