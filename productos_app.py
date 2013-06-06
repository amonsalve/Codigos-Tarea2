#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
import control_productos
from productos_ui import Ui_ProductosWindow
import view_productos_form


class ProductosApp(QtGui.QWidget):

    def __init__(self):
        super(ProductosApp, self).__init__()
        self.ui = Ui_ProductosWindow()
	self.ui.setupUi(self)
	self.set_listeners()
	self.load_productos()
	self.load_marcas()
	self.delete()
	self.show()
       

    def set_listeners(self):
        self.ui.btn_new.clicked.connect(self.show_add_form)
        self.ui.btn_search.clicked.connect(self.load_productos_by_search)
	self.ui.combo_marcas.activated[int].connect(self.load_productos_por_marca)
        self.ui.btn_delete.clicked.connect(self.delete)


    def delete(self):
        model = self.ui.table_productos.model()
        index = self.ui.table_productos.currentIndex()
	
        if index.row() == -1: #No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            #Obtenemos el rut que es la primary key en la tabla
            codigo = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            if (control_productos.delete(codigo)):
                self.load_productos()
                msgBox = QtGui.QMessageBox()
                msgBox.setText("EL registro fue eliminado.")
                msgBox.exec_()
                return True
            else:
                self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                self.ui.errorMessageDialog.showMessage("Error al eliminar")
                return False


    def load_marcas(self):
        marcas = control_productos.get_marcas()
        self.ui.combo_marcas.addItem("Todos", -1)
        for marca in marcas:
            self.ui.combo_marcas.addItem(marca["nombre"], marca["id_marca"])



    def load_productos_by_search(self):
        word = self.ui.search_box.text()
        productos = control_productos.search_productos(word)
        self.load_productos(productos)



    def load_productos_por_marca(self, index):
        id_marca = self.ui.combo_marcas.itemData(self.ui.combo_marcas.currentIndex())
        if id_marca == -1:
            productos = control_productos.get_productos()
        else:
            productos = control_productos.get_productos_por_marca(id_marca)
        self.load_productos(productos)



    def show_add_form(self):
        form = view_productos_form.Form(self)
        form.rejected.connect(self.load_productos)
        form.exec_()

    def load_productos(self, productos=None):
        	if productos is None:
            		productos = control_productos.get_productos()

        	
        	self.model = QtGui.QStandardItemModel(len(productos), 6)
        	self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Codigo"))
        	self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        	self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Descripcion"))
        	self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Color"))
		self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Precio"))
		self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Marca"))
        	r = 0
        	for row in productos:
            		index = self.model.index(r, 0, QtCore.QModelIndex()); 
            		self.model.setData(index, row['codigo'])
            		index = self.model.index(r, 1, QtCore.QModelIndex()); 
            		self.model.setData(index, row['nombre'])
            		index = self.model.index(r, 2, QtCore.QModelIndex()); 
            		self.model.setData(index, row['descripcion'])
            		index = self.model.index(r, 3, QtCore.QModelIndex()); 
           		self.model.setData(index, row['color'])
			index = self.model.index(r, 4, QtCore.QModelIndex()); 
           		self.model.setData(index, row['precio'])
			index = self.model.index(r, 5, QtCore.QModelIndex()); 
           		self.model.setData(index, row['marca'])
           		r = r+1

        	self.ui.table_productos.setModel(self.model)
        	self.ui.table_productos.setColumnWidth(0, 150)
        	self.ui.table_productos.setColumnWidth(1, 150)
       	 	self.ui.table_productos.setColumnWidth(2, 150)
        	self.ui.table_productos.setColumnWidth(3, 150)
		self.ui.table_productos.setColumnWidth(4, 150)
		self.ui.table_productos.setColumnWidth(5, 150)

def run():
    app = QtGui.QApplication(sys.argv)
    main = ProductosApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    	run()
