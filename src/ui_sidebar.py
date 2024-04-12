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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(872, 619)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
"	background-color:#F5FAFE;\n"
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
        self.groupBox_form = QGroupBox(self.dashboard_page)
        self.groupBox_form.setObjectName(u"groupBox_form")
        self.groupBox_form.setGeometry(QRect(0, 0, 631, 250))
        self.groupBox_form.setStyleSheet(u"color:black;\n"
"")
        self.layoutWidget = QWidget(self.groupBox_form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 26, 619, 214))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.fechaLabel = QLabel(self.layoutWidget)
        self.fechaLabel.setObjectName(u"fechaLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.fechaLabel)

        self.kc_19_1_5Label = QLabel(self.layoutWidget)
        self.kc_19_1_5Label.setObjectName(u"kc_19_1_5Label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.kc_19_1_5Label)

        self.kc_19_1_5LineEdit = QLineEdit(self.layoutWidget)
        self.kc_19_1_5LineEdit.setObjectName(u"kc_19_1_5LineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.kc_19_1_5LineEdit)

        self.ema_12Label = QLabel(self.layoutWidget)
        self.ema_12Label.setObjectName(u"ema_12Label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.ema_12Label)

        self.ema_12LineEdit = QLineEdit(self.layoutWidget)
        self.ema_12LineEdit.setObjectName(u"ema_12LineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ema_12LineEdit)

        self.ema_24Label = QLabel(self.layoutWidget)
        self.ema_24Label.setObjectName(u"ema_24Label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.ema_24Label)

        self.ema_24LineEdit = QLineEdit(self.layoutWidget)
        self.ema_24LineEdit.setObjectName(u"ema_24LineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.ema_24LineEdit)

        self.rSILabel = QLabel(self.layoutWidget)
        self.rSILabel.setObjectName(u"rSILabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.rSILabel)

        self.rsiLineEdit = QLineEdit(self.layoutWidget)
        self.rsiLineEdit.setObjectName(u"rsiLineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.rsiLineEdit)

        self.sma_14Label = QLabel(self.layoutWidget)
        self.sma_14Label.setObjectName(u"sma_14Label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.sma_14Label)

        self.sma_14LineEdit = QLineEdit(self.layoutWidget)
        self.sma_14LineEdit.setObjectName(u"sma_14LineEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.sma_14LineEdit)

        self.patronesVelaLabel = QLabel(self.layoutWidget)
        self.patronesVelaLabel.setObjectName(u"patronesVelaLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.patronesVelaLabel)

        self.patronesVelaLineEdit = QLineEdit(self.layoutWidget)
        self.patronesVelaLineEdit.setObjectName(u"patronesVelaLineEdit")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.patronesVelaLineEdit)

        self.fechaLineEdit = QDateTimeEdit(self.layoutWidget)
        self.fechaLineEdit.setObjectName(u"fechaLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fechaLineEdit)


        self.horizontalLayout_5.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.volumenOperacionesLabel = QLabel(self.layoutWidget)
        self.volumenOperacionesLabel.setObjectName(u"volumenOperacionesLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.volumenOperacionesLabel)

        self.volumenOperacionesLineEdit = QLineEdit(self.layoutWidget)
        self.volumenOperacionesLineEdit.setObjectName(u"volumenOperacionesLineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.volumenOperacionesLineEdit)

        self.nSoporteResistenciaLabel = QLabel(self.layoutWidget)
        self.nSoporteResistenciaLabel.setObjectName(u"nSoporteResistenciaLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.nSoporteResistenciaLabel)

        self.nSoporteResistenciaLineEdit = QLineEdit(self.layoutWidget)
        self.nSoporteResistenciaLineEdit.setObjectName(u"nSoporteResistenciaLineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.nSoporteResistenciaLineEdit)

        self.indicadorVolumenLabel = QLabel(self.layoutWidget)
        self.indicadorVolumenLabel.setObjectName(u"indicadorVolumenLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.indicadorVolumenLabel)

        self.indicadorVolumenLineEdit = QLineEdit(self.layoutWidget)
        self.indicadorVolumenLineEdit.setObjectName(u"indicadorVolumenLineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.indicadorVolumenLineEdit)

        self.analisisDireccionMercadoLabel = QLabel(self.layoutWidget)
        self.analisisDireccionMercadoLabel.setObjectName(u"analisisDireccionMercadoLabel")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.analisisDireccionMercadoLabel)

        self.analisisDireccionMercadoLineEdit = QLineEdit(self.layoutWidget)
        self.analisisDireccionMercadoLineEdit.setObjectName(u"analisisDireccionMercadoLineEdit")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.analisisDireccionMercadoLineEdit)

        self.direcciNMercadoLabel = QLabel(self.layoutWidget)
        self.direcciNMercadoLabel.setObjectName(u"direcciNMercadoLabel")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.direcciNMercadoLabel)

        self.direccionMercadoLineEdit = QLineEdit(self.layoutWidget)
        self.direccionMercadoLineEdit.setObjectName(u"direccionMercadoLineEdit")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.direccionMercadoLineEdit)

        self.cambioPorcentualLabel = QLabel(self.layoutWidget)
        self.cambioPorcentualLabel.setObjectName(u"cambioPorcentualLabel")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.cambioPorcentualLabel)

        self.cambioPorcentualLineEdit = QLineEdit(self.layoutWidget)
        self.cambioPorcentualLineEdit.setObjectName(u"cambioPorcentualLineEdit")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.cambioPorcentualLineEdit)


        self.horizontalLayout_5.addLayout(self.formLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.addNew = QPushButton(self.layoutWidget)
        self.addNew.setObjectName(u"addNew")

        self.horizontalLayout_5.addWidget(self.addNew)

        self.table = QTableWidget(self.dashboard_page)
        if (self.table.columnCount() < 13):
            self.table.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(0, 350, 631, 201))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setStyleSheet(u"color:black;\n"
"")
        self.table.setRowCount(0)
        self.table.setColumnCount(13)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setMinimumSectionSize(32)
        self.table.horizontalHeader().setDefaultSectionSize(150)
        self.table.verticalHeader().setMinimumSectionSize(24)
        self.table.verticalHeader().setStretchLastSection(False)
        self.groupBox_buttons = QGroupBox(self.dashboard_page)
        self.groupBox_buttons.setObjectName(u"groupBox_buttons")
        self.groupBox_buttons.setGeometry(QRect(9, 260, 631, 81))
        self.groupBox_buttons.setStyleSheet(u"color:black;")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_buttons)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.loadData = QPushButton(self.groupBox_buttons)
        self.loadData.setObjectName(u"loadData")

        self.horizontalLayout_6.addWidget(self.loadData)

        self.callData = QPushButton(self.groupBox_buttons)
        self.callData.setObjectName(u"callData")

        self.horizontalLayout_6.addWidget(self.callData)

        self.uploadData = QPushButton(self.groupBox_buttons)
        self.uploadData.setObjectName(u"uploadData")

        self.horizontalLayout_6.addWidget(self.uploadData)

        self.deleteData = QPushButton(self.groupBox_buttons)
        self.deleteData.setObjectName(u"deleteData")

        self.horizontalLayout_6.addWidget(self.deleteData)

        self.stackedWidget.addWidget(self.dashboard_page)
        self.messages_page = QWidget()
        self.messages_page.setObjectName(u"messages_page")
        self.label_5 = QLabel(self.messages_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 190, 221, 121))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color:black;\n"
"")
        self.stackedWidget.addWidget(self.messages_page)
        self.notifications_page = QWidget()
        self.notifications_page.setObjectName(u"notifications_page")
        self.label_6 = QLabel(self.notifications_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(230, 140, 221, 121))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color:black;\n"
"")
        self.stackedWidget.addWidget(self.notifications_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.label_8 = QLabel(self.settings_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(180, 180, 211, 81))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color:black;\n"
"")
        self.stackedWidget.addWidget(self.settings_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.label_7 = QLabel(self.profile_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(240, 170, 151, 121))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color:black;\n"
"")
        self.stackedWidget.addWidget(self.profile_page)

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
        self.groupBox_form.setTitle(QCoreApplication.translate("MainWindow", u"Add New Trade", None))
        self.fechaLabel.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.kc_19_1_5Label.setText(QCoreApplication.translate("MainWindow", u"kc_19_1_5", None))
        self.ema_12Label.setText(QCoreApplication.translate("MainWindow", u"ema_12", None))
        self.ema_24Label.setText(QCoreApplication.translate("MainWindow", u"ema_24", None))
        self.rSILabel.setText(QCoreApplication.translate("MainWindow", u"RSI", None))
        self.sma_14Label.setText(QCoreApplication.translate("MainWindow", u"sma_14", None))
        self.patronesVelaLabel.setText(QCoreApplication.translate("MainWindow", u"patrones vela", None))
        self.volumenOperacionesLabel.setText(QCoreApplication.translate("MainWindow", u"Volumen operaciones", None))
        self.nSoporteResistenciaLabel.setText(QCoreApplication.translate("MainWindow", u"N Soporte/Resistencia", None))
        self.indicadorVolumenLabel.setText(QCoreApplication.translate("MainWindow", u"Indicador volumen", None))
        self.analisisDireccionMercadoLabel.setText(QCoreApplication.translate("MainWindow", u"An\u00e0lisis direcci\u00f2n mercado", None))
        self.direcciNMercadoLabel.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f2n mercado", None))
        self.cambioPorcentualLabel.setText(QCoreApplication.translate("MainWindow", u"cambio porcentual", None))
        self.addNew.setText(QCoreApplication.translate("MainWindow", u"Add new tarde", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"kc_19_1_5", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ema_12", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ema_24", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"rsi", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"sma_14", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Volumen operaciones", None));
        ___qtablewidgetitem7 = self.table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Patrones vela", None));
        ___qtablewidgetitem8 = self.table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"N Soporte/Resistencia", None));
        ___qtablewidgetitem9 = self.table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Indicador volumen", None));
        ___qtablewidgetitem10 = self.table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"An\u00e0lsis mercado", None));
        ___qtablewidgetitem11 = self.table.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f2n mercado", None));
        ___qtablewidgetitem12 = self.table.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Cambio porcentual", None));
        self.groupBox_buttons.setTitle(QCoreApplication.translate("MainWindow", u"Manage Data", None))
        self.loadData.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.callData.setText(QCoreApplication.translate("MainWindow", u"Extrac Data", None))
        self.uploadData.setText(QCoreApplication.translate("MainWindow", u"Upload Data", None))
        self.deleteData.setText(QCoreApplication.translate("MainWindow", u"Delete Data", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Messages Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Notifications Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Settings Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Profile Page", None))
    # retranslateUi
