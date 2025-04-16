# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'administrative.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 648)
        icon = QIcon(QIcon.fromTheme(u"go-home"))
        MainWindow.setWindowIcon(icon)
        self.actionMuokkaa = QAction(MainWindow)
        self.actionMuokkaa.setObjectName(u"actionMuokkaa")
        self.actionTietoja_ohjelmasta = QAction(MainWindow)
        self.actionTietoja_ohjelmasta.setObjectName(u"actionTietoja_ohjelmasta")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 671, 591))
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.tabWidget.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.lenderTab = QWidget()
        self.lenderTab.setObjectName(u"lenderTab")
        self.lenderTab.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.registeredPersonsTableWidget = QTableWidget(self.lenderTab)
        if (self.registeredPersonsTableWidget.columnCount() < 6):
            self.registeredPersonsTableWidget.setColumnCount(6)
        if (self.registeredPersonsTableWidget.rowCount() < 10):
            self.registeredPersonsTableWidget.setRowCount(10)
        self.registeredPersonsTableWidget.setObjectName(u"registeredPersonsTableWidget")
        self.registeredPersonsTableWidget.setGeometry(QRect(10, 230, 641, 321))
        self.registeredPersonsTableWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ForbiddenCursor))
        self.registeredPersonsTableWidget.setRowCount(10)
        self.registeredPersonsTableWidget.setColumnCount(6)
        self.registeredPersonLabel = QLabel(self.lenderTab)
        self.registeredPersonLabel.setObjectName(u"registeredPersonLabel")
        self.registeredPersonLabel.setGeometry(QRect(10, 210, 141, 16))
        font = QFont()
        font.setPointSize(10)
        self.registeredPersonLabel.setFont(font)
        self.savePersonPushButton = QPushButton(self.lenderTab)
        self.savePersonPushButton.setObjectName(u"savePersonPushButton")
        self.savePersonPushButton.setGeometry(QRect(270, 173, 75, 25))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.savePersonPushButton.setFont(font1)
        self.savePersonPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.savePersonPushButton.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.layoutWidget = QWidget(self.lenderTab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 11, 244, 188))
        self.lenderGridLayout = QGridLayout(self.layoutWidget)
        self.lenderGridLayout.setObjectName(u"lenderGridLayout")
        self.lenderGridLayout.setContentsMargins(0, 0, 0, 0)
        self.ssnLabel = QLabel(self.layoutWidget)
        self.ssnLabel.setObjectName(u"ssnLabel")
        self.ssnLabel.setFont(font)

        self.lenderGridLayout.addWidget(self.ssnLabel, 0, 0, 1, 1)

        self.ssnLineEdit = QLineEdit(self.layoutWidget)
        self.ssnLineEdit.setObjectName(u"ssnLineEdit")
        font2 = QFont()
        font2.setPointSize(11)
        self.ssnLineEdit.setFont(font2)

        self.lenderGridLayout.addWidget(self.ssnLineEdit, 0, 1, 1, 1)

        self.firstNameLabel = QLabel(self.layoutWidget)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        self.firstNameLabel.setFont(font)

        self.lenderGridLayout.addWidget(self.firstNameLabel, 1, 0, 1, 1)

        self.firstNameLineEdit = QLineEdit(self.layoutWidget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")
        self.firstNameLineEdit.setFont(font2)

        self.lenderGridLayout.addWidget(self.firstNameLineEdit, 1, 1, 1, 1)

        self.lastNameLabel = QLabel(self.layoutWidget)
        self.lastNameLabel.setObjectName(u"lastNameLabel")
        self.lastNameLabel.setFont(font)

        self.lenderGridLayout.addWidget(self.lastNameLabel, 2, 0, 1, 1)

        self.lastNameLineEdit = QLineEdit(self.layoutWidget)
        self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")
        self.lastNameLineEdit.setFont(font2)

        self.lenderGridLayout.addWidget(self.lastNameLineEdit, 2, 1, 1, 1)

        self.groupLabel = QLabel(self.layoutWidget)
        self.groupLabel.setObjectName(u"groupLabel")
        self.groupLabel.setFont(font)

        self.lenderGridLayout.addWidget(self.groupLabel, 3, 0, 1, 1)

        self.groupComboBox = QComboBox(self.layoutWidget)
        self.groupComboBox.setObjectName(u"groupComboBox")
        self.groupComboBox.setFont(font2)

        self.lenderGridLayout.addWidget(self.groupComboBox, 3, 1, 1, 1)

        self.vehicleClassLabel = QLabel(self.layoutWidget)
        self.vehicleClassLabel.setObjectName(u"vehicleClassLabel")
        self.vehicleClassLabel.setFont(font)

        self.lenderGridLayout.addWidget(self.vehicleClassLabel, 4, 0, 1, 1)

        self.vehicleClassLineEdit = QLineEdit(self.layoutWidget)
        self.vehicleClassLineEdit.setObjectName(u"vehicleClassLineEdit")
        self.vehicleClassLineEdit.setFont(font2)

        self.lenderGridLayout.addWidget(self.vehicleClassLineEdit, 4, 1, 1, 1)

        self.emailLabel = QLabel(self.layoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setFont(font)

        self.lenderGridLayout.addWidget(self.emailLabel, 5, 0, 1, 1)

        self.emailLineEdit = QLineEdit(self.layoutWidget)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setFont(font2)

        self.lenderGridLayout.addWidget(self.emailLineEdit, 5, 1, 1, 1)

        self.tabWidget.addTab(self.lenderTab, "")
        self.vehicleTab = QWidget()
        self.vehicleTab.setObjectName(u"vehicleTab")
        self.layoutWidget1 = QWidget(self.vehicleTab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 252, 156))
        self.vehicleGridLayout = QGridLayout(self.layoutWidget1)
        self.vehicleGridLayout.setObjectName(u"vehicleGridLayout")
        self.vehicleGridLayout.setContentsMargins(0, 0, 0, 0)
        self.licensePlateNumberLabel = QLabel(self.layoutWidget1)
        self.licensePlateNumberLabel.setObjectName(u"licensePlateNumberLabel")
        self.licensePlateNumberLabel.setFont(font)

        self.vehicleGridLayout.addWidget(self.licensePlateNumberLabel, 0, 0, 1, 1)

        self.licensePlateNumberLineEdit = QLineEdit(self.layoutWidget1)
        self.licensePlateNumberLineEdit.setObjectName(u"licensePlateNumberLineEdit")
        self.licensePlateNumberLineEdit.setFont(font2)

        self.vehicleGridLayout.addWidget(self.licensePlateNumberLineEdit, 0, 1, 1, 1)

        self.manufacturerLabel = QLabel(self.layoutWidget1)
        self.manufacturerLabel.setObjectName(u"manufacturerLabel")
        self.manufacturerLabel.setFont(font)

        self.vehicleGridLayout.addWidget(self.manufacturerLabel, 1, 0, 1, 1)

        self.manufacturerLineEdit = QLineEdit(self.layoutWidget1)
        self.manufacturerLineEdit.setObjectName(u"manufacturerLineEdit")
        self.manufacturerLineEdit.setFont(font2)

        self.vehicleGridLayout.addWidget(self.manufacturerLineEdit, 1, 1, 1, 1)

        self.modelLabel = QLabel(self.layoutWidget1)
        self.modelLabel.setObjectName(u"modelLabel")
        self.modelLabel.setFont(font)

        self.vehicleGridLayout.addWidget(self.modelLabel, 2, 0, 1, 1)

        self.modelLineEdit = QLineEdit(self.layoutWidget1)
        self.modelLineEdit.setObjectName(u"modelLineEdit")
        self.modelLineEdit.setFont(font2)

        self.vehicleGridLayout.addWidget(self.modelLineEdit, 2, 1, 1, 1)

        self.modelYearLabel = QLabel(self.layoutWidget1)
        self.modelYearLabel.setObjectName(u"modelYearLabel")
        self.modelYearLabel.setFont(font)

        self.vehicleGridLayout.addWidget(self.modelYearLabel, 3, 0, 1, 1)

        self.modelYearLineEdit = QLineEdit(self.layoutWidget1)
        self.modelYearLineEdit.setObjectName(u"modelYearLineEdit")
        self.modelYearLineEdit.setFont(font2)

        self.vehicleGridLayout.addWidget(self.modelYearLineEdit, 3, 1, 1, 1)

        self.capacityLabel = QLabel(self.layoutWidget1)
        self.capacityLabel.setObjectName(u"capacityLabel")
        self.capacityLabel.setFont(font)

        self.vehicleGridLayout.addWidget(self.capacityLabel, 4, 0, 1, 1)

        self.capacityLineEdit = QLineEdit(self.layoutWidget1)
        self.capacityLineEdit.setObjectName(u"capacityLineEdit")
        self.capacityLineEdit.setFont(font2)

        self.vehicleGridLayout.addWidget(self.capacityLineEdit, 4, 1, 1, 1)

        self.saveVehiclePushButton = QPushButton(self.vehicleTab)
        self.saveVehiclePushButton.setObjectName(u"saveVehiclePushButton")
        self.saveVehiclePushButton.setGeometry(QRect(280, 140, 75, 25))
        self.saveVehiclePushButton.setFont(font1)
        self.saveVehiclePushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.saveVehiclePushButton.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.printBarcodePushButton = QPushButton(self.vehicleTab)
        self.printBarcodePushButton.setObjectName(u"printBarcodePushButton")
        self.printBarcodePushButton.setGeometry(QRect(280, 110, 75, 25))
        self.printBarcodePushButton.setFont(font1)
        self.printBarcodePushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.printBarcodePushButton.setStyleSheet(u"background-color: rgb(217, 149, 39);\n"
"color: rgb(255, 255, 255);")
        self.vehicleCatalogTableWidget = QTableWidget(self.vehicleTab)
        if (self.vehicleCatalogTableWidget.columnCount() < 5):
            self.vehicleCatalogTableWidget.setColumnCount(5)
        if (self.vehicleCatalogTableWidget.rowCount() < 10):
            self.vehicleCatalogTableWidget.setRowCount(10)
        self.vehicleCatalogTableWidget.setObjectName(u"vehicleCatalogTableWidget")
        self.vehicleCatalogTableWidget.setGeometry(QRect(10, 230, 541, 321))
        font3 = QFont()
        font3.setPointSize(9)
        self.vehicleCatalogTableWidget.setFont(font3)
        self.vehicleCatalogTableWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ForbiddenCursor))
        self.vehicleCatalogTableWidget.setRowCount(10)
        self.vehicleCatalogTableWidget.setColumnCount(5)
        self.carListLabel = QLabel(self.vehicleTab)
        self.carListLabel.setObjectName(u"carListLabel")
        self.carListLabel.setGeometry(QRect(15, 210, 111, 16))
        self.carListLabel.setFont(font)
        self.tabWidget.addTab(self.vehicleTab, "")
        self.groupTab = QWidget()
        self.groupTab.setObjectName(u"groupTab")
        self.saveGroupPushButton = QPushButton(self.groupTab)
        self.saveGroupPushButton.setObjectName(u"saveGroupPushButton")
        self.saveGroupPushButton.setGeometry(QRect(280, 45, 75, 25))
        self.saveGroupPushButton.setFont(font1)
        self.saveGroupPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.saveGroupPushButton.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.savedGroupsTableWidget = QTableWidget(self.groupTab)
        if (self.savedGroupsTableWidget.columnCount() < 2):
            self.savedGroupsTableWidget.setColumnCount(2)
        if (self.savedGroupsTableWidget.rowCount() < 10):
            self.savedGroupsTableWidget.setRowCount(10)
        self.savedGroupsTableWidget.setObjectName(u"savedGroupsTableWidget")
        self.savedGroupsTableWidget.setGeometry(QRect(10, 130, 241, 201))
        self.savedGroupsTableWidget.setFont(font2)
        self.savedGroupsTableWidget.setRowCount(10)
        self.savedGroupsTableWidget.setColumnCount(2)
        self.savedGroupsLabel = QLabel(self.groupTab)
        self.savedGroupsLabel.setObjectName(u"savedGroupsLabel")
        self.savedGroupsLabel.setGeometry(QRect(10, 100, 121, 24))
        self.savedGroupsLabel.setFont(font)
        self.layoutWidget2 = QWidget(self.groupTab)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(11, 11, 237, 60))
        self.groupGridLayout = QGridLayout(self.layoutWidget2)
        self.groupGridLayout.setObjectName(u"groupGridLayout")
        self.groupGridLayout.setContentsMargins(0, 0, 0, 0)
        self.groupNameLabel = QLabel(self.layoutWidget2)
        self.groupNameLabel.setObjectName(u"groupNameLabel")
        self.groupNameLabel.setFont(font)

        self.groupGridLayout.addWidget(self.groupNameLabel, 0, 0, 1, 1)

        self.groupNameLineEdit = QLineEdit(self.layoutWidget2)
        self.groupNameLineEdit.setObjectName(u"groupNameLineEdit")
        self.groupNameLineEdit.setFont(font2)

        self.groupGridLayout.addWidget(self.groupNameLineEdit, 0, 1, 1, 1)

        self.responsiblePersonLabel = QLabel(self.layoutWidget2)
        self.responsiblePersonLabel.setObjectName(u"responsiblePersonLabel")
        self.responsiblePersonLabel.setFont(font)

        self.groupGridLayout.addWidget(self.responsiblePersonLabel, 1, 0, 1, 1)

        self.responsiblePersonLineEdit = QLineEdit(self.layoutWidget2)
        self.responsiblePersonLineEdit.setObjectName(u"responsiblePersonLineEdit")
        self.responsiblePersonLineEdit.setFont(font2)

        self.groupGridLayout.addWidget(self.responsiblePersonLineEdit, 1, 1, 1, 1)

        self.tabWidget.addTab(self.groupTab, "")
        self.reportsTab = QWidget()
        self.reportsTab.setObjectName(u"reportsTab")
        self.reportComboBox = QComboBox(self.reportsTab)
        self.reportComboBox.setObjectName(u"reportComboBox")
        self.reportComboBox.setGeometry(QRect(10, 40, 241, 22))
        self.reportComboBox.setFont(font2)
        self.reportLabel = QLabel(self.reportsTab)
        self.reportLabel.setObjectName(u"reportLabel")
        self.reportLabel.setGeometry(QRect(10, 20, 71, 16))
        self.reportLabel.setFont(font)
        self.startDateEdit = QDateEdit(self.reportsTab)
        self.startDateEdit.setObjectName(u"startDateEdit")
        self.startDateEdit.setGeometry(QRect(10, 110, 110, 22))
        self.startDateEdit.setFont(font2)
        self.startDateEdit.setCalendarPopup(True)
        self.startDateEdit.setDate(QDate(2025, 1, 1))
        self.startLabel = QLabel(self.reportsTab)
        self.startLabel.setObjectName(u"startLabel")
        self.startLabel.setGeometry(QRect(10, 90, 71, 16))
        self.startLabel.setFont(font)
        self.endLabel = QLabel(self.reportsTab)
        self.endLabel.setObjectName(u"endLabel")
        self.endLabel.setGeometry(QRect(140, 90, 71, 16))
        self.endLabel.setFont(font)
        self.endDateEdit = QDateEdit(self.reportsTab)
        self.endDateEdit.setObjectName(u"endDateEdit")
        self.endDateEdit.setGeometry(QRect(140, 110, 110, 22))
        self.endDateEdit.setFont(font2)
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setDate(QDate(2025, 1, 1))
        self.reportPrintPushButton = QPushButton(self.reportsTab)
        self.reportPrintPushButton.setObjectName(u"reportPrintPushButton")
        self.reportPrintPushButton.setGeometry(QRect(260, 110, 75, 25))
        self.reportPrintPushButton.setFont(font1)
        self.reportPrintPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reportPrintPushButton.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.previewTableWidget = QTableWidget(self.reportsTab)
        if (self.previewTableWidget.columnCount() < 6):
            self.previewTableWidget.setColumnCount(6)
        if (self.previewTableWidget.rowCount() < 22):
            self.previewTableWidget.setRowCount(22)
        self.previewTableWidget.setObjectName(u"previewTableWidget")
        self.previewTableWidget.setGeometry(QRect(10, 210, 641, 321))
        self.previewTableWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ForbiddenCursor))
        self.previewTableWidget.setRowCount(22)
        self.previewTableWidget.setColumnCount(6)
        self.previewLabel = QLabel(self.reportsTab)
        self.previewLabel.setObjectName(u"previewLabel")
        self.previewLabel.setGeometry(QRect(10, 190, 71, 16))
        self.previewLabel.setFont(font)
        self.tabWidget.addTab(self.reportsTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuAsetukset = QMenu(self.menubar)
        self.menuAsetukset.setObjectName(u"menuAsetukset")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAsetukset.menuAction())
        self.menuAsetukset.addAction(self.actionMuokkaa)
        self.menuAsetukset.addAction(self.actionTietoja_ohjelmasta)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionMuokkaa.setText(QCoreApplication.translate("MainWindow", u"Muokkaa...", None))
#if QT_CONFIG(tooltip)
        self.actionMuokkaa.setToolTip(QCoreApplication.translate("MainWindow", u"Muokkaa ohjelman asetuksia", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionMuokkaa.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionTietoja_ohjelmasta.setText(QCoreApplication.translate("MainWindow", u"Tietoja ohjelmasta...", None))
#if QT_CONFIG(shortcut)
        self.actionTietoja_ohjelmasta.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+T", None))
#endif // QT_CONFIG(shortcut)
        self.registeredPersonLabel.setText(QCoreApplication.translate("MainWindow", u"Rekister\u00f6idyt lainaajat", None))
        self.savePersonPushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.ssnLabel.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6tunnus", None))
        self.firstNameLabel.setText(QCoreApplication.translate("MainWindow", u"Etunimi", None))
        self.lastNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi", None))
        self.groupLabel.setText(QCoreApplication.translate("MainWindow", u"Ryhm\u00e4", None))
        self.groupComboBox.setCurrentText("")
        self.vehicleClassLabel.setText(QCoreApplication.translate("MainWindow", u"Ajokorttiluokka", None))
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"S\u00e4hk\u00f6posti", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lenderTab), QCoreApplication.translate("MainWindow", u"Lainaajat", None))
        self.licensePlateNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Rekisterinumero", None))
        self.manufacturerLabel.setText(QCoreApplication.translate("MainWindow", u"Merkki", None))
        self.modelLabel.setText(QCoreApplication.translate("MainWindow", u"Malli", None))
        self.modelYearLabel.setText(QCoreApplication.translate("MainWindow", u"Vuosimalli", None))
        self.capacityLabel.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6m\u00e4\u00e4r\u00e4", None))
        self.saveVehiclePushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.printBarcodePushButton.setText(QCoreApplication.translate("MainWindow", u"Viivakoodi", None))
        self.carListLabel.setText(QCoreApplication.translate("MainWindow", u"Autoluettelo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vehicleTab), QCoreApplication.translate("MainWindow", u"Autot", None))
        self.saveGroupPushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.savedGroupsLabel.setText(QCoreApplication.translate("MainWindow", u"Tallennetut ryhm\u00e4t", None))
        self.groupNameLabel.setText(QCoreApplication.translate("MainWindow", u"Ryhm\u00e4n nimi", None))
        self.responsiblePersonLabel.setText(QCoreApplication.translate("MainWindow", u"Vastuuhenkil\u00f6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.groupTab), QCoreApplication.translate("MainWindow", u"Ryhm\u00e4t", None))
        self.reportLabel.setText(QCoreApplication.translate("MainWindow", u"Raportti", None))
        self.startDateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"d/M/yyyy", None))
        self.startLabel.setText(QCoreApplication.translate("MainWindow", u"Alkaa", None))
        self.endLabel.setText(QCoreApplication.translate("MainWindow", u"P\u00e4\u00e4ttyy", None))
        self.endDateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"d/M/yyyy", None))
        self.reportPrintPushButton.setText(QCoreApplication.translate("MainWindow", u"Tulosta", None))
        self.previewLabel.setText(QCoreApplication.translate("MainWindow", u"Esikatselu", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reportsTab), QCoreApplication.translate("MainWindow", u"Raportit", None))
        self.menuAsetukset.setTitle(QCoreApplication.translate("MainWindow", u"Asetukset", None))
    # retranslateUi

