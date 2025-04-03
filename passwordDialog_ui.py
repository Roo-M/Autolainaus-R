# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(284, 115)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(14, 10, 261, 56))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.oldPasswordLabel = QLabel(self.layoutWidget)
        self.oldPasswordLabel.setObjectName(u"oldPasswordLabel")
        font = QFont()
        font.setPointSize(10)
        self.oldPasswordLabel.setFont(font)

        self.gridLayout.addWidget(self.oldPasswordLabel, 0, 0, 1, 1)

        self.oldPasswordLineEdit = QLineEdit(self.layoutWidget)
        self.oldPasswordLineEdit.setObjectName(u"oldPasswordLineEdit")
        font1 = QFont()
        font1.setPointSize(11)
        self.oldPasswordLineEdit.setFont(font1)
        self.oldPasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.oldPasswordLineEdit, 0, 1, 1, 1)

        self.newPasswordLabel = QLabel(self.layoutWidget)
        self.newPasswordLabel.setObjectName(u"newPasswordLabel")
        self.newPasswordLabel.setFont(font)

        self.gridLayout.addWidget(self.newPasswordLabel, 1, 0, 1, 1)

        self.newPasswordLineEdit = QLineEdit(self.layoutWidget)
        self.newPasswordLineEdit.setObjectName(u"newPasswordLineEdit")
        self.newPasswordLineEdit.setFont(font1)
        self.newPasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.newPasswordLineEdit, 1, 1, 1, 1)

        self.savePasswordPushButton = QPushButton(Dialog)
        self.savePasswordPushButton.setObjectName(u"savePasswordPushButton")
        self.savePasswordPushButton.setEnabled(False)
        self.savePasswordPushButton.setGeometry(QRect(200, 80, 70, 25))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.savePasswordPushButton.setFont(font2)
        self.savePasswordPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.savePasswordPushButton.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.oldPasswordLabel.setText(QCoreApplication.translate("Dialog", u"Vanha salasana", None))
#if QT_CONFIG(tooltip)
        self.oldPasswordLineEdit.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Salasana</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.newPasswordLabel.setText(QCoreApplication.translate("Dialog", u"Uusi salasana", None))
#if QT_CONFIG(tooltip)
        self.newPasswordLineEdit.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Salasana</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.savePasswordPushButton.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Tallentaa asetukset tiedostoon</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.savePasswordPushButton.setText(QCoreApplication.translate("Dialog", u"Tallenna", None))
    # retranslateUi

