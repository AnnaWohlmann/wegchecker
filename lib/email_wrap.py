import smtplib

sender = 'chireamihaela99@gmail.com'
password = "wuisclttjjbgeaur"
receivers = ['chireamihaela99@gmail.com']

# TODO: Change later
mailSubject = "Is it working?"
mailBody = "HIIIIIIIIIII"

def sendEmail(subject, body):
   message = """\
   TO: %s
   FROM: %s
   Subject: %s

   %s"""% (sender, ", ".join(receivers), subject, body)

   smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
   smtpObj.ehlo()
   smtpObj.starttls()
   smtpObj.login(sender, password)

   smtpObj.sendmail(sender, receivers, message)      
   smtpObj.quit()

   print("Successfully sent email")

# Check if it works
# sendEmail(mailSubject, mailBody)
