#!/usr/bin/env python3
from xlrd  import open_workbook
from lottery_draw import Ui_Form
import sys
import random
import time
import os.path
from PyQt5.QtCore import QThread, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets

NAME_SET = set()


def get_all_names():
    p_path = os.path.split(os.path.realpath(__file__))[0]
    table = open_workbook(p_path + '/test.xlsx').sheet_by_index(0)
    for cell in table.col_values(0):
        if not cell:
            break
        NAME_SET.add(cell.strip())

class Py_Select(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super(Py_Select, self).__init__()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("BST_lucky_draw")

    def init(self):
        get_all_names()
        self.name_list = list(NAME_SET)
        self.textBrowser.setText('')
        self.start.clicked.connect(self._start)
        self.stop.clicked.connect(self._stop)
        self.index = 0
        self.prize_count = 0
        self.lottery_count = 0
        self.timer = None

    def _start(self):
        self.prize_count = self.prize_count + 1
        self.start.setHidden(True)
        self.stop.setHidden(False)
        self.name_list = list(NAME_SET)
        random.seed(int(time.time()))
        random.shuffle(self.name_list)

        if not self.timer:
            self.timer = QTimer()
        self.timer.timeout.connect(self._range_name)
        self.timer.start(50)

    def _range_name(self):
        # self.index += 1
        # if self.index >= len(self.name_list):
            # self.index = 0
        # self.textBrowser.setText(self.name_list[self.index])
        winner = random.choice(self.name_list)
        self.textBrowser.setText(winner)
        
    def _range_10times(self):
        winner = random.choice(self.name_list)
        self.textBrowser.setText(winner)
        self.lottery_count = self.lottery_count + 1
        NAME_SET.discard(self.textBrowser.toPlainText().strip())
        if self.prize_count == 6:
            self.firstprize.insertPlainText(self.textBrowser.toPlainText() + "\n")
        else:
            self.secondprize.insertPlainText(self.textBrowser.toPlainText() + "\n")
        
        if self.lottery_count > 9:
            if self.timer:
                self.timer.stop()
            self.start.setHidden(False)
            self.lottery_count = 0
    
    def _stop(self):       
        if self.timer:
            self.timer.stop()
            NAME_SET.discard(self.textBrowser.toPlainText().strip())
            
            self.lottery_count = self.lottery_count + 1
            
            if self.prize_count == 6:
                self.firstprize.insertPlainText(self.textBrowser.toPlainText() + "\n")
            else:
                self.secondprize.insertPlainText(self.textBrowser.toPlainText() + "\n")
            
            if not self.timer:
                self.timer = QTimer()
            self.timer.timeout.connect(self._range_10times)
            self.timer.start(500)
            # self.timer.start(500)
            # self.name_list = list(NAME_SET)
            # random.seed(int(time.time()))
            # random.shuffle(self.name_list)

            # if not self.timer:
                # self.timer = QTimer()
            # self.timer.timeout.connect(self._range_name)
            # self.timer.start(500)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = Py_Select()
    myshow.show()
    sys.exit(app.exec_())