# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screen_2.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLCDNumber, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_2(object):
    def setupUi(self, Dialog_2):
        if not Dialog_2.objectName():
            Dialog_2.setObjectName(u"Dialog_2")
        Dialog_2.resize(562, 439)
        self.gridLayout = QGridLayout(Dialog_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(Dialog_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.l_text = QLabel(self.groupBox_2)
        self.l_text.setObjectName(u"l_text")
        font = QFont()
        font.setPointSize(35)
        self.l_text.setFont(font)
        self.l_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.l_text, 1, 0, 1, 3)

        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lcd_curernt_count = QLCDNumber(self.groupBox)
        self.lcd_curernt_count.setObjectName(u"lcd_curernt_count")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcd_curernt_count.sizePolicy().hasHeightForWidth())
        self.lcd_curernt_count.setSizePolicy(sizePolicy)
        self.lcd_curernt_count.setFrameShape(QFrame.Shape.NoFrame)
        self.lcd_curernt_count.setLineWidth(1)

        self.horizontalLayout.addWidget(self.lcd_curernt_count)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(50)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.lcd_target_count = QLCDNumber(self.groupBox)
        self.lcd_target_count.setObjectName(u"lcd_target_count")
        sizePolicy.setHeightForWidth(self.lcd_target_count.sizePolicy().hasHeightForWidth())
        self.lcd_target_count.setSizePolicy(sizePolicy)
        self.lcd_target_count.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lcd_target_count.setFrameShape(QFrame.Shape.NoFrame)
        self.lcd_target_count.setSmallDecimalPoint(False)
        self.lcd_target_count.setProperty("value", 0.000000000000000)

        self.horizontalLayout.addWidget(self.lcd_target_count)


        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 3)

        self.pb_reset = QPushButton(self.groupBox_2)
        self.pb_reset.setObjectName(u"pb_reset")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pb_reset.sizePolicy().hasHeightForWidth())
        self.pb_reset.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(13)
        font2.setWeight(QFont.Light)
        self.pb_reset.setFont(font2)
        self.pb_reset.setAutoDefault(True)
        self.pb_reset.setFlat(False)

        self.gridLayout_2.addWidget(self.pb_reset, 4, 0, 1, 1)

        self.pb_plus = QPushButton(self.groupBox_2)
        self.pb_plus.setObjectName(u"pb_plus")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pb_plus.sizePolicy().hasHeightForWidth())
        self.pb_plus.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(15)
        font3.setWeight(QFont.ExtraBold)
        self.pb_plus.setFont(font3)

        self.gridLayout_2.addWidget(self.pb_plus, 4, 2, 1, 1)

        self.pb_minus = QPushButton(self.groupBox_2)
        self.pb_minus.setObjectName(u"pb_minus")
        sizePolicy3.setHeightForWidth(self.pb_minus.sizePolicy().hasHeightForWidth())
        self.pb_minus.setSizePolicy(sizePolicy3)
        self.pb_minus.setFont(font3)

        self.gridLayout_2.addWidget(self.pb_minus, 4, 1, 1, 1)

        self.l_final = QLabel(self.groupBox_2)
        self.l_final.setObjectName(u"l_final")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.l_final.sizePolicy().hasHeightForWidth())
        self.l_final.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.l_final, 3, 0, 1, 3)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)


        self.retranslateUi(Dialog_2)

        self.pb_reset.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog_2)
    # setupUi

    def retranslateUi(self, Dialog_2):
        Dialog_2.setWindowTitle(QCoreApplication.translate("Dialog_2", u"screen_2", None))
        self.groupBox_2.setTitle("")
        self.l_text.setText(QCoreApplication.translate("Dialog_2", u"Customer Count: ", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Dialog_2", u"/", None))
        self.pb_reset.setText(QCoreApplication.translate("Dialog_2", u"Reset", None))
        self.pb_plus.setText(QCoreApplication.translate("Dialog_2", u"+", None))
        self.pb_minus.setText(QCoreApplication.translate("Dialog_2", u"-", None))
        self.l_final.setText("")
    # retranslateUi

