# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.setEnabled(True)
        Dialog.resize(407, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(407, 400))
        Dialog.setMaximumSize(QtCore.QSize(407, 400))
        Dialog.setMouseTracking(False)
        Dialog.setStyleSheet("background-color: #057;")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 230, 321, 148))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.button1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button1.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #D41;\n"
"    border-radius: None;\n"
"    font: 75 13pt \"Mangal\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C31;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #A20;\n"
"}\n"
"")
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 2, 0, 1, 1)
        self.buttonN = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.buttonN.setAutoFillBackground(False)
        self.buttonN.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #D41;\n"
"    border-radius: None;\n"
"    font: 75 13pt \"Mangal\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C31;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #A20;\n"
"}")
        self.buttonN.setAutoDefault(True)
        self.buttonN.setDefault(False)
        self.buttonN.setFlat(False)
        self.buttonN.setObjectName("buttonN")
        self.gridLayout.addWidget(self.buttonN, 0, 0, 1, 1)
        self.buttonW = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.buttonW.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #D41;\n"
"    border-radius: None;\n"
"    font: 75 13pt \"Mangal\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C31;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #A20;\n"
"}\n"
"")
        self.buttonW.setObjectName("buttonW")
        self.gridLayout.addWidget(self.buttonW, 1, 0, 1, 1)
        self.buttonS = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.buttonS.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #D41;\n"
"    border-radius: None;\n"
"    font: 75 13pt \"Mangal\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C31;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #A20;\n"
"}\n"
"")
        self.buttonS.setObjectName("buttonS")
        self.gridLayout.addWidget(self.buttonS, 1, 1, 1, 1)
        self.buttonE = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.buttonE.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonE.sizePolicy().hasHeightForWidth())
        self.buttonE.setSizePolicy(sizePolicy)
        self.buttonE.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.buttonE.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #D41;\n"
"    border-radius: None;\n"
"    font: 75 13pt \"Mangal\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C31;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #A20;\n"
"}")
        self.buttonE.setObjectName("buttonE")
        self.gridLayout.addWidget(self.buttonE, 0, 1, 1, 1)
        self.button2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button2.setEnabled(True)
        self.button2.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #D41;\n"
"    border-radius: None;\n"
"    font: 75 13pt \"Mangal\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C31;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #A20;\n"
"}")
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 2, 1, 1, 1)
        self.top_label = QtWidgets.QLabel(Dialog)
        self.top_label.setGeometry(QtCore.QRect(30, 20, 350, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_label.sizePolicy().hasHeightForWidth())
        self.top_label.setSizePolicy(sizePolicy)
        self.top_label.setStyleSheet("QLabel {\n"
"    background-color: #000;\n"
"    color: #AAA;\n"
"    padding:10;\n"
"    font: 8pt \"Mangal\";\n"
"}")
        self.top_label.setObjectName("top_label")
        self.down_label = QtWidgets.QLabel(Dialog)
        self.down_label.setGeometry(QtCore.QRect(30, 110, 350, 111))
        self.down_label.setStyleSheet("QLabel {\n"
"    background-color: #000;\n"
"    color: #AAA;\n"
"    padding:10;\n"
"    font: 8pt \"Mangal\";\n"
"}")
        self.down_label.setObjectName("down_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Funny game"))
        self.button1.setText(_translate("Dialog", "Осмотреться"))
        self.buttonN.setText(_translate("Dialog", "Северная дверь"))
        self.buttonW.setText(_translate("Dialog", "Западная дверь"))
        self.buttonS.setText(_translate("Dialog", "Южная дверь"))
        self.buttonE.setText(_translate("Dialog", "Восточная дверь"))
        self.button2.setText(_translate("Dialog", "Крикнуть"))
        self.top_label.setText(_translate("Dialog", "Комната"))
        self.down_label.setText(_translate("Dialog", "<html><head/><body><p>Итоги:</p><p>Действие</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
