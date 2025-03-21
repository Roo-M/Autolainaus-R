# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'saveSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.saveSettingsPushButton = QPushButton(self.centralwidget)
        self.saveSettingsPushButton.setObjectName(u"saveSettingsPushButton")
        self.saveSettingsPushButton.setGeometry(QRect(160, 160, 75, 23))
        font = QFont()
        font.setPointSize(11)
        self.saveSettingsPushButton.setFont(font)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(12, 12, 225, 136))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.serverLabel = QLabel(self.layoutWidget)
        self.serverLabel.setObjectName(u"serverLabel")
        font1 = QFont()
        font1.setPointSize(10)
        self.serverLabel.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.serverLabel)

        self.serverLineEdit = QLineEdit(self.layoutWidget)
        self.serverLineEdit.setObjectName(u"serverLineEdit")
        self.serverLineEdit.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.serverLineEdit)

        self.portLabel = QLabel(self.layoutWidget)
        self.portLabel.setObjectName(u"portLabel")
        self.portLabel.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.portLabel)

        self.portLineEdit = QLineEdit(self.layoutWidget)
        self.portLineEdit.setObjectName(u"portLineEdit")
        self.portLineEdit.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.portLineEdit)

        self.databaseLabel = QLabel(self.layoutWidget)
        self.databaseLabel.setObjectName(u"databaseLabel")
        self.databaseLabel.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.databaseLabel)

        self.databaseLineEdit = QLineEdit(self.layoutWidget)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")
        self.databaseLineEdit.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.databaseLineEdit)

        self.userLabel = QLabel(self.layoutWidget)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.userLabel)

        self.userLineEdit = QLineEdit(self.layoutWidget)
        self.userLineEdit.setObjectName(u"userLineEdit")
        self.userLineEdit.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.userLineEdit)

        self.passwordLabel = QLabel(self.layoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self.layoutWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setFont(font1)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.passwordLineEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.saveSettingsPushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Tallentaa asetukset tiedostoon</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.saveSettingsPushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.serverLabel.setText(QCoreApplication.translate("MainWindow", u"Palvelin", None))
#if QT_CONFIG(tooltip)
        self.serverLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Palvelimen nimi tai IP-osoite</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.portLabel.setText(QCoreApplication.translate("MainWindow", u"Portti", None))
#if QT_CONFIG(tooltip)
        self.portLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Palvelimen porttinumero</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.databaseLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokanta", None))
#if QT_CONFIG(tooltip)
        self.databaseLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Tietokannan nimi</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.userLabel.setText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
#if QT_CONFIG(tooltip)
        self.userLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Sovelluksen k\u00e4ytt\u00e4j\u00e4tunnus</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Salasana", None))
#if QT_CONFIG(tooltip)
        self.passwordLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Salasana</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

