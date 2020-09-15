import csv
import cs50
# Группа вводится
group = 795
from datetime import datetime
db = cs50.SQL("sqlite:///students.db")
res = db.execute("SELECT `lastName`, `firstName`, `surname`, `urlVideo`, `githubName`, `timestamp`  FROM students WHERE `group`=? ORDER BY `timestamp`", group)
for row in res:
    lastName = row["lastName"]
    firstName = row["firstName"]
    surname = row["surname"]
    githubName = row["githubName"]
    urlVideo = row["urlVideo"]
    timestamp = row["timestamp"]
    d = datetime.strptime(timestamp,'%Y/%m/%d %H:%M:%S %p GMT+7') 

    print(lastName,", ", firstName," | ",  urlVideo, " | ", d.date())
res = db.execute("SELECT COUNT(firstName) as N FROM students WHERE `group`=?", group)[0]
print(res['N'])
