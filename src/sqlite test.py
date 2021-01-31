import sqlite3
import csv

sqlite_connection = sqlite3.connect("database.db")
cursor = sqlite_connection.cursor()


def get_info(lesson):
    cursor.execute('SELECT студент, avg(оценка) FROM оценки WHERE предмет="{0}" GROUP BY студент'.format(lesson))
    for student in cursor.fetchall():
        for i in student:
            print(str(i) + " ", end='')
        print()


def create_db():
    try:
        cursor.execute("""CREATE TABLE оценки(предмет, студент, оценка, время получения)""")
        cursor.execute("""CREATE TABLE предметы(название предмета, имя преподавателя)""")
        cursor.execute("""CREATE TABLE студенты(имя, фамилия, страна, группа, дата рождения)""")
        sqlite_connection.commit()
    except:
        print("Что-то пошло не так")


def open_file(properties, file):
    reader = [tuple(x) for x in list(csv.reader(file))]
    cursor.executemany(properties, reader)
    sqlite_connection.commit()


def upload():
    with open('../../SQLPractice/src/marks.csv', "r") as file:
        open_file("INSERT INTO оценки VALUES (?,?,?,?)", file)

    with open('students.csv', "r") as file:
        open_file("INSERT INTO студенты VALUES (?,?,?,?,?)", file)

    with open('../../SQLPractice/src/lessons.csv', "r") as file:
        open_file("INSERT INTO предметы VALUES (?,?)", file)


create_db()
upload()
print("Оценки по предмету физика")
get_info('physic')
print("Оценки по предмету литература")
get_info('literature')
