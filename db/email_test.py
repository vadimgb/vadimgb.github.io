import smtplib, ssl
from email.message import EmailMessage
import os

smtp_server = "mail.tspu.edu.ru"
port = 587
sender_email = "Vadim G.B. <vadim@tspu.edu.ru>"
receiver_email = "Вадим Б.Г. <vadimgb@yandex.ru>"
password = os.getenv("EMAIL_PASSWORD") 
name = "Лена"
text =f"\n {name}, не забудьте выполнить задание 14 недели." 
msg = EmailMessage()
msg.set_content(text)
msg['From'] = sender_email 
msg['Subject'] = "Задание 14 недели"
msg['To'] = receiver_email


context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login("vadim", password)
    server.send_message(msg)
except Exception as e:
    print(e)

finally:
    server.quit()
