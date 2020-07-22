#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:24:56 2019

@author: youxie
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymysql
from matplotlib.pyplot import plot,savefig
SQL_Password = "Liyize97"

def visual(tt1, tt2):
    db = pymysql.connect(host="localhost", user="root", passwd=SQL_Password, db="SharedBikes", charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Bikes WHERE location = '%s'"%'station1')
    results = cursor.fetchall()
    s1 = 0
    for row in results:
        s1 += 1
    cursor.execute("SELECT * FROM Bikes WHERE location = '%s'"%'station2')
    results = cursor.fetchall()
    s2 = 0
    for row in results:
        s2 += 1
    cursor.execute("SELECT * FROM Bikes WHERE location = '%s'"%'station3')
    results = cursor.fetchall()
    s3 = 0
    for row in results:
        s3 += 1
    cursor.execute("SELECT * FROM Bikes WHERE location = '%s'"%'station4')
    results = cursor.fetchall()
    s4 = 0
    for row in results:
        s4 += 1
    cursor.execute("SELECT * FROM Bikes WHERE location = '%s'"%'station5')
    results = cursor.fetchall()
    s5 = 0
    for row in results:
        s5 += 1

    cursor.execute("SELECT broken_time FROM Bikes WHERE broken_time>%d AND broken_time<%d"% (tt1, tt2))
    results = cursor.fetchall()
    t1 = 0
    for row in results:
        t1 += 1
    t2 = 100 - t1

    index=np.arange(5)
    values=[s1,s2,s3,s4,s5]
    plt.bar(index,values,color='k',label='Number of bikes in station')
    plt.title('Bike Distribution')
    plt.xticks(index,['Station1','Station2','Station3','Station4','Station5'])
    plt.legend(loc=2)
    for a,b in zip(index,values):
        plt.text(a,b+0.5,'%d'%b,ha='center',va='bottom',fontsize=11)
    # plt.show()
    plt.savefig("Bike_Distribution_Bar.png")
    plt.close()


    labels=['Station1','Station2','Station3','Station4','Station5']
    values=[s1, s2, s3, s4, s5]
    colors=['yellow','blue','red','orange','green']
    plt.title('Bike Distribution')
    plt.pie(values,labels=labels,colors=colors,shadow=True,autopct='%1.1f%%',startangle=180)
    plt.axis('equal')
    # plt.show()
    plt.savefig("Bike_Distribution_Pie.png")
    plt.close()

    labels = ['Broken Condition', 'Perfect Condition']
    values = [t1, t2]
    colors = ['yellow', 'red']
    plt.title('Bike Condition')
    plt.pie(values,labels=labels,colors=colors,shadow=True,autopct='%1.1f%%',startangle=180)
    plt.axis('equal')
    plt.savefig("Bike_Perfect_Rate.png")