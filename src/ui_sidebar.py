# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(962, 619)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 100, 30))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 100, 30))
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 100, 30))
        self.gridLayout_4 = QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 0, 100, 30))
        self.gridLayout_5 = QGridLayout(self.layoutWidget3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	text-align:left;\n"
"	height:30px;\n"
"	padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:#F5FAFE;;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/images/profile_pic.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:white;")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_name_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        icon = QIcon()
        icon.addFile(u":/images/dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/dashboard.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_2.setIcon(icon)
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_2)

        self.profile_2 = QPushButton(self.icon_name_widget)
        self.profile_2.setObjectName(u"profile_2")
        icon1 = QIcon()
        icon1.addFile(u":/images/profile_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/profile.png", QSize(), QIcon.Normal, QIcon.On)
        self.profile_2.setIcon(icon1)
        self.profile_2.setCheckable(True)
        self.profile_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.profile_2)

        self.messages_2 = QPushButton(self.icon_name_widget)
        self.messages_2.setObjectName(u"messages_2")
        icon2 = QIcon()
        icon2.addFile(u":/images/messages_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/messages.png", QSize(), QIcon.Normal, QIcon.On)
        self.messages_2.setIcon(icon2)
        self.messages_2.setCheckable(True)
        self.messages_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.messages_2)

        self.notifications_2 = QPushButton(self.icon_name_widget)
        self.notifications_2.setObjectName(u"notifications_2")
        icon3 = QIcon()
        icon3.addFile(u":/images/notifications_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/images/notifications.png", QSize(), QIcon.Normal, QIcon.On)
        self.notifications_2.setIcon(icon3)
        self.notifications_2.setCheckable(True)
        self.notifications_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.notifications_2)

        self.settings_2 = QPushButton(self.icon_name_widget)
        self.settings_2.setObjectName(u"settings_2")
        icon4 = QIcon()
        icon4.addFile(u":/images/settings_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/settings.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_2.setIcon(icon4)
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settings_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 263, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushButton_13 = QPushButton(self.icon_name_widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        icon5 = QIcon()
        icon5.addFile(u":/images/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon5)
        self.pushButton_13.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_13)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	height:30px;\n"
"	border:none;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:#F5FAFE;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/images/profile_pic.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_1)

        self.profile_1 = QPushButton(self.icon_only_widget)
        self.profile_1.setObjectName(u"profile_1")
        self.profile_1.setIcon(icon1)
        self.profile_1.setCheckable(True)
        self.profile_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.profile_1)

        self.messages_1 = QPushButton(self.icon_only_widget)
        self.messages_1.setObjectName(u"messages_1")
        self.messages_1.setIcon(icon2)
        self.messages_1.setCheckable(True)
        self.messages_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.messages_1)

        self.notifications_1 = QPushButton(self.icon_only_widget)
        self.notifications_1.setObjectName(u"notifications_1")
        self.notifications_1.setIcon(icon3)
        self.notifications_1.setCheckable(True)
        self.notifications_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.notifications_1)

        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        self.settings_1.setIcon(icon4)
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settings_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 263, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.pushButton_6 = QPushButton(self.icon_only_widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu = QPushButton(self.header_widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u":/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon6)
        self.menu.setIconSize(QSize(20, 20))
        self.menu.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.menu)

        self.horizontalSpacer_2 = QSpacerItem(38, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"boder:0,5px black;")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_20 = QPushButton(self.header_widget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        icon7 = QIcon()
        icon7.addFile(u":/images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_20.setIcon(icon7)

        self.horizontalLayout.addWidget(self.pushButton_20)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(189, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_21 = QPushButton(self.header_widget)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setStyleSheet(u"border:none;")
        icon8 = QIcon()
        icon8.addFile(u":/images/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_21.setIcon(icon8)

        self.horizontalLayout_4.addWidget(self.pushButton_21)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.label_4 = QLabel(self.dashboard_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 20, 401, 16))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: black;\n"
"")
        self.label_5 = QLabel(self.dashboard_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(38, 50, 411, 20))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: black;\n"
"")
        self.label_9 = QLabel(self.dashboard_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 80, 181, 20))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color: black;\n"
"")
        self.stackedWidget.addWidget(self.dashboard_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.label_7 = QLabel(self.profile_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(240, 170, 151, 121))
        font3 = QFont()
        font3.setPointSize(20)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color:black;\n"
"")
        self.stackedWidget.addWidget(self.profile_page)
        self.messages_page = QWidget()
        self.messages_page.setObjectName(u"messages_page")
        self.groupBox_buttons_2 = QGroupBox(self.messages_page)
        self.groupBox_buttons_2.setObjectName(u"groupBox_buttons_2")
        self.groupBox_buttons_2.setGeometry(QRect(9, 260, 671, 81))
        self.groupBox_buttons_2.setStyleSheet(u"color:black;")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_buttons_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.loadData_2 = QPushButton(self.groupBox_buttons_2)
        self.loadData_2.setObjectName(u"loadData_2")

        self.horizontalLayout_7.addWidget(self.loadData_2)

        self.callData_2 = QPushButton(self.groupBox_buttons_2)
        self.callData_2.setObjectName(u"callData_2")

        self.horizontalLayout_7.addWidget(self.callData_2)

        self.uploadData_2 = QPushButton(self.groupBox_buttons_2)
        self.uploadData_2.setObjectName(u"uploadData_2")

        self.horizontalLayout_7.addWidget(self.uploadData_2)

        self.deleteData_2 = QPushButton(self.groupBox_buttons_2)
        self.deleteData_2.setObjectName(u"deleteData_2")

        self.horizontalLayout_7.addWidget(self.deleteData_2)

        self.groupBox_form_2 = QGroupBox(self.messages_page)
        self.groupBox_form_2.setObjectName(u"groupBox_form_2")
        self.groupBox_form_2.setGeometry(QRect(0, 0, 681, 251))
        self.groupBox_form_2.setStyleSheet(u"color:black;\n"
"")
        self.layoutWidget_2 = QWidget(self.groupBox_form_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 26, 651, 220))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.fechaLabel_2 = QLabel(self.layoutWidget_2)
        self.fechaLabel_2.setObjectName(u"fechaLabel_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.fechaLabel_2)

        self.fecha_LineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.fecha_LineEdit_2.setObjectName(u"fecha_LineEdit_2")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.fecha_LineEdit_2)

        self.kc_19_1_5Label_2 = QLabel(self.layoutWidget_2)
        self.kc_19_1_5Label_2.setObjectName(u"kc_19_1_5Label_2")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.kc_19_1_5Label_2)

        self.kc_19_1_5LineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.kc_19_1_5LineEdit_2.setObjectName(u"kc_19_1_5LineEdit_2")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.kc_19_1_5LineEdit_2)

        self.ema_12Label_2 = QLabel(self.layoutWidget_2)
        self.ema_12Label_2.setObjectName(u"ema_12Label_2")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.ema_12Label_2)

        self.ema_12LineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.ema_12LineEdit_2.setObjectName(u"ema_12LineEdit_2")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.ema_12LineEdit_2)

        self.ema_24Label_2 = QLabel(self.layoutWidget_2)
        self.ema_24Label_2.setObjectName(u"ema_24Label_2")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.ema_24Label_2)

        self.ema_24LineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.ema_24LineEdit_2.setObjectName(u"ema_24LineEdit_2")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.ema_24LineEdit_2)

        self.rSILabel_2 = QLabel(self.layoutWidget_2)
        self.rSILabel_2.setObjectName(u"rSILabel_2")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.rSILabel_2)

        self.rsiLineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.rsiLineEdit_2.setObjectName(u"rsiLineEdit_2")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.rsiLineEdit_2)

        self.sma_14Label_2 = QLabel(self.layoutWidget_2)
        self.sma_14Label_2.setObjectName(u"sma_14Label_2")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.sma_14Label_2)

        self.sma_14LineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.sma_14LineEdit_2.setObjectName(u"sma_14LineEdit_2")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.sma_14LineEdit_2)

        self.coin_2 = QLabel(self.layoutWidget_2)
        self.coin_2.setObjectName(u"coin_2")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.coin_2)

        self.coin_LineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.coin_LineEdit_2.setObjectName(u"coin_LineEdit_2")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.coin_LineEdit_2)


        self.horizontalLayout_8.addLayout(self.formLayout_3)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.volumenOperacionesLabel_2 = QLabel(self.layoutWidget_2)
        self.volumenOperacionesLabel_2.setObjectName(u"volumenOperacionesLabel_2")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.volumenOperacionesLabel_2)

        self.volumenOperacionesLineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.volumenOperacionesLineEdit_2.setObjectName(u"volumenOperacionesLineEdit_2")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.volumenOperacionesLineEdit_2)

        self.nSoporteResistenciaLabel_2 = QLabel(self.layoutWidget_2)
        self.nSoporteResistenciaLabel_2.setObjectName(u"nSoporteResistenciaLabel_2")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.nSoporteResistenciaLabel_2)

        self.nSoporteResistenciaLineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.nSoporteResistenciaLineEdit_2.setObjectName(u"nSoporteResistenciaLineEdit_2")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.nSoporteResistenciaLineEdit_2)

        self.indicadorVolumenLabel_2 = QLabel(self.layoutWidget_2)
        self.indicadorVolumenLabel_2.setObjectName(u"indicadorVolumenLabel_2")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.indicadorVolumenLabel_2)

        self.indicadorVolumenLineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.indicadorVolumenLineEdit_2.setObjectName(u"indicadorVolumenLineEdit_2")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.indicadorVolumenLineEdit_2)

        self.analisisDireccionMercadoLabel_2 = QLabel(self.layoutWidget_2)
        self.analisisDireccionMercadoLabel_2.setObjectName(u"analisisDireccionMercadoLabel_2")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.analisisDireccionMercadoLabel_2)

        self.analisisDireccionMercadoLineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.analisisDireccionMercadoLineEdit_2.setObjectName(u"analisisDireccionMercadoLineEdit_2")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.analisisDireccionMercadoLineEdit_2)

        self.direcciNMercadoLabel_2 = QLabel(self.layoutWidget_2)
        self.direcciNMercadoLabel_2.setObjectName(u"direcciNMercadoLabel_2")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.direcciNMercadoLabel_2)

        self.direccionMercadoLineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.direccionMercadoLineEdit_2.setObjectName(u"direccionMercadoLineEdit_2")

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.direccionMercadoLineEdit_2)

        self.cambioPorcentualLabel_2 = QLabel(self.layoutWidget_2)
        self.cambioPorcentualLabel_2.setObjectName(u"cambioPorcentualLabel_2")

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.cambioPorcentualLabel_2)

        self.cambioPorcentualLineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.cambioPorcentualLineEdit_2.setObjectName(u"cambioPorcentualLineEdit_2")

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.cambioPorcentualLineEdit_2)

        self.patronesVelaLabel_2 = QLabel(self.layoutWidget_2)
        self.patronesVelaLabel_2.setObjectName(u"patronesVelaLabel_2")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.patronesVelaLabel_2)

        self.patronesVelaLineEdit_2 = QLineEdit(self.layoutWidget_2)
        self.patronesVelaLineEdit_2.setObjectName(u"patronesVelaLineEdit_2")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.patronesVelaLineEdit_2)


        self.horizontalLayout_8.addLayout(self.formLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.addNew_2 = QPushButton(self.layoutWidget_2)
        self.addNew_2.setObjectName(u"addNew_2")

        self.horizontalLayout_8.addWidget(self.addNew_2)

        self.table_2 = QTableWidget(self.messages_page)
        if (self.table_2.columnCount() < 14):
            self.table_2.setColumnCount(14)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_2.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        self.table_2.setObjectName(u"table_2")
        self.table_2.setGeometry(QRect(0, 350, 681, 201))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_2.sizePolicy().hasHeightForWidth())
        self.table_2.setSizePolicy(sizePolicy)
        self.table_2.setStyleSheet(u"color:black;\n"
"")
        self.table_2.setRowCount(0)
        self.table_2.setColumnCount(14)
        self.table_2.horizontalHeader().setVisible(True)
        self.table_2.horizontalHeader().setCascadingSectionResizes(False)
        self.table_2.horizontalHeader().setMinimumSectionSize(32)
        self.table_2.horizontalHeader().setDefaultSectionSize(150)
        self.table_2.verticalHeader().setMinimumSectionSize(24)
        self.table_2.verticalHeader().setStretchLastSection(False)
        self.stackedWidget.addWidget(self.messages_page)
        self.notifications_page = QWidget()
        self.notifications_page.setObjectName(u"notifications_page")
        self.label_6 = QLabel(self.notifications_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(230, 140, 221, 121))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color:black;\n"
"")
        self.stackedWidget.addWidget(self.notifications_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.label_8 = QLabel(self.settings_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(180, 180, 211, 81))
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color:black;\n"
"")
        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.settings_1.toggled.connect(self.settings_2.setChecked)
        self.dashboard_1.toggled.connect(self.dashboard_2.setChecked)
        self.profile_1.toggled.connect(self.profile_2.setChecked)
        self.messages_1.toggled.connect(self.messages_2.setChecked)
        self.notifications_1.toggled.connect(self.notifications_2.setChecked)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.profile_2.toggled.connect(self.profile_1.setChecked)
        self.messages_2.toggled.connect(self.messages_1.setChecked)
        self.notifications_2.toggled.connect(self.notifications_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.pushButton_6.toggled.connect(MainWindow.close)
        self.pushButton_13.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sidebar", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.profile_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.messages_2.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.notifications_2.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Sing Out", None))
        self.label.setText("")
        self.dashboard_1.setText("")
        self.profile_1.setText("")
        self.messages_1.setText("")
        self.notifications_1.setText("")
        self.settings_1.setText("")
        self.pushButton_6.setText("")
        self.menu.setText("")
        self.pushButton_20.setText("")
        self.pushButton_21.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Most Popular Programming Languages", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Some commonly recognized programming languages that frequently appear", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"In list of top languages include", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Profile Page", None))
        self.groupBox_buttons_2.setTitle(QCoreApplication.translate("MainWindow", u"Manage Data", None))
        self.loadData_2.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.callData_2.setText(QCoreApplication.translate("MainWindow", u"Extrac Data", None))
        self.uploadData_2.setText(QCoreApplication.translate("MainWindow", u"Upload Data", None))
        self.deleteData_2.setText(QCoreApplication.translate("MainWindow", u"Delete Data", None))
        self.groupBox_form_2.setTitle(QCoreApplication.translate("MainWindow", u"Add New Trade", None))
        self.fechaLabel_2.setText(QCoreApplication.translate("MainWindow", u"Fecha (dd/mm/yyyy)", None))
        self.kc_19_1_5Label_2.setText(QCoreApplication.translate("MainWindow", u"kc_19_1_5", None))
        self.ema_12Label_2.setText(QCoreApplication.translate("MainWindow", u"ema_12", None))
        self.ema_24Label_2.setText(QCoreApplication.translate("MainWindow", u"ema_24", None))
        self.rSILabel_2.setText(QCoreApplication.translate("MainWindow", u"RSI", None))
        self.sma_14Label_2.setText(QCoreApplication.translate("MainWindow", u"sma_14", None))
        self.coin_2.setText(QCoreApplication.translate("MainWindow", u"Coin", None))
        self.volumenOperacionesLabel_2.setText(QCoreApplication.translate("MainWindow", u"Volumen operaciones", None))
        self.nSoporteResistenciaLabel_2.setText(QCoreApplication.translate("MainWindow", u"N Soporte/Resistencia", None))
        self.indicadorVolumenLabel_2.setText(QCoreApplication.translate("MainWindow", u"Indicador volumen", None))
        self.analisisDireccionMercadoLabel_2.setText(QCoreApplication.translate("MainWindow", u"An\u00e0lisis direcci\u00f2n mercado", None))
        self.direcciNMercadoLabel_2.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f2n mercado", None))
        self.cambioPorcentualLabel_2.setText(QCoreApplication.translate("MainWindow", u"cambio porcentual", None))
        self.patronesVelaLabel_2.setText(QCoreApplication.translate("MainWindow", u"patrones vela", None))
        self.addNew_2.setText(QCoreApplication.translate("MainWindow", u"Add new tarde", None))
        ___qtablewidgetitem = self.table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Fecha (dd/mm/yyyy)", None));
        ___qtablewidgetitem1 = self.table_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Coin", None));
        ___qtablewidgetitem2 = self.table_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"kc_19_1_5", None));
        ___qtablewidgetitem3 = self.table_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ema_12", None));
        ___qtablewidgetitem4 = self.table_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ema_24", None));
        ___qtablewidgetitem5 = self.table_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"rsi", None));
        ___qtablewidgetitem6 = self.table_2.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"sma_14", None));
        ___qtablewidgetitem7 = self.table_2.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Patrones vela", None));
        ___qtablewidgetitem8 = self.table_2.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Volumen operaciones", None));
        ___qtablewidgetitem9 = self.table_2.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"N Soporte/Resistencia", None));
        ___qtablewidgetitem10 = self.table_2.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Indicador volumen", None));
        ___qtablewidgetitem11 = self.table_2.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"An\u00e0lsis mercado", None));
        ___qtablewidgetitem12 = self.table_2.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f2n mercado", None));
        ___qtablewidgetitem13 = self.table_2.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Cambio porcentual", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Notifications Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Settings Page", None))
    # retranslateUi

