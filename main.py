import os
import smtplib
print("smtplib imported!")

sender = os.environ.get("sender")
passward = os.environ.get("passward")
receiver = os.environ.get("receiver")
subject = os.environ.get("subject")
body = os.environ.get("body")
spamcount = os.environ.get("count")

server = smtplib.SMTP('smtp.gmail.com',587)
print("tls handshaking")
server.ehlo()
server.starttls()
print("logging in...")
server.login(sender, passward)
print("Logged in!")
subject = str(subject)
body = str(body)


msg = f"Subject :{subject}\n\n{body}"
print("sending message...")
for i in range(spamcount):
	server.sendmail(sender, receiver, msg)
	print("message sent!"+i)
server.quit()