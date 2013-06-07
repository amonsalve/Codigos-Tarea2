#!/usr/bin/python
# ­*­ coding: utf­8 ­*­



from PySide import QtGui, QtCore
import control_productos
from productos_form import Ui_Form

class Form(QtGui.QDialog):
    def __init__(self, parent=None, codigo=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui =  Ui_Form()
        self.ui.setupUi(self)
        
	if codigo is None:
            self.ui.btn_add.clicked.connect(self.add)
        else:
            self.codigo = codigo
            datos_productos = control_productos.get_productos_por_codigo(codigo)
            self.ui.codigo.setText(datos_productos["codigo"])
            self.ui.nombre.setText(datos_productos["nombre"])
            self.ui.descripcion.setText(datos_productos["descripcion"])
            self.ui.color.setText(datos_productos["color"])
            self.ui.precio.setText(datos_productos["precio"])

            self.ui.btn_add.clicked.connect(self.edit)


        self.ui.btn_cancel.clicked.connect(self.cancel)
     



    def add(self):
        codigo = self.ui.codigo.text()
        nombre = self.ui.nombre.text()
        descripcion = self.ui.descripcion.text()
        color = self.ui.color.text()
	precio = self.ui.precio.text()
        result = control_productos.agregar(codigo, nombre, descripcion, color, precio)

        if result:
            self.reject() #Cerramos y esto cargara nuevamente la grilla
        else:
            self.ui.mensajes.setText("No se pudo agregar el producto,hubo un error")

    def edit(self):
        print "estoy editando: ", self.codigo
   

    def cancel(self):
        self.reject()

		
	
	
	
	
	

