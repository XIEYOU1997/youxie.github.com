# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox, QLineEdit
from Bikes import *
from Customers import *
from Operators import *
from Managers import *
from decimal import Decimal

cus = Customer('')
Bikenum = 0
stationNum4Query = ""
accountnum = 0
b = 0


class Ui_Register(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 208)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
                                         "    background-color:rgb(33, 33, 43)\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 50, 231, 21))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "    color:rgb(255,255,255);\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 80, 231, 21))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
                                      "    color:rgb(255,255,255);\n"
                                      "}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 52, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 131, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(195, 145, 241, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    background-color:rgb(71, 187, 98);\n"
                                      "    color:rgb(255,255,255);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 110, 231, 21))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
                                      "    color:rgb(255,255,255);\n"
                                      "}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 110, 131, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Registration", "Registration"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" color:#ffffff;\">Enter your email</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" color:#ffffff;\">Enter your password</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Register"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" color:#ffffff;\">Enter your balence</span></p></body></html>"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(759, 375)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("QPushButton{\n"
                                 "    font: 12pt \"Trebuchet MS\";\n"
                                 "    padding:5px 10px;\n"
                                 "    color:rgb(81, 80, 82);\n"
                                 "    background-color:rgb(70, 166, 255);\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
                                         "    background-color:rgb(33, 33, 43)\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 230, 431, 32))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    background-color:rgb(71, 187, 98);\n"
                                        "    color:rgb(255,255,255);\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 150, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(15)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 190, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 70, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Zapfino")
        font.setPointSize(18)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("Qlabel{\n"
                                   "fontcolor:rgb(255, 255, 255);\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 150, 321, 21))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "    color:rgb(255,255,255);\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 190, 321, 21))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
                                      "    color:rgb(255,255,255);\n"
                                      "}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 270, 431, 32))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    background-color:rgb(71, 187, 98);\n"
                                      "    color:rgb(255,255,255);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Welcome to Shared Bike System", "Welcome to Shared Bike System"))
        self.pushButton_2.setText(_translate("MainWindow", "User/Stuff Log in"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" color:#ffffff;\">Account Name</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" color:#ffffff;\">Password</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" color:#ffffff;\">Shared Bike System</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Register"))


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 470)

        self.browser = QWebEngineView()

        # 加载外部页面，调用
        # self.browser.load(QtCore.QUrl("https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318&markers=color:red%7Clabel:C%7C40.718217,-73.998284&key=AIzaSyA5P1BYw5rP4TGUk0kb4iUevS7-K5d5LQ0"))
        self.browser.setHtml('''
            <!DOCTYPE html>
    <html>
      <head>
        <style>
           /* Set the size of the div element that contains the map */
          #map {
            height: 400px;  /* The height is 400 pixels */
            width: 100%;  /* The width is the width of the web page */
           }
        </style>
      </head>
      <body>
        <h3>STATION MAP</h3>
        <!--The div element for the map -->
        <div id="map"></div>
        <script>
    // Initialize and add the map
    var labels = '12345';
    
    function initMap() {
      // The location of Uluru
      var u1 = {lat: 55.863215, lng: -4.263794};
      var u2 = {lat: 55.863229, lng: -4.261262};
      var u3 = {lat: 55.870734, lng: -4.270268};
      var u4 = {lat: 55.885732, lng: -4.312699};
      var u5 = {lat: 55.873783, lng: -4.287991};

      // The map, centered at Uluru
      var map = new google.maps.Map(
          document.getElementById('map'), {zoom: 13, center: u3});
      // The marker, positioned at Uluru
      var marker1 = new google.maps.Marker({position: u1, label: labels[0], map: map});
      var marker2 = new google.maps.Marker({position: u2, label: labels[1], map: map});
      var marker3 = new google.maps.Marker({position: u3, label: labels[2], map: map});
      var marker4 = new google.maps.Marker({position: u4, label: labels[3], map: map});
      var marker5 = new google.maps.Marker({position: u5, label: labels[4], map: map});
    }
    
        </script>
        <!--Load the API from the specified URL
        * The async attribute allows the browser to render the page while the API loads
        * The key parameter will contain your own API key (which is not needed for this tutorial)
        * The callback parameter executes the initMap() function
        -->
        <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyA5P1BYw5rP4TGUk0kb4iUevS7-K5d5LQ0&callback=initMap">
        </script>
      </body>
    </html>''')
        self.setCentralWidget(self.browser)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("QWidget{\n"
                           "background-color:rgb(214,214,214);\n"
                           "}")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(200, 10, 581, 31))
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
                                       "color:rgb(255,255,255);\n"
                                       "}")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 410, 161, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color:rgb(71, 187, 98);\n"
                                      "color:rgb(255,255,255);\n"
                                      "font-size:17px;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 410, 281, 41))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "background-color:rgb(71, 187, 98);\n"
                                        "color:rgb(255,255,255);\n"
                                        "font-size:17px;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 410, 91, 41))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "background-color:rgb(71, 187, 98);\n"
                                        "color:rgb(255, 96, 99);\n"
                                        "font-size:17px;\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(790, 10, 101, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 410, 171, 41))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
                                        "background-color:rgb(71, 187, 98);\n"
                                        "color:rgb(255,255,255);\n"
                                        "font-size:17px;\n"
                                        "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 380, 171, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 380, 261, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(530, 380, 281, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit.setPlaceholderText("Input station No. to check:")
        self.lineEdit_2.setPlaceholderText("Input bike's No. to rent")
        self.lineEdit_3.setPlaceholderText("Input Destination Station No. to return")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Shared Bike System - User", "Shared Bike System - User"))
        self.textBrowser.setHtml(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#ffffff;\">Shared Bike User System</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; color:#ffffff;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Rent"))
        self.pushButton_2.setText(_translate("Form", "Return"))
        self.pushButton_3.setText(_translate("Form", "Report"))
        self.pushButton_4.setText(_translate("Form", "My Account"))
        self.pushButton_5.setText(_translate("Form", "Check"))


class MyAccountWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 70, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(72, 160, 131, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color:rgb(71, 187, 98);\n"
                                      "color:rgb(255,255,255);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 160, 131, 51))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "background-color:rgb(71, 187, 98);\n"
                                        "color:rgb(255,255,255);\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 130, 16, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 70, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(165, 132, 131, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        left = b
        owe = 0.00

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("My Account", "My Account"))
        self.label.setText(_translate("Form", "￡"))
        self.pushButton.setText(_translate("Form", "Refresh"))
        self.pushButton_2.setText(_translate("Form", "Pay"))
        self.label_2.setText(_translate("Form", "￡"))
        self.label_3.setText(_translate("Form", str(left) + " Left"))
        self.label_4.setText(_translate("Form", str(owe) + "  to be paid"))


class Ui_OperatorTerminal(object):
    def setupUi(self, OperatorTerminal):
        OperatorTerminal.setObjectName("OperatorTerminal")
        OperatorTerminal.resize(578, 435)
        OperatorTerminal.setWindowTitle("OperatorTerminal")
        self.lineEdit = QtWidgets.QLineEdit(OperatorTerminal)
        self.lineEdit.setGeometry(QtCore.QRect(150, 285, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(OperatorTerminal)
        self.pushButton.setGeometry(QtCore.QRect(340, 280, 191, 45))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(OperatorTerminal)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 331, 51, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(OperatorTerminal)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 326, 191, 45))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(OperatorTerminal)
        self.label.setGeometry(QtCore.QRect(60, 335, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(OperatorTerminal)
        self.label_2.setGeometry(QtCore.QRect(210, 335, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(OperatorTerminal)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 331, 41, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.listView = QtWidgets.QListView(OperatorTerminal)
        self.listView.setGeometry(QtCore.QRect(15, 21, 541, 231))
        self.listView.setObjectName("listView")
        self.label_3 = QtWidgets.QLabel(OperatorTerminal)
        self.label_3.setGeometry(QtCore.QRect(60, 290, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        # self.pushButton_3 = QtWidgets.QPushButton(OperatorTerminal)
        # self.pushButton_3.setGeometry(QtCore.QRect(340, 370, 191, 45))
        # self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(OperatorTerminal)
        QtCore.QMetaObject.connectSlotsByName(OperatorTerminal)

    def retranslateUi(self, OperatorTerminal):
        _translate = QtCore.QCoreApplication.translate
        OperatorTerminal.setWindowTitle(_translate("Shared Bike System - Operator", "Shared Bike System - Operator"))
        self.pushButton.setText(_translate("OperatorTerminal", "Confirm Repaired"))
        self.pushButton_2.setText(_translate("OperatorTerminal", "Confirm Moving"))
        self.label.setText(_translate("OperatorTerminal", "Move Bike:"))
        self.label_2.setText(_translate("OperatorTerminal", "to Station:"))
        self.label_3.setText(_translate("OperatorTerminal", "Repair Bike:"))



class Ui_AvailableBikes(object):
    def setupUi(self, AvailableBikes):
        AvailableBikes.setObjectName("AvailableBikes")
        AvailableBikes.resize(400, 300)
        self.listView = QtWidgets.QListView(AvailableBikes)
        self.listView.setGeometry(QtCore.QRect(20, 10, 361, 271))
        self.listView.setObjectName("listView")

        bikeList4user = cus.checkAllBikes(stationNum4Query)
        listview = self.listView
        slm = QStringListModel()
        self.qList = bikeList4user
        slm.setStringList(self.qList)
        listview.setModel(slm)

        self.retranslateUi(AvailableBikes)
        QtCore.QMetaObject.connectSlotsByName(AvailableBikes)

    def retranslateUi(self, AvailableBikes):
        _translate = QtCore.QCoreApplication.translate
        AvailableBikes.setWindowTitle(_translate("AvailableBikes", "AvailableBikes"))



class Ui_ManagerWindow(object):
    def setupUi(self, OperatorTerminal):
        OperatorTerminal.setObjectName("OperatorTerminal")
        OperatorTerminal.resize(578, 343)
        self.listView = QtWidgets.QListView(OperatorTerminal)
        self.listView.setGeometry(QtCore.QRect(15, 21, 541, 231))
        self.listView.setObjectName("listView")
        self.pushButton_3 = QtWidgets.QPushButton(OperatorTerminal)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 258, 191, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(OperatorTerminal)
        self.label_4.setGeometry(QtCore.QRect(60, 270, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(OperatorTerminal)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 260, 221, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setPlaceholderText("Input like 2016-05-05 20:28:54")
        self.label_5 = QtWidgets.QLabel(OperatorTerminal)
        self.label_5.setGeometry(QtCore.QRect(80, 309, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(OperatorTerminal)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 300, 221, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setPlaceholderText("Input like 2016-05-05 20:28:54")

        self.retranslateUi(OperatorTerminal)
        QtCore.QMetaObject.connectSlotsByName(OperatorTerminal)

    def retranslateUi(self, OperatorTerminal):
        _translate = QtCore.QCoreApplication.translate
        OperatorTerminal.setWindowTitle(_translate("Shared Bike System - Manager", "Shared Bike System - Manager"))
        self.pushButton_3.setText(_translate("OperatorTerminal", "Generate Report"))
        self.label_4.setText(_translate("OperatorTerminal", "From"))
        self.label_5.setText(_translate("OperatorTerminal", "to"))


# ---------------------------bound buttons within each windows with functions----------------------------------------- #
class registerWindow(QtWidgets.QMainWindow, Ui_Register):
    def __init__(self):
        super(registerWindow, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.registration)

    def registration(self):
        regName = self.lineEdit.text()
        regPassword = self.lineEdit_2.text()
        regBalence = self.lineEdit_3.text()
        if Register(regName, regPassword, regBalence):
            QMessageBox.warning(self,
                                "Congratulation!",
                                "Welcome to our system",
                                QMessageBox.Yes)
            self.close()
        else:
            QMessageBox.warning(self,
                                "Warning",
                                "Your email has been taken",
                                QMessageBox.Yes)


class loginWindow(QtWidgets.QWidget, Ui_MainWindow):

    def __init__(self):
        super(loginWindow, self).__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.login)  # 绑定按钮login功能
        self.pushButton.clicked.connect(self.ShowRegister)

    def login(self):
        global accountnum
        login_username = self.lineEdit.text()
        accountnum = login_username
        login_password = self.lineEdit_2.text()
        judge = Login(login_username, login_password)

        if judge == "user":
            self.window = userMainWindow()
            self.window.show()
            self.close()

        elif judge == "manager":
            self.window = managerMainWindow()
            self.window.show()
            self.close()

        elif judge == "operator":
            self.window = operatorMainWindow()
            self.window.show()
            self.close()

        else:
            QMessageBox.warning(self,
                                "Warning",
                                "WRONG ACCOUNT NAME OR PASSWORD！",
                                QMessageBox.Yes)
            self.lineEdit.setFocus()

    def ShowRegister(self):
        self.window = registerWindow()
        self.window.show()


class userMainWindow(QtWidgets.QMainWindow, Ui_Form):

    def __init__(self):
        super(userMainWindow, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.rentbikes)
        self.pushButton_3.clicked.connect(self.report)
        self.pushButton_2.clicked.connect(self.returnBike)
        self.pushButton_4.clicked.connect(self.cheBal)
        self.pushButton_4.clicked.connect(self.showWindow)
        # self.pushButton_4.clicked.connect(self.showWindow)
        self.pushButton_5.clicked.connect(self.showBikes)

    def cheBal(self):
        cus =Customer(accountnum)
        global b
        b = cus.CheckBalance()

    def showWindow(self):
        self.window = userAccountWindow()
        self.window.show()

    def showBikes(self):
        global stationNum4Query
        q = self.lineEdit.text()
        stationNum4Query = "station" + q

        self.window = userCheckAvailableBikes()
        self.window.show()

    def rentbikes(self):
        global cus
        global Bikenum  # define global variable for further function
        Bikenum = self.lineEdit_2.text()
        cus = Customer(accountnum)
        i = cus.rent(Bikenum)

        if i == 3:
            QMessageBox.warning(self,
                                "Success",
                                "Suceess, enjoy!", QMessageBox.Yes)
        elif i == 1:
            QMessageBox.warning(self,
                                "This bike is broken",
                                "This bike is broken", QMessageBox.Yes)
        elif i == 2:
            QMessageBox.warning(self,
                                "This bike is being used",
                                "This bike is being used", QMessageBox.Yes)

    def report(self):
        Bikenum = self.lineEdit_2.text()
        cus = Customer(accountnum)
        cus.reportState(Bikenum)
        QMessageBox.warning(self,
                            "Success",
                            "You reported a bike is broken", QMessageBox.Yes)




    def returnBike(self):
        stationNum4Return = self.lineEdit_3.text()
        cus = Customer(accountnum)
        cus.return_bike(Bikenum, stationNum4Return)
        QMessageBox.warning(self,
                            "Success",
                            "You returned a bike", QMessageBox.Yes)


class userCheckAvailableBikes(QtWidgets.QMainWindow, Ui_AvailableBikes):
    def __init__(self):
        super(userCheckAvailableBikes, self).__init__()
        self.setupUi(self)


class userAccountWindow(QtWidgets.QMainWindow, MyAccountWindow):
    def __init__(self):
        super(userAccountWindow, self).__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.Paybutton)
        self.pushButton.clicked.connect(self.Refreshbutton)

    def Refreshbutton(self):
        left = cus.CheckBalance()
        cus.CalculateMoney()
        owe = cus.CheckLastbill()

        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Form", str(left) + " Left"))
        self.label_4.setText(_translate("Form", str(owe) + "   to be paid"))

    def Paybutton(self):
        left = (round(cus.CheckBalance(), 2) - round(cus.CalculateMoney(), 2)) # calculate balance
        owe = 0.00  # how much did last ride cost
        cus.UpdateBalance()
        cus.UpdateLastBill()

        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Form", str(left) + " Left"))
        self.label_4.setText(_translate("Form", str(owe) + "    to be paid"))


class operatorMainWindow(QtWidgets.QMainWindow, Ui_OperatorTerminal):
    def __init__(self):
        super(operatorMainWindow, self).__init__()
        self.setupUi(self)
        # Initialise all bikes' state list
        listview = self.listView
        slm = QStringListModel()
        self.qList = TrackLocation()
        slm.setStringList(self.qList)
        listview.setModel(slm)

        self.pushButton.clicked.connect(self.ConfirmRepaired)
        self.pushButton_2.clicked.connect(self.ConfirmMoving)
        # self.pushButton_3.clicked.connect(self.GenerateReport)

    def ConfirmRepaired(self):
        brokenBikeNum = int(self.lineEdit.text())
        Repair(brokenBikeNum)
        # Refresh all bikes' state list
        listview = self.listView
        slm = QStringListModel()
        self.qList = TrackLocation()
        slm.setStringList(self.qList)
        listview.setModel(slm)

    def ConfirmMoving(self):
        bike2MoveNum = int(self.lineEdit_2.text())
        newLocation = self.lineEdit_3.text()
        MoveBikeas(bike2MoveNum, newLocation)
        # Refresh all bikes' state list
        listview = self.listView
        slm = QStringListModel()
        self.qList = TrackLocation()
        slm.setStringList(self.qList)
        listview.setModel(slm)

    # def GenerateReport(self):
    #     visual()
    #     QMessageBox.warning(self,
    #                         "Warning",
    #                         "Image saved in source folder",
    #                         QMessageBox.Yes)

class managerMainWindow(QtWidgets.QMainWindow, Ui_ManagerWindow):
    def __init__(self):
        super(managerMainWindow, self).__init__()
        self.setupUi(self)
        # Initialise all bikes' state list
        listview = self.listView
        slm = QStringListModel()
        self.qList = TrackLocation()
        slm.setStringList(self.qList)
        listview.setModel(slm)

        self.pushButton_3.clicked.connect(self.GenerateReport)

    def GenerateReport(self):
        timeArray1 = time.strptime(self.lineEdit_4.text(), "%Y-%m-%d %H:%M:%S")
        timeArray2 = time.strptime(self.lineEdit_5.text(), "%Y-%m-%d %H:%M:%S")
        timestamp1 = time.mktime(timeArray1)
        timestamp2 = time.mktime(timeArray2)
        # print(timestamp1)
        # print(timestamp2)

        visual(timestamp1, timestamp2)
        QMessageBox.warning(self,
                            "Warning",
                            "Image saved in source folder",
                            QMessageBox.Yes)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    entrance = loginWindow()
    entrance.show()

    sys.exit(app.exec_())
