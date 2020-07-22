#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:51:57 2019

@author: brillianthc
"""
import pymysql
from datetime import datetime
import time
from Bikes import Bikes
SQL_Password = "Liyize97"
db = pymysql.connect(host="localhost", user="root", passwd=SQL_Password, db="SharedBikes", charset="utf8")
cursor = db.cursor()


def Register(email, password, balance):
    # global email
    # email = input("Enter you email ")
    # password = input("Enter your password ")
    # balance = input("How much money you want to add to your balance ")
    cursor.execute("""SELECT email FROM users WHERE email = '%s' """ % email)
    if cursor.fetchone():
        cursor.close()
        db.close()
        return False
    else:
        cursor.execute("""INSERT INTO Users(email,password,balance)
                               VALUES ('%s', '%s', '%s')""" % (email, password, balance))
        db.commit()
        db.close()
        return True



def Login(account, password):
    #    account = input("Please enter your eamil to login ")
    #    password = input("Please enter your password ")
    db = pymysql.connect(host="localhost", user="root", passwd=SQL_Password, db="SharedBikes", charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users where email = '%s'" % account)
    if cursor.fetchone() is not None:
        cursor.execute("SELECT * FROM users where email = '%s'" % account)
        result = cursor.fetchone()
        passwordInDb = result[1]
        if password == passwordInDb:
            # print("Login success")
            return "user"
        else:
            return "wrong"
    cursor.close()

    cursor = db.cursor()
    cursor.execute("SELECT * FROM managers where ManagerName = '%s'" % account)
    if cursor.fetchone() is not None:
        cursor.execute("SELECT * FROM managers where ManagerName = '%s'" % account)
        result = cursor.fetchone()
        passwordInDb = result[1]
        if password == passwordInDb:
            return "manager"

        else:
            # print("Invaild account or password")
            return "wrong"
    cursor.close()

    cursor = db.cursor()
    cursor.execute("SELECT * FROM operators where Operators_ID = '%s'" % account)
    result = cursor.fetchone()
    passwordInDb = result[1]
    if password == passwordInDb:
        return "operator"

    else:
        # print("Invaild account or password")
        return "wrong"


class Customer:
    dt = 0
    dt2 =0

    def __init__(self, email):
        self.Email = email
        # self.dt = ""
    def checkAllBikes(self, stationNum4Query):
        db = pymysql.connect(host="localhost", user="root", passwd=SQL_Password, db="SharedBikes", charset="utf8")
        cursor = db.cursor()
        # print(stationNum4Query)
        cursor.execute("SELECT idBikes, location FROM Bikes WHERE location = '%s' " % stationNum4Query)
        i = 0
        bikeList4user = list()
        for row in cursor.fetchall():
            # print(row)
            bikeList4user.append(str(row))
        db.close()
        return bikeList4user

    def rent(self, bike_ID):
        #        bike_ID = int(input("please input bike id "))
        BikesObject = Bikes(bike_ID)

        if (BikesObject.CheckState() == 1):
            print("This bike is broken")
            return 1
        elif (BikesObject.CheckState() == 2):
            print("This bike is being used")
            return 2
        elif (BikesObject.CheckState() == 3):
            db = pymysql.connect(host="localhost", user="root", passwd=SQL_Password, db="SharedBikes", charset="utf8")
            cursor = db.cursor()
            # print("Success")
            cursor.execute("UPDATE Bikes SET usable = 'no' WHERE idBikes = '%s'" % bike_ID)
            db.commit()
            db.close()
            # self.dt = datetime.now()
            global dt
            dt = datetime.now()
            return 3

    def return_bike(self, bike_ID, station):
        db = pymysql.connect(host="localhost", user="root", passwd=SQL_Password, db="SharedBikes", charset="utf8")
        cursor = db.cursor()
        #         bike_ID = int(input("please input bike id "))
        station = "station" + station
        cursor.execute("UPDATE Bikes SET usable = 'yes' WHERE idBikes = '%s'" % bike_ID)
        cursor.execute("UPDATE Bikes SET location = '%s' WHERE idBikes = '%s'" % (station, bike_ID))
        db.commit()
        db.close()
        global dt2
        dt2 = datetime.now()

    # THis function can be used for users to report a defective bike
    def reportState(self, bike_ID):
        BikesObject = Bikes(bike_ID)
        cursor = db.cursor()
        #         bike_ID = int(input("please input bike id "))
        cursor.execute("UPDATE Bikes SET state = 'no' WHERE idBikes = %s" % bike_ID)

        # BikesObject.RecordBrokenTime()
        # db.commit()
        broken_dt = time.time()
        # broken_dt = str(datetime.now())
        # broken_dt = broken_dt[11:13]
        cursor.execute("UPDATE Bikes SET broken_time = %lf WHERE idBikes = %s" % (broken_dt, bike_ID))
        db.commit()
        db.close()

    # This function can be used to calculate bills
    def CalculateMoney(self):
        db = pymysql.connect(host="localhost", user="root", passwd=SQL_Password, db="SharedBikes", charset="utf8")
        cursor = db.cursor()

        # dt = self.dt
        dt2 = datetime.now()

        money = round((2 * ((dt2 - dt).total_seconds() / 3600)), 2)
        # print(money)
        cursor.execute("UPDATE users SET recentbill = '%s' WHERE email = '%s' " % (money, self.Email))
        db.commit()
        db.close()
        return money

    def UpdateBalance(self):
        db = pymysql.connect(host="localhost", user="root", passwd="Liyize97", db="SharedBikes", charset="utf8")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users where email = '%s'" % self.Email)
        result = cursor.fetchone()
        Cost = result[2]
        Cost = Cost[0:4]
        # print(Cost)
        # print(type(Cost))
        balance = result[3]
        # print(balance)
        # print(type(balance))
        newbalance = str(round(round(float(balance), 2) - round(float(Cost), 2), 2))
        # print(newbalance)
        cursor.execute("UPDATE users SET balance = '%s' WHERE email = '%s'" % (newbalance, self.Email))
        db.commit()
        db.close()

    def UpdateLastBill(self):
        db = pymysql.connect(host="localhost", user="root", passwd="Liyize97", db="SharedBikes", charset="utf8")
        cursor = db.cursor()
        cursor.execute("UPDATE users SET recentbill = '%s' WHERE email = '%s'" % (0, self.Email))
        db.commit()
        db.close()

    def CheckBalance(self):
        db = pymysql.connect(host="localhost", user="root", passwd="Liyize97", db="SharedBikes", charset="utf8")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users where email = '%s'" % self.Email)
        result = cursor.fetchone()
        balance = float(result[3])
        # print(balance)
        db.commit()
        db.close()
        return balance

    def CheckLastbill(self):
        db = pymysql.connect(host="localhost", user="root", passwd="Liyize97", db="SharedBikes", charset="utf8")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users where email = '%s'" % self.Email)
        result = cursor.fetchone()
        lastbill = float(result[2])
        db.commit()
        db.close()
        return lastbill



