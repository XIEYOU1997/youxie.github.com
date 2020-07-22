import pymysql
from datetime import datetime

SQL_Password = "Liyize97"
db = pymysql.connect(host="localhost", user="root", passwd=SQL_Password, db="SharedBikes", charset="utf8")
cursor = db.cursor()


class Bikes():

    def __init__(self, id):
        self.id = id
        # print(id)

    def Usable(self):
        cursor.execute("SELECT * FROM bikes where idBikes = %d" % self.id)
        results = cursor.fetchall()
        for row in results:
            isusable = row[3]
            print("Does this bike can be used? %s" % isusable)

    def CheckState(self):
        db = pymysql.connect(host="localhost", user="root", passwd=SQL_Password, db="SharedBikes", charset="utf8")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM bikes where idBikes = %s" % self.id)
        results = cursor.fetchall()
        for row in results:
            state1 = row[2]
            state2 = row[3]
        if state1 == 'no' and state2 == 'yes':
            return 1
        elif state1 == 'yes' and state2 == 'no':
            return 2
        elif state1 == 'yes' and state2 == 'yes':
            return 3






