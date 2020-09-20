import sqlite3
import smtplib, ssl
from email.message import EmailMessage
import os


# Получаем информацию о поулчателх
con = sqlite3.connect("students.db")
db = con.cursor()
receivers = db.execute("SELECT `email`, `lastName`, `firstName`, `surname`    FROM students;").fetchall()

#Данные для подключения
smtp_server = "mail.tspu.edu.ru"
port = 587
sender_email = "Vadim G.B. <vadim@tspu.edu.ru>"
password = os.getenv("EMAIL_PASSWORD") 


# Подкючаемся к серверу.
context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login("vadim", password)

# Отправка писем
    for receiver in receivers: 
        receiver_email = receiver[0] 
        name = receiver[2] 
        surname = receiver[3] 
        text =f"\n {name} {surname}, вы сдали задание 10 недели." 
        msg = EmailMessage()
        msg.set_content(text)
        msg['From'] = sender_email 
        msg['Subject'] = "Задание 10 недели"
        msg['To'] = receiver_email
        print(text)
        server.send_message(msg)
except Exception as e:
    print(e)

finally:
    server.quit()










