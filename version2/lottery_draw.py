# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lottery_draw.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1032, 782)
        Form.setStyleSheet("")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(50, 50, 256, 192))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setMouseTracking(False)
        self.textBrowser.setStyleSheet("background-color: rgb(170, 85, 0);\n"
"font: 81 16pt \"Rockwell Extra Bold\";")
        self.textBrowser.setObjectName("textBrowser")
        self.start = QtWidgets.QPushButton(Form)
        self.start.setGeometry(QtCore.QRect(310, 50, 93, 28))
        self.start.setStyleSheet("background-color: rgb(255, 153, 69);\n"
"font: 10pt \"Bosch Script\";")
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(Form)
        self.stop.setGeometry(QtCore.QRect(310, 90, 91, 31))
        self.stop.setStyleSheet("background-color: rgb(255, 153, 69);\n"
"font: 10pt \"Bosch Script\";")
        self.stop.setObjectName("stop")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1031, 781))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("bst.ppm"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.firstprize = QtWidgets.QTextBrowser(Form)
        self.firstprize.setGeometry(QtCore.QRect(450, 50, 151, 271))
        self.firstprize.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.firstprize.setObjectName("firstprize")
        self.secondprize = QtWidgets.QTextBrowser(Form)
        self.secondprize.setGeometry(QtCore.QRect(635, 50, 261, 691))
        self.secondprize.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.secondprize.setObjectName("secondprize")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(450, 10, 151, 41))
        self.label_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 10pt \"Bosch Script\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(630, 10, 261, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 10pt \"Bosch Script\";")
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.firstprize.raise_()
        self.textBrowser.raise_()
        self.start.raise_()
        self.stop.raise_()
        self.secondprize.raise_()
        self.label_2.raise_()
        self.label_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell Extra Bold\'; font-size:16pt; font-weight:80; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>"))
        self.start.setText(_translate("Form", "Start"))
        self.stop.setText(_translate("Form", "stop"))
        self.label_2.setText(_translate("Form", "First Prize"))
        self.label_3.setText(_translate("Form", "Second Prize"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
