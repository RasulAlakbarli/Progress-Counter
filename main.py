import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QApplication

from UI.screen_1_ui import Ui_Dialog_1
from UI.screen_2_ui import Ui_Dialog_2


class MainWindow(QDialog, Ui_Dialog_1, Ui_Dialog_2):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pb_start.clicked.connect(self.action)

        self.second_window = Screen_2()


    def action(self):
        self.name = self.item_name.text()
        self.count = self.item_count.text()


        if not self.name:
            self.label_3.setText("Please enter item name!")
        else:
            self.label_3.setText("✅")

        if not self.count:
            self.label_4.setText("Please enter item count!")
        else:
            self.label_4.setText("✅")
        
        if self.name and self.count:
            widget.setCurrentIndex(widget.currentIndex()+1)

    def passinfo(self):
        self.second_window.lcd_target_count.display(int(self.count))



class Screen_2(QDialog, Ui_Dialog_2):
    def __init__(self):
        super(Screen_2, self).__init__()
        self.setupUi(self) 
        self.pb_back.clicked.connect(self.goback)
        self.pb_minus.clicked.connect(self.substract)
        self.pb_plus.clicked.connect(self.add)
        self.pb_reset.clicked.connect(self.reset)

        self.lcd_target_count = QtWidgets.QLCDNumber()


    def goback(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
    
    def substract(self):
        old_value = self.lcd_current_count.value()
        new_value = old_value-1
        if new_value >= 0:
            self.lcd_current_count.display(new_value)

    def add(self):
        old_value = self.lcd_current_count.value()
        new_value = old_value+1
        if new_value >= 0:
            self.lcd_current_count.display(new_value)

    def reset(self):
        self.lcd_current_count.display(0)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = MainWindow()
    screen_2 = Screen_2()
    widget.addWidget(mainwindow)
    widget.addWidget(screen_2)
    widget.setMinimumHeight(320)
    widget.setMinimumWidth(480)
    widget.show()
    
    sys.exit(app.exec())