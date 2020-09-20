import csv
import cs50
csv_file = "pset10.csv"
url_video = "Укажите URL видео,  демонстрирующего, вашу реализацию проекта 10-ой недели."
open("students.db", "w").close()
db = cs50.SQL("sqlite:///students.db")

db.execute("CREATE TABLE students('id' INTEGER, 'timestamp' NUMERIC,'email' VARCHAR(155), \
        'urlVideo' VARCHAR(255),\
        'githubName' VARCHAR(255), 'firstName' VARCHAR(255), \
        'surname' VARCHAR(255), 'lastName' VARCHAR(255),\
        'group' INTEGER, 'subgroup' CHAR(1), PRIMARY KEY('id'));") 

with open(csv_file, "r") as file: 
    rows = csv.DictReader(file)
    for row in rows:
        timestamp = row["Timestamp"]
        email = row["Username"]
        urlVideo = row[url_video]
        githubName = row["Ваше имя на GitHub"]
        firstName = row["Имя"]
        surname = row["Отчество"]
        lastName = row["Фамилия"]
        group = row["Номер группы"]
        subgroup = row["Подгруппа"]
        db.execute("INSERT INTO students ('timestamp', 'email', 'urlVideo', 'githubName', \
                'firstName', 'surname', 'lastName', 'group', 'subgroup') \
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", timestamp, email, urlVideo, githubName, \
                firstName, surname, lastName, int(group), subgroup)




