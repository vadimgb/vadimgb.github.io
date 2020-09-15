import sqlite3
import smtplib, ssl
from email.message import EmailMessage
from datetime import datetime
import os
#Настройка письма--------------------
group = 784
email_subject = "Задание недели 1, 2"
#имя, msg_text
msg_text = "выполняем все для недели 1, 2 с сайта vadimgb.github.io"
startDatetime = datetime(2020, 9, 4, 0, 0)
#-------------------------------------

# Получаем информацию о поулчателх
con = sqlite3.connect("students.db")
db = con.cursor()
receivers = db.execute("SELECT `email`, `lastName`, `firstName`, `surname`, `timestamp`    FROM students WHERE `group`=?;", (group,) ).fetchall()

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
        text =f"\n {name} {surname}, {msg_text}." 
        msg = EmailMessage()
        msg.set_content(text)
        msg['From'] = sender_email 
        msg['Subject'] = email_subject
        msg['To'] = receiver_email
        timestamp = receiver[4]
        d = datetime.strptime(timestamp,'%Y/%m/%d %H:%M:%S %p GMT+7') 
        if startDatetime < d: 
            print(text, d.ctime()) 
            server.send_message(msg)
except Exception as e:
    print(e)

finally:
    server.quit()










