import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

f = open("../creds.txt", "r")
creds = f.readlines()
f.close()
login = creds[0].strip("/n") # paste your login generated by Mailtrap
password = creds[1].strip("/n") # paste your password generated by Mailtrap

sender_email = "knockknockhackathon@gmail.com"
receiver_email = "knockknockhackathon@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = "Turn On"
message["From"] = sender_email
message["To"] = receiver_email
# Write the plain text part
text = """Hi, please turn on!!!"""

# convert both parts to MIMEText objects and add them to the MIMEMultipart message
part1 = MIMEText(text, "plain")
part2 = MIMEText(text, "html")
message.attach(part1)
message.attach(part2)

# send your email
with smtplib.SMTP("smtp.gmail.com:587") as server:
    server.ehlo()
    server.starttls()
    server.login(login, password)
    server.sendmail( sender_email, receiver_email, message.as_string() )

print('Sent')