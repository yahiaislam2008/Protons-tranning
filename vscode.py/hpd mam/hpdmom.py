# Form implementation generated from reading ui file 'hpdmom.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_m4_lazm_t3rfy(object):
    def setupUi(self, m4_lazm_t3rfy):
        m4_lazm_t3rfy.setObjectName("m4_lazm_t3rfy")
        m4_lazm_t3rfy.resize(556, 480)
        m4_lazm_t3rfy.setStyleSheet("color: rgb(170, 255, 255);\n"
"background:rgb(32, 239, 239)")
        self.centralwidget = QtWidgets.QWidget(parent=m4_lazm_t3rfy)
        self.centralwidget.setObjectName("centralwidget")
        self.suprize = QtWidgets.QPushButton(parent=self.centralwidget)
        self.suprize.setGeometry(QtCore.QRect(210, 290, 111, 41))
        self.suprize.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 16pt \"Segoe UI\";\n"
"background-color: rgb(176, 156, 255);")
        self.suprize.setObjectName("suprize")
        m4_lazm_t3rfy.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=m4_lazm_t3rfy)
        self.statusbar.setObjectName("statusbar")
        m4_lazm_t3rfy.setStatusBar(self.statusbar)

        self.retranslateUi(m4_lazm_t3rfy)
        QtCore.QMetaObject.connectSlotsByName(m4_lazm_t3rfy)

    def retranslateUi(self, m4_lazm_t3rfy):
        _translate = QtCore.QCoreApplication.translate
        m4_lazm_t3rfy.setWindowTitle(_translate("m4_lazm_t3rfy", "MainWindow"))
        self.suprize.setText(_translate("m4_lazm_t3rfy", "click here "))