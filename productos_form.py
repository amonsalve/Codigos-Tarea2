# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productos_form.ui'
#
# Created: Mon Jun  3 17:39:49 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(419, 321)
        self.codigo = QtGui.QLineEdit(Form)
        self.codigo.setGeometry(QtCore.QRect(116, 34, 141, 27))
        self.codigo.setObjectName("codigo")
        self.nombre = QtGui.QLineEdit(Form)
        self.nombre.setGeometry(QtCore.QRect(116, 69, 231, 27))
        self.nombre.setObjectName("nombre")
        self.descripcion = QtGui.QLineEdit(Form)
        self.descripcion.setGeometry(QtCore.QRect(116, 104, 231, 27))
        self.descripcion.setObjectName("descripcion")
        self.color = QtGui.QLineEdit(Form)
        self.color.setGeometry(QtCore.QRect(116, 140, 181, 27))
        self.color.setObjectName("color")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 51, 20))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 66, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 51, 20))
        self.label_4.setObjectName("label_4")
        self.btn_add = QtGui.QPushButton(Form)
        self.btn_add.setGeometry(QtCore.QRect(147, 220, 98, 27))
        self.btn_add.setObjectName("btn_add")
        self.btn_cancel = QtGui.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(247, 220, 98, 27))
        self.btn_cancel.setObjectName("btn_cancel")
        self.mensajes = QtGui.QLabel(Form)
        self.mensajes.setGeometry(QtCore.QRect(60, 270, 301, 17))
        self.mensajes.setText("")
        self.mensajes.setObjectName("mensajes")
        self.precio = QtGui.QLineEdit(Form)
        self.precio.setGeometry(QtCore.QRect(120, 180, 121, 27))
        self.precio.setObjectName("precio")
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 180, 51, 20))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.codigo.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingrese el codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.nombre.setPlaceholderText(QtGui.QApplication.translate("Form", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.descripcion.setPlaceholderText(QtGui.QApplication.translate("Form", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.color.setPlaceholderText(QtGui.QApplication.translate("Form", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add.setText(QtGui.QApplication.translate("Form", "Crear", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.precio.setPlaceholderText(QtGui.QApplication.translate("Form", "Precio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Precio", None, QtGui.QApplication.UnicodeUTF8))

