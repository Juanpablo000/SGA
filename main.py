# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 13:29:46 2022

@author: Sam
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi

class VentanaPrincipal(QMainWindow):
    
    
    # Control Menú Superior
    
    def control_bt_minimizar(self):
        self.showMinimized()
    
    def control_bt_normal(self):
        self.showNormal()
        self.bt_restaurar.hide()
        self.bt_maximizar.show()
        
    def control_bt_maximizar(self):
        self.showMaximized()
        self.bt_maximizar.hide()
        self.bt_restaurar.show()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <= 10:
            self.showMaximized()
            self.bt_maximizar.hide()
            self.bt_restaurar.show()
        else:
            self.showNormal()
            self.bt_restaurar.hide()
            self.bt_maximizar.show()
            
            
    # Animación de paginas
    def pagina_uno(self):
        self.stackedWidget.setCurrentWidget(self.page_uno)
        self.animacion_paginas()
    def pagina_dos(self):
        self.stackedWidget.setCurrentWidget(self.page_dos)
        self.animacion_paginas
    def pagina_tres(self):
        self.stackedWidget.setCurrentWidget(self.page_tres)
        self.animacion_paginas
    def pagina_cuatro(self):
        self.stackedWidget.setCurrentWidget(self.page_cuatro)
        self.animacion_paginas
    def pagina_cinco(self):
        self.stackedWidget.setCurrentWidget(self.page_cinco)
        self.animacion_paginas
        
    # Creamos el metodo para la animación de las paginas
    def animacion_paginas(self):
        if True:
            width = self.stackedWidget.width()
            x1 = self.frame_paginas.rect().right()
            normal = 100
            if width == 100:
                extender = x1
            else:
                extender = normal
            self.animacion1 = QPropertyAnimation(self.stackWidget, b"maxiumWidth") 
            self.animacion1.setStartValue(width)
            self.animacion1.setEndValue(extender)
            self.animacion1.setDuration(500)
            self.animacion1.setEasingCurve(QEasingCurve.InOutQuad)
            self.animacion1.start()
            
    ## SizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        
    ## mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()   
        
    
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('diseño.ui', self)
        
        # sombra de los widgets
        
        # ocultamos el botón
        self.bt_restaurar.hide()
        
        # control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())
        
        # eliminar barra de titulo - opacidad
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        # SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        
        # acceder a las paginas
        self.bt_uno.clicked.connect(self.pagina_uno)
        self.bt_dos.clicked.connect(self.pagina_dos)
        self.bt_tres.clicked.connect(self.pagina_tres)
        self.bt_cuatro.clicked.connect(self.pagina_cuatro)
        self.bt_cinco.clicked.connect(self.pagina_cinco)        
            
            
            
        # creamos el metodo sombra        
            
        
                
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())
            
            
        