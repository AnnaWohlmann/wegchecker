import smtplib

sender = 'chireamihaela99@gmail.com'
password = "wuisclttjjbgeaur"
receivers = ['chireamihaela99@gmail.com']

mailSubject = "Wegchecker reporting issues"

def fillInEmailBody(nUsers, issueTag, location):
   mailBody = ''
   with open('email.txt', 'r') as file:
      mailBody = file.read()

   return mailBody.format(nr_users=nUsers, issue_tag=issueTag, location=location)

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
# mailBody = fillInEmailBody(10, 23456, "5576589")
# print(mailBody)
# sendEmail(mailSubject, mailBody)
