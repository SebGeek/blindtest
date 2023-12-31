# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quizz_master_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 452)
        self.TeamBlue = QLabel(Dialog)
        self.TeamBlue.setObjectName(u"TeamBlue")
        self.TeamBlue.setGeometry(QRect(20, 20, 141, 51))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.TeamBlue.setFont(font)
        self.TeamBlue.setStyleSheet(u"color: blue")
        self.fastestTeam = QLabel(Dialog)
        self.fastestTeam.setObjectName(u"fastestTeam")
        self.fastestTeam.setGeometry(QRect(10, 190, 381, 41))
        font1 = QFont()
        font1.setPointSize(23)
        self.fastestTeam.setFont(font1)
        self.fastestTeam.setStyleSheet(u"color: red")
        self.fastestTeam.setAlignment(Qt.AlignCenter)
        self.TeamRed = QLabel(Dialog)
        self.TeamRed.setObjectName(u"TeamRed")
        self.TeamRed.setGeometry(QRect(210, 20, 171, 51))
        self.TeamRed.setFont(font)
        self.TeamRed.setStyleSheet(u"color: red")
        self.ScoreBlue = QLabel(Dialog)
        self.ScoreBlue.setObjectName(u"ScoreBlue")
        self.ScoreBlue.setGeometry(QRect(40, 70, 71, 51))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.ScoreBlue.setFont(font2)
        self.ScoreBlue.setStyleSheet(u"color: blue")
        self.ScoreBlue.setAlignment(Qt.AlignCenter)
        self.ScoreRed = QLabel(Dialog)
        self.ScoreRed.setObjectName(u"ScoreRed")
        self.ScoreRed.setGeometry(QRect(250, 70, 81, 51))
        self.ScoreRed.setFont(font2)
        self.ScoreRed.setStyleSheet(u"color: red")
        self.ScoreRed.setAlignment(Qt.AlignCenter)
        self.pushButton_blueteam_plus1 = QPushButton(Dialog)
        self.pushButton_blueteam_plus1.setObjectName(u"pushButton_blueteam_plus1")
        self.pushButton_blueteam_plus1.setGeometry(QRect(10, 330, 71, 51))
        font3 = QFont()
        font3.setPointSize(20)
        self.pushButton_blueteam_plus1.setFont(font3)
        self.pushButton_blueteam_plus1.setStyleSheet(u"color: blue")
        self.pushButton_blueteam_minus1 = QPushButton(Dialog)
        self.pushButton_blueteam_minus1.setObjectName(u"pushButton_blueteam_minus1")
        self.pushButton_blueteam_minus1.setGeometry(QRect(10, 400, 31, 31))
        font4 = QFont()
        font4.setPointSize(12)
        self.pushButton_blueteam_minus1.setFont(font4)
        self.pushButton_blueteam_minus1.setStyleSheet(u"color: blue")
        self.pushButton_redteam_plus1 = QPushButton(Dialog)
        self.pushButton_redteam_plus1.setObjectName(u"pushButton_redteam_plus1")
        self.pushButton_redteam_plus1.setGeometry(QRect(240, 330, 71, 51))
        self.pushButton_redteam_plus1.setFont(font3)
        self.pushButton_redteam_plus1.setStyleSheet(u"color: red")
        self.pushButton_redteam_minus1 = QPushButton(Dialog)
        self.pushButton_redteam_minus1.setObjectName(u"pushButton_redteam_minus1")
        self.pushButton_redteam_minus1.setGeometry(QRect(240, 400, 31, 31))
        self.pushButton_redteam_minus1.setFont(font4)
        self.pushButton_redteam_minus1.setStyleSheet(u"color: red")
        self.pushButton_blueteam_plus3 = QPushButton(Dialog)
        self.pushButton_blueteam_plus3.setObjectName(u"pushButton_blueteam_plus3")
        self.pushButton_blueteam_plus3.setGeometry(QRect(90, 330, 71, 51))
        self.pushButton_blueteam_plus3.setFont(font3)
        self.pushButton_blueteam_plus3.setStyleSheet(u"color: blue")
        self.pushButton_redteam_plus3 = QPushButton(Dialog)
        self.pushButton_redteam_plus3.setObjectName(u"pushButton_redteam_plus3")
        self.pushButton_redteam_plus3.setGeometry(QRect(320, 330, 71, 51))
        self.pushButton_redteam_plus3.setFont(font3)
        self.pushButton_redteam_plus3.setStyleSheet(u"color: red")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.TeamBlue.setText(QCoreApplication.translate("Dialog", u"Equipe Mayo", None))
        self.fastestTeam.setText(QCoreApplication.translate("Dialog", u"Ketchup est le plus rapide !", None))
        self.TeamRed.setText(QCoreApplication.translate("Dialog", u"Equipe Ketchup", None))
        self.ScoreBlue.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.ScoreRed.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.pushButton_blueteam_plus1.setText(QCoreApplication.translate("Dialog", u"+1", None))
        self.pushButton_blueteam_minus1.setText(QCoreApplication.translate("Dialog", u"-1", None))
        self.pushButton_redteam_plus1.setText(QCoreApplication.translate("Dialog", u"+1", None))
        self.pushButton_redteam_minus1.setText(QCoreApplication.translate("Dialog", u"-1", None))
        self.pushButton_blueteam_plus3.setText(QCoreApplication.translate("Dialog", u"+3", None))
        self.pushButton_redteam_plus3.setText(QCoreApplication.translate("Dialog", u"+3", None))
    # retranslateUi

