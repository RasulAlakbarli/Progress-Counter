# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screen_1.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog_1(object):
    def setupUi(self, Dialog_1):
        if not Dialog_1.objectName():
            Dialog_1.setObjectName(u"Dialog_1")
        Dialog_1.resize(577, 439)
        self.gridLayout = QGridLayout(Dialog_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Dialog_1)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.item_name = QLineEdit(self.groupBox)
        self.item_name.setObjectName(u"item_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.item_name)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.item_count = QLineEdit(self.groupBox)
        self.item_count.setObjectName(u"item_count")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.item_count)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_4)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.pb_start = QPushButton(Dialog_1)
        self.pb_start.setObjectName(u"pb_start")

        self.gridLayout.addWidget(self.pb_start, 2, 0, 1, 1)


        self.retranslateUi(Dialog_1)

        QMetaObject.connectSlotsByName(Dialog_1)
    # setupUi

    def retranslateUi(self, Dialog_1):
        Dialog_1.setWindowTitle(QCoreApplication.translate("Dialog_1", u"screen_1", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Dialog_1", u"Name of tracked item:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_1", u"Target count: ", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.pb_start.setText(QCoreApplication.translate("Dialog_1", u"Start", None))
    # retranslateUi

