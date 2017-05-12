from celery import Celery
from smtplib import SMTP
from email.mime.text import MIMEText as text
#import redis

celery = Celery('a', backend='amqp://localhost//',
                    broker='amqp://localhost//')
#celery = Celery('a', backend='redis://localhost//',
#                    broker='redis://localhost//')

@celery.task
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

    s.quit()
