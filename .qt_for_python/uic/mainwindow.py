# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1200, 700)
        Form.setMinimumSize(QSize(1200, 700))
        Form.setMaximumSize(QSize(1200, 700))
        Form.setMouseTracking(False)
        Form.setAutoFillBackground(False)
        self.account = QWidget(Form)
        self.account.setObjectName(u"account")
        self.account.setGeometry(QRect(20, 10, 341, 671))
        self.account.setCursor(QCursor(Qt.ArrowCursor))
        self.account.setMouseTracking(False)
        self.account.setAutoFillBackground(True)
        self.l2 = QLabel(self.account)
        self.l2.setObjectName(u"l2")
        self.l2.setGeometry(QRect(110, 40, 121, 31))
        self.l2.setAlignment(Qt.AlignCenter)
        self.l3 = QLabel(self.account)
        self.l3.setObjectName(u"l3")
        self.l3.setGeometry(QRect(10, 130, 61, 31))
        self.l4 = QLabel(self.account)
        self.l4.setObjectName(u"l4")
        self.l4.setGeometry(QRect(10, 200, 61, 31))
        self.l5 = QLabel(self.account)
        self.l5.setObjectName(u"l5")
        self.l5.setGeometry(QRect(10, 270, 71, 31))
        self.l1 = QLabel(self.account)
        self.l1.setObjectName(u"l1")
        self.l1.setGeometry(QRect(10, 340, 71, 31))
        self.userName = QLineEdit(self.account)
        self.userName.setObjectName(u"userName")
        self.userName.setGeometry(QRect(120, 270, 211, 31))
        self.password = QLineEdit(self.account)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(120, 340, 211, 31))
        self.userState = QLabel(self.account)
        self.userState.setObjectName(u"userState")
        self.userState.setGeometry(QRect(120, 130, 171, 31))
        self.userIdentity = QLabel(self.account)
        self.userIdentity.setObjectName(u"userIdentity")
        self.userIdentity.setGeometry(QRect(120, 200, 171, 31))
        self.logoutBtn = QPushButton(self.account)
        self.logoutBtn.setObjectName(u"logoutBtn")
        self.logoutBtn.setGeometry(QRect(230, 430, 101, 41))
        self.loginBtn = QPushButton(self.account)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(10, 430, 101, 41))
        self.registBtn = QPushButton(self.account)
        self.registBtn.setObjectName(u"registBtn")
        self.registBtn.setGeometry(QRect(120, 430, 101, 41))
        self.info = QWidget(Form)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(380, 10, 811, 671))
        self.label = QLabel(self.info)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 40, 171, 31))
        self.label.setAlignment(Qt.AlignCenter)
        self.queue = QWidget(self.info)
        self.queue.setObjectName(u"queue")
        self.queue.setGeometry(QRect(10, 110, 381, 241))
        self.label_2 = QLabel(self.queue)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 141, 41))
        self.queueBtn = QPushButton(self.queue)
        self.queueBtn.setObjectName(u"queueBtn")
        self.queueBtn.setGeometry(QRect(280, 10, 91, 41))
        self.queueTable = QTableWidget(self.queue)
        if (self.queueTable.columnCount() < 8):
            self.queueTable.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.queueTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.queueTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.queueTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.queueTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.queueTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.queueTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.queueTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.queueTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.queueTable.setObjectName(u"queueTable")
        self.queueTable.setGeometry(QRect(10, 60, 361, 171))
        self.pileStateSearch = QWidget(self.info)
        self.pileStateSearch.setObjectName(u"pileStateSearch")
        self.pileStateSearch.setGeometry(QRect(420, 110, 371, 241))
        self.label_3 = QLabel(self.pileStateSearch)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 171, 41))
        self.pileStateBtn = QPushButton(self.pileStateSearch)
        self.pileStateBtn.setObjectName(u"pileStateBtn")
        self.pileStateBtn.setGeometry(QRect(270, 10, 91, 41))
        self.pileStateTable = QTableWidget(self.pileStateSearch)
        if (self.pileStateTable.columnCount() < 5):
            self.pileStateTable.setColumnCount(5)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.pileStateTable.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.pileStateTable.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.pileStateTable.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.pileStateTable.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.pileStateTable.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        self.pileStateTable.setObjectName(u"pileStateTable")
        self.pileStateTable.setGeometry(QRect(10, 60, 351, 171))
        self.pileList = QWidget(self.info)
        self.pileList.setObjectName(u"pileList")
        self.pileList.setGeometry(QRect(10, 360, 381, 241))
        self.label_4 = QLabel(self.pileList)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 171, 41))
        self.pileListBtn = QPushButton(self.pileList)
        self.pileListBtn.setObjectName(u"pileListBtn")
        self.pileListBtn.setGeometry(QRect(280, 10, 91, 41))
        self.pileListTable = QTableWidget(self.pileList)
        if (self.pileListTable.columnCount() < 10):
            self.pileListTable.setColumnCount(10)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.pileListTable.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.pileListTable.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.pileListTable.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.pileListTable.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.pileListTable.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.pileListTable.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.pileListTable.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.pileListTable.setHorizontalHeaderItem(7, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.pileListTable.setHorizontalHeaderItem(8, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.pileListTable.setHorizontalHeaderItem(9, __qtablewidgetitem22)
        self.pileListTable.setObjectName(u"pileListTable")
        self.pileListTable.setGeometry(QRect(10, 60, 361, 171))
        self.pileStateUpdate = QWidget(self.info)
        self.pileStateUpdate.setObjectName(u"pileStateUpdate")
        self.pileStateUpdate.setGeometry(QRect(420, 360, 371, 241))
        self.label_5 = QLabel(self.pileStateUpdate)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 171, 41))
        self.label_6 = QLabel(self.pileStateUpdate)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 70, 171, 41))
        self.label_7 = QLabel(self.pileStateUpdate)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 130, 171, 41))
        self.pileNum = QLineEdit(self.pileStateUpdate)
        self.pileNum.setObjectName(u"pileNum")
        self.pileNum.setGeometry(QRect(210, 70, 151, 41))
        self.switchState = QComboBox(self.pileStateUpdate)
        self.switchState.addItem("")
        self.switchState.addItem("")
        self.switchState.addItem("")
        self.switchState.setObjectName(u"switchState")
        self.switchState.setGeometry(QRect(210, 130, 151, 41))
        self.updateBtn = QPushButton(self.pileStateUpdate)
        self.updateBtn.setObjectName(u"updateBtn")
        self.updateBtn.setGeometry(QRect(120, 190, 131, 41))
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(360, 10, 16, 671))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5145\u7535\u8ba1\u8d39\u7ba1\u7406\u5458\u5ba2\u6237\u7aef", None))
        self.l2.setText(QCoreApplication.translate("Form", u"\u8d26\u53f7\u7ba1\u7406", None))
        self.l3.setText(QCoreApplication.translate("Form", u"\u72b6\u6001", None))
        self.l4.setText(QCoreApplication.translate("Form", u"\u8eab\u4efd", None))
        self.l5.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.l1.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.userState.setText("")
        self.userIdentity.setText("")
        self.logoutBtn.setText(QCoreApplication.translate("Form", u"\u6ce8\u9500", None))
        self.loginBtn.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.registBtn.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4fe1\u606f\u67e5\u8be2\u4e0e\u7ba1\u7406", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2\u6392\u961f\u60c5\u51b5", None))
        self.queueBtn.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2", None))
        ___qtablewidgetitem = self.queueTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u5145\u7535\u6869\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.queueTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u72b6\u6001", None));
        ___qtablewidgetitem2 = self.queueTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u7d2f\u8ba1\u4f7f\u7528\u6b21\u6570", None));
        ___qtablewidgetitem3 = self.queueTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u7d2f\u8ba1\u4f7f\u7528\u65f6\u95f4", None));
        ___qtablewidgetitem4 = self.queueTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u7d2f\u8ba1\u5145\u7535\u7535\u91cf", None));
        ___qtablewidgetitem5 = self.queueTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u7d2f\u8ba1\u5145\u7535\u8d39\u7528", None));
        ___qtablewidgetitem6 = self.queueTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"\u7d2f\u8ba1\u670d\u52a1\u8d39\u7528", None));
        ___qtablewidgetitem7 = self.queueTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u7d2f\u8ba1\u8d39\u7528", None));
        self.label_3.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2\u5145\u7535\u6869\u72b6\u6001", None))
        self.pileStateBtn.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2", None))
        ___qtablewidgetitem8 = self.pileStateTable.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"\u5145\u7535\u6869\u7f16\u53f7", None));
        ___qtablewidgetitem9 = self.pileStateTable.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"\u72b6\u6001", None));
        ___qtablewidgetitem10 = self.pileStateTable.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"\u7d2f\u8ba1\u4f7f\u7528\u6b21\u6570", None));
        ___qtablewidgetitem11 = self.pileStateTable.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"\u7d2f\u8ba1\u5145\u7535\u65f6\u95f4", None));
        ___qtablewidgetitem12 = self.pileStateTable.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"\u7d2f\u8ba1\u5145\u7535\u7535\u91cf", None));
        self.label_4.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2\u5145\u7535\u6869\u62a5\u8868", None))
        self.pileListBtn.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2", None))
        ___qtablewidgetitem13 = self.pileListTable.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"\u5145\u7535\u6869\u7f16\u53f7", None));
        ___qtablewidgetitem14 = self.pileListTable.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"\u5929", None));
        ___qtablewidgetitem15 = self.pileListTable.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"\u5468", None));
        ___qtablewidgetitem16 = self.pileListTable.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"\u6708", None));
        ___qtablewidgetitem17 = self.pileListTable.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"\u7d2f\u8ba1\u4f7f\u7528\u6b21\u6570", None));
        ___qtablewidgetitem18 = self.pileListTable.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"\u7d2f\u8ba1\u5145\u7535\u65f6\u957f", None));
        ___qtablewidgetitem19 = self.pileListTable.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"\u7d2f\u8ba1\u5145\u7535\u7535\u91cf", None));
        ___qtablewidgetitem20 = self.pileListTable.horizontalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form", u"\u7d2f\u8ba1\u5145\u7535\u8d39\u7528", None));
        ___qtablewidgetitem21 = self.pileListTable.horizontalHeaderItem(8)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form", u"\u7d2f\u8ba1\u670d\u52a1\u8d39\u7528", None));
        ___qtablewidgetitem22 = self.pileListTable.horizontalHeaderItem(9)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form", u"\u7d2f\u8ba1\u8d39\u7528", None));
        self.label_5.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u5145\u7535\u6869\u72b6\u6001", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5145\u7535\u6869\u7f16\u53f7", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u72b6\u6001", None))
        self.switchState.setItemText(0, QCoreApplication.translate("Form", u"\u8fd0\u884c", None))
        self.switchState.setItemText(1, QCoreApplication.translate("Form", u"\u5173\u673a", None))
        self.switchState.setItemText(2, QCoreApplication.translate("Form", u"\u6545\u969c", None))

        self.updateBtn.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0", None))
    # retranslateUi

