#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:00:01 2019

@author: brillianthc
"""
import pymysql
SQL_Password = "Liyize97"

def TrackLocation():
    db = pymysql.connect(host="localhost", user="root", passwd=SQL_Password, db="SharedBikes", charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT idBikes,location,state,usable FROM bikes ORDER BY location")
    results = cursor.fetchall()
    bikeList4operator = list()
    bikeList4operator.append(str({'Bike ID  |  Location |  In Good Condition or not |  Idle or not'}))
    for row in results:
        bikeList4operator.append(str(row))

    return bikeList4operator



def Repair(bike_ID):
    db = pymysql.connect(host="localhost", user="root", passwd=SQL_Password, db="SharedBikes", charset="utf8")
    cursor = db.cursor()
    # bike_ID = int(input("please input bike id "))
    cursor.execute("UPDATE Bikes SET state = 'yes' WHERE idBikes = %d" % bike_ID)
    db.commit()
    cursor.execute("UPDATE Bikes SET broken_time = NULL WHERE idBikes = %d" % bike_ID)
    db.commit()
    db.close()


def MoveBikeas(bike_ID, locationNum):
    db = pymysql.connect(host="localhost", user="root", passwd=SQL_Password, db="SharedBikes", charset="utf8")
    cursor = db.cursor()
    # bike_ID = int(input("please input bike id "))
    # locationNum = input("plesase input station number ")
    location = "station" + locationNum
    cursor.execute("UPDATE Bikes SET location = '%s' WHERE idBikes = %d" % (location, bike_ID))
    db.commit()
    db.close()
