# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfirmacionAccion_d.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(382, 411)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textBrowser_indicaciones = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_indicaciones.setMinimumSize(QtCore.QSize(330, 120))
        self.textBrowser_indicaciones.setStyleSheet("border-radius:10px;\n"
"border : 2px solid black;\n"
"background : white;")
        self.textBrowser_indicaciones.setObjectName("textBrowser_indicaciones")
        self.verticalLayout.addWidget(self.textBrowser_indicaciones)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lineEdit_wordRepetir = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_wordRepetir.setMinimumSize(QtCore.QSize(220, 40))
        self.lineEdit_wordRepetir.setStyleSheet("border-radius:5px;\n"
"border : 1px solid black;\n"
"background : white;")
        self.lineEdit_wordRepetir.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_wordRepetir.setObjectName("lineEdit_wordRepetir")
        self.horizontalLayout_2.addWidget(self.lineEdit_wordRepetir)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lineEdit_firma = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_firma.setMinimumSize(QtCore.QSize(220, 40))
        self.lineEdit_firma.setStyleSheet("border-radius:5px;\n"
"border : 1px solid black;\n"
"background : white;")
        self.lineEdit_firma.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_firma.setObjectName("lineEdit_firma")
        self.horizontalLayout.addWidget(self.lineEdit_firma)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.btn_aceptar = QtWidgets.QPushButton(Dialog)
        self.btn_aceptar.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.horizontalLayout_3.addWidget(self.btn_aceptar)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Confirmacion accion"))
        self.label.setText(_translate("Dialog", "Indicaciones:"))
        self.label_2.setText(_translate("Dialog", "Frase de confirmacion:"))
        self.label_3.setText(_translate("Dialog", "Repetir frase de confirmacion:"))
        self.btn_aceptar.setText(_translate("Dialog", "Aceptar"))