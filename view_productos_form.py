#!/usr/bin/python
# ­*­ coding: utf­8 ­*­

from PySide import QtGui, QtCore
import control_productos
from productos_form import Ui_Form

class Form(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui =  Ui_Form()
        self.ui.setupUi(self)
        self.ui.btn_cancel.clicked.connect(self.cancel)
	self.ui.btn_add.clicked.connect(self.add)
        

    def cancel(self):
        self.reject()

    def add(self):
	self.reject()
	
	

