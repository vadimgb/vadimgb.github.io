import csv
import cs50
open("students.db", "w").close()
db = cs50.SQL("sqlite:///students.db")

db.execute("CREATE TABLE students('id' INTEGER, 'timestamp' NUMERIC,'email' VARCHAR(155), \
        'githubName' VARCHAR(255), 'firstName' VARCHAR(255), \
        'surname' VARCHAR(255), 'lastName' VARCHAR(255),\
        'group' INTEGER,  PRIMARY KEY('id'))") 

with open("Форма.csv", "r") as file: 
    rows = csv.DictReader(file)
    for row in rows:
        timestamp = row["Timestamp"]
        email = row["Username"]
        githubName = row["Ваше имя на GitHub"]
        firstName = row["Имя"]
        surname = row["Отчество"]
        lastName = row["Фамилия"]
        group = row["Группа"]
        db.execute("INSERT INTO students ('timestamp', 'email', 'githubName', \
                'firstName', 'surname', 'lastName', 'group') \
                VALUES(?, ?, ?, ?, ?, ?, ?)", timestamp, email, githubName, \
                firstName, surname, lastName, int(group))




