# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_productos.ui'
#
# Created: Wed Jun  5 21:20:20 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ProductosWindow(object):
    def setupUi(self, ProductosWindow):
        ProductosWindow.setObjectName("ProductosWindow")
        ProductosWindow.resize(851, 457)
        self.combo_marcas = QtGui.QComboBox(ProductosWindow)
        self.combo_marcas.setGeometry(QtCore.QRect(700, 60, 101, 31))
        self.combo_marcas.setObjectName("combo_marcas")
        self.label = QtGui.QLabel(ProductosWindow)
        self.label.setGeometry(QtCore.QRect(550, 66, 151, 20))
        self.label.setObjectName("label")
        self.search_box = QtGui.QLineEdit(ProductosWindow)
        self.search_box.setGeometry(QtCore.QRect(20, 30, 421, 25))
        self.search_box.setText("")
        self.search_box.setObjectName("search_box")
        self.btn_search = QtGui.QPushButton(ProductosWindow)
        self.btn_search.setGeometry(QtCore.QRect(20, 60, 87, 27))
        self.btn_search.setObjectName("btn_search")
        self.table_productos = QtGui.QTableView(ProductosWindow)
        self.table_productos.setGeometry(QtCore.QRect(20, 100, 791, 331))
        self.table_productos.setObjectName("table_productos")
        self.btn_new = QtGui.QPushButton(ProductosWindow)
        self.btn_new.setGeometry(QtCore.QRect(486, 20, 121, 27))
        self.btn_new.setObjectName("btn_new")
        self.btn_delete = QtGui.QPushButton(ProductosWindow)
        self.btn_delete.setGeometry(QtCore.QRect(720, 20, 87, 27))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_edit_2 = QtGui.QPushButton(ProductosWindow)
        self.btn_edit_2.setGeometry(QtCore.QRect(620, 20, 87, 27))
        self.btn_edit_2.setObjectName("btn_edit")

        self.retranslateUi(ProductosWindow)
        QtCore.QMetaObject.connectSlotsByName(ProductosWindow)

    def retranslateUi(self, ProductosWindow):
        ProductosWindow.setWindowTitle(QtGui.QApplication.translate("ProductosWindow", "Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProductosWindow", "Seleccione una marca", None, QtGui.QApplication.UnicodeUTF8))
        self.search_box.setPlaceholderText(QtGui.QApplication.translate("ProductosWindow", "Que producto desea buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_search.setText(QtGui.QApplication.translate("ProductosWindow", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_new.setText(QtGui.QApplication.translate("ProductosWindow", "Nuevo Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setText(QtGui.QApplication.translate("ProductosWindow", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_edit_2.setText(QtGui.QApplication.translate("ProductosWindow", "Editar", None, QtGui.QApplication.UnicodeUTF8))

