# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaSistema.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_janelaPrincipal(object):
    def setupUi(self, janelaPrincipal):
        janelaPrincipal.setObjectName("janelaPrincipal")
        janelaPrincipal.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(janelaPrincipal.sizePolicy().hasHeightForWidth())
        janelaPrincipal.setSizePolicy(sizePolicy)
        janelaPrincipal.setMinimumSize(QtCore.QSize(800, 600))
        janelaPrincipal.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(janelaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_1 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_1.setGeometry(QtCore.QRect(20, 20, 88, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.bt_1.setFont(font)
        self.bt_1.setStyleSheet("background-color: yellow;")
        self.bt_1.setObjectName("bt_1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 30, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 130, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.bt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_2.setGeometry(QtCore.QRect(20, 120, 88, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.bt_2.setFont(font)
        self.bt_2.setStyleSheet("background-color: orange\n"
";")
        self.bt_2.setObjectName("bt_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 240, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.bt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_3.setGeometry(QtCore.QRect(20, 230, 88, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.bt_3.setFont(font)
        self.bt_3.setStyleSheet("background-color: red;")
        self.bt_3.setObjectName("bt_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 310, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:blue;")
        self.label_4.setObjectName("label_4")
        self.entrada_msg = QtWidgets.QTextEdit(self.centralwidget)
        self.entrada_msg.setGeometry(QtCore.QRect(20, 360, 761, 221))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.entrada_msg.setFont(font)
        self.entrada_msg.setStyleSheet("font: 75 36pt \"MS Shell Dlg 2\";")
        self.entrada_msg.setObjectName("entrada_msg")
        janelaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(janelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(janelaPrincipal)

    def retranslateUi(self, janelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        janelaPrincipal.setWindowTitle(_translate("janelaPrincipal", "ALERTA FRINEPE CAIXA"))
        self.bt_1.setText(_translate("janelaPrincipal", "1"))
        self.label.setText(_translate("janelaPrincipal", "CANCELAR ITEM NA VENDA"))
        self.label_2.setText(_translate("janelaPrincipal", "CANCELAR VENDA COMPLETA"))
        self.bt_2.setText(_translate("janelaPrincipal", "2"))
        self.label_3.setText(_translate("janelaPrincipal", "PRECISO DE AJUDA NO CAIXA"))
        self.bt_3.setText(_translate("janelaPrincipal", "3"))
        self.label_4.setText(_translate("janelaPrincipal", "MENSAGEM"))
        self.entrada_msg.setHtml(_translate("janelaPrincipal", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:40px; font-weight:600;\"><br /></p></body></html>"))
