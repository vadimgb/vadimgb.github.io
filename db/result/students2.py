import csv
import cs50
csv_file1 ="students - 791.csv" 
csv_forma = "Форма.csv"

open("students.db", "w").close()
db = cs50.SQL("sqlite:///students.db")

db.execute("CREATE TABLE students('id' INTEGER, 'timestamp' NUMERIC,'email' VARCHAR(155), \
        'result' REAL,\
        'githubName' VARCHAR(255), 'firstName' VARCHAR(255), \
        'surname' VARCHAR(255), 'lastName' VARCHAR(255),\
        'group' INTEGER, 'subgroup' CHAR(1), PRIMARY KEY('id'));") 

with open(csv_file1, "r") as file_csv1:         
    rows1 = csv.DictReader(file_csv1)
    for row1 in rows1:
        firstName1 = row1["firstName"].capitalize()
        lastName1 = row1["lastName"].capitalize()
        surname1 = row1["surname"].capitalize()
        result1 = row1["result"]

        find_count = 0
        with open(csv_forma, "r") as file_forma:
            rows = csv.DictReader(file_forma)
            for row in rows:
                timestamp = row["Timestamp"]
                githubName = row["Ваше имя на GitHub"]
                firstName = row["Имя"]
                lastName = row["Фамилия"]
                surname = row["Отчество"]
                group = row["Номер группы"]
                subgroup = row["Подгруппа"]
                email = row["Username"] 
                if firstName1 == firstName and surname1 == surname and lastName1 == lastName: 
                    db.execute("INSERT INTO students ('timestamp', 'email', 'result', 'githubName', \
                    'firstName', 'surname', 'lastName', 'group', 'subgroup') \
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", timestamp, email, float(result1), githubName, \
                    firstName, surname, lastName, int(group), subgroup)
                    find_count += 1
            if find_count == 0:
                print("Не найден:", lastName1, firstName1)
            elif find_count > 1:
                print("Дублирование:", lastName1, firstName1)
            else:
                print("     ", lastName1, firstName1)

