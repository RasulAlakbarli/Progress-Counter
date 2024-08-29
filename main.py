import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QApplication

from UI.screen_2_ui import Ui_Dialog_2
from UI.main_window_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.second_window = Screen_2()1

        self.pb_start.clicked.connect(self.passInfo)

    def passInfo(self):
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

        self.second_window.l_text.setText(f"{self.name} Count")
        self.second_window.lcd_target_count.display(self.count)
        self.second_window.displayInfo()



class Screen_2(QDialog, Ui_Dialog_2):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.pb_minus.clicked.connect(self.substract)
        self.pb_plus.clicked.connect(self.add)
        self.pb_reset.clicked.connect(self.reset)
    
    def substract(self):
        old_value = self.lcd_curernt_count.value()
        if old_value-1 >= 0:
            new_value = old_value-1
            self.lcd_curernt_count.display(new_value)
        
        if new_value != self.lcd_target_count.value():
            self.l_final.setText("")

    def add(self):
        old_value = self.lcd_curernt_count.value()
        
        if old_value+1 <= self.lcd_target_count.value():
            new_value = old_value+1
            self.lcd_curernt_count.display(new_value)
        
        if new_value == self.lcd_target_count.value():
            self.l_final.setText("Congratulations, you reached your goal!!!")

    def reset(self):
        self.lcd_curernt_count.display(0)
    
    def displayInfo(self):
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setMinimumHeight(320)
    window.setMinimumWidth(480)
    window.show()

    sys.exit(app.exec_())