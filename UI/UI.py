# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v0.2copy.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1361, 483)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1818, 668))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(1800, 650))
        self.frame.setMaximumSize(QtCore.QSize(16771215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget_10 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(1090, 350, 121, 251))
        self.gridLayoutWidget_10.setObjectName("gridLayoutWidget_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.trainimage_8 = QtWidgets.QLabel(self.gridLayoutWidget_10)
        self.trainimage_8.setObjectName("trainimage_8")
        self.gridLayout_10.addWidget(self.trainimage_8, 0, 0, 1, 1)
        self.gotobutton = QtWidgets.QPushButton(self.frame)
        self.gotobutton.setGeometry(QtCore.QRect(620, 620, 41, 23))
        self.gotobutton.setObjectName("gotobutton")
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(810, 350, 121, 251))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.trainimage_6 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.trainimage_6.setObjectName("trainimage_6")
        self.gridLayout_8.addWidget(self.trainimage_6, 0, 0, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(530, 350, 121, 251))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.trainimage_4 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.trainimage_4.setObjectName("trainimage_4")
        self.gridLayout_6.addWidget(self.trainimage_4, 0, 0, 1, 1)
        self.showmetrics = QtWidgets.QPushButton(self.frame)
        self.showmetrics.setGeometry(QtCore.QRect(10, 90, 71, 81))
        self.showmetrics.setObjectName("showmetrics")
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(950, 350, 121, 251))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.trainimage_7 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.trainimage_7.setObjectName("trainimage_7")
        self.gridLayout_7.addWidget(self.trainimage_7, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(670, 280, 121, 71))
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(670, 350, 121, 251))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.trainimage_5 = QtWidgets.QLabel(self.gridLayoutWidget_9)
        self.trainimage_5.setObjectName("trainimage_5")
        self.gridLayout_9.addWidget(self.trainimage_5, 0, 0, 1, 1)
        self.imagecounter = QtWidgets.QSpinBox(self.frame)
        self.imagecounter.setGeometry(QtCore.QRect(660, 620, 42, 22))
        self.imagecounter.setObjectName("imagecounter")
        self.nextbutton = QtWidgets.QPushButton(self.frame)
        self.nextbutton.setGeometry(QtCore.QRect(720, 620, 75, 23))
        self.nextbutton.setObjectName("nextbutton")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(1230, 280, 121, 71))
        self.label_9.setObjectName("label_9")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(390, 350, 121, 251))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.trainimage_3 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.trainimage_3.setObjectName("trainimage_3")
        self.gridLayout_5.addWidget(self.trainimage_3, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(250, 280, 121, 71))
        self.label_2.setObjectName("label_2")
        self.totaledit_label = QtWidgets.QLabel(self.frame)
        self.totaledit_label.setGeometry(QtCore.QRect(920, 10, 191, 21))
        self.totaledit_label.setObjectName("totaledit_label")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(250, 350, 121, 251))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.trainimage_2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.trainimage_2.setObjectName("trainimage_2")
        self.gridLayout_4.addWidget(self.trainimage_2, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(810, 280, 121, 71))
        self.label_6.setObjectName("label_6")
        self.train = QtWidgets.QPushButton(self.frame)
        self.train.setGeometry(QtCore.QRect(10, 0, 71, 81))
        self.train.setObjectName("train")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(1090, 280, 121, 71))
        self.label_8.setObjectName("label_8")
        self.gridLayoutWidget_11 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(1230, 350, 121, 251))
        self.gridLayoutWidget_11.setObjectName("gridLayoutWidget_11")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.trainimage_9 = QtWidgets.QLabel(self.gridLayoutWidget_11)
        self.trainimage_9.setObjectName("trainimage_9")
        self.gridLayout_11.addWidget(self.trainimage_9, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(530, 280, 121, 71))
        self.label_4.setObjectName("label_4")
        self.showerror = QtWidgets.QPushButton(self.frame)
        self.showerror.setGeometry(QtCore.QRect(10, 360, 71, 81))
        self.showerror.setObjectName("showerror")
        self.previousbutton = QtWidgets.QPushButton(self.frame)
        self.previousbutton.setGeometry(QtCore.QRect(530, 620, 75, 23))
        self.previousbutton.setObjectName("previousbutton")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(390, 280, 121, 71))
        self.label_3.setObjectName("label_3")
        self.gridLayoutWidget_12 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_12.setGeometry(QtCore.QRect(110, 0, 121, 231))
        self.gridLayoutWidget_12.setObjectName("gridLayoutWidget_12")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.validimage = QtWidgets.QLabel(self.gridLayoutWidget_12)
        self.validimage.setObjectName("validimage")
        self.gridLayout_12.addWidget(self.validimage, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 280, 121, 71))
        self.label.setObjectName("label")
        self.totaledit_count = QtWidgets.QLCDNumber(self.frame)
        self.totaledit_count.setGeometry(QtCore.QRect(1123, 10, 101, 23))
        self.totaledit_count.setObjectName("totaledit_count")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(950, 280, 121, 71))
        self.label_7.setObjectName("label_7")
        self.valid_label = QtWidgets.QLabel(self.frame)
        self.valid_label.setGeometry(QtCore.QRect(240, 10, 121, 251))
        self.valid_label.setObjectName("valid_label")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(110, 350, 121, 251))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.trainimage = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.trainimage.setObjectName("trainimage")
        self.gridLayout_3.addWidget(self.trainimage, 0, 0, 1, 1)
        self.gridLayoutWidget_13 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_13.setGeometry(QtCore.QRect(1370, 350, 121, 251))
        self.gridLayoutWidget_13.setObjectName("gridLayoutWidget_13")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.trainimage_10 = QtWidgets.QLabel(self.gridLayoutWidget_13)
        self.trainimage_10.setObjectName("trainimage_10")
        self.gridLayout_13.addWidget(self.trainimage_10, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(1370, 280, 121, 71))
        self.label_10.setObjectName("label_10")
        self.gridLayoutWidget_14 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_14.setGeometry(QtCore.QRect(1510, 350, 121, 251))
        self.gridLayoutWidget_14.setObjectName("gridLayoutWidget_14")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.trainimage_11 = QtWidgets.QLabel(self.gridLayoutWidget_14)
        self.trainimage_11.setObjectName("trainimage_11")
        self.gridLayout_14.addWidget(self.trainimage_11, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(1510, 280, 121, 71))
        self.label_11.setObjectName("label_11")
        self.gridLayoutWidget_15 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_15.setGeometry(QtCore.QRect(1650, 350, 121, 251))
        self.gridLayoutWidget_15.setObjectName("gridLayoutWidget_15")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.gridLayoutWidget_15)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.trainimage_12 = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.trainimage_12.setObjectName("trainimage_12")
        self.gridLayout_15.addWidget(self.trainimage_12, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(1650, 280, 121, 71))
        self.label_12.setObjectName("label_12")
        self.result_button = QtWidgets.QPushButton(self.frame)
        self.result_button.setGeometry(QtCore.QRect(10, 180, 71, 81))
        self.result_button.setObjectName("result_button")
        self.json_button = QtWidgets.QPushButton(self.frame)
        self.json_button.setGeometry(QtCore.QRect(10, 270, 71, 81))
        self.json_button.setObjectName("json_button")
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.trainimage_8.setText(_translate("Form", "TextLabel"))
        self.gotobutton.setText(_translate("Form", "Goto"))
        self.trainimage_6.setText(_translate("Form", "TextLabel"))
        self.trainimage_4.setText(_translate("Form", "TextLabel"))
        self.showmetrics.setText(_translate("Form", "Show Metrics"))
        self.trainimage_7.setText(_translate("Form", "TextLabel"))
        self.label_5.setText(_translate("Form", "TextLabel"))
        self.trainimage_5.setText(_translate("Form", "TextLabel"))
        self.nextbutton.setText(_translate("Form", "Next"))
        self.label_9.setText(_translate("Form", "TextLabel"))
        self.trainimage_3.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.totaledit_label.setText(_translate("Form", "Total Edit "))
        self.trainimage_2.setText(_translate("Form", "TextLabel"))
        self.label_6.setText(_translate("Form", "TextLabel"))
        self.train.setText(_translate("Form", "Train/Retrain"))
        self.label_8.setText(_translate("Form", "TextLabel"))
        self.trainimage_9.setText(_translate("Form", "TextLabel"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.showerror.setText(_translate("Form", "Show Errors"))
        self.previousbutton.setText(_translate("Form", "Previous"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.validimage.setText(_translate("Form", "TextLabel"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_7.setText(_translate("Form", "TextLabel"))
        self.valid_label.setText(_translate("Form", "TextLabel"))
        self.trainimage.setText(_translate("Form", "TextLabel"))
        self.trainimage_10.setText(_translate("Form", "TextLabel"))
        self.label_10.setText(_translate("Form", "TextLabel"))
        self.trainimage_11.setText(_translate("Form", "TextLabel"))
        self.label_11.setText(_translate("Form", "TextLabel"))
        self.trainimage_12.setText(_translate("Form", "TextLabel"))
        self.label_12.setText(_translate("Form", "TextLabel"))
        self.result_button.setText(_translate("Form", "Result path"))
        self.json_button.setText(_translate("Form", "Json path"))

