# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 13:29:46 2022

@author: Sam
"""
import re
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QMessageBox, QTableWidgetItem, QComboBox
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from datetime import datetime

# Se importan las funciones del mainback
from mainback import SetData, GetData

"""
     _______________________________
    °                               ° 
    °                               °
    °          FRONT APP            °
    °                               °
    °_______________________________°

"""

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
        self.animacion_paginas
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

        z=0
        super(VentanaPrincipal, self).__init__()
        loadUi('diseñoSGA.ui', self)
        
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
            
            
            
        """
             _______________________________
            °                               ° 
            °                               °
            °    FUNCIONALIDADES FRONT      °
            °                               °
            °_______________________________°
        
        """
        
        
        


        # Registrar Nuevo Cliente
        
        def NewClient():
            
            params = []
            
            params.append(str(self.cb_tipodoc_C.currentText()))
            params.append(self.le_documento_C.text())            
            params.append(self.le_nombre_C.text())
            params.append(self.le_apellido_C.text())
            params.append(self.le_direccion_C.text())
            params.append(self.le_telefono_C.text())
            params.append(str(self.cb_ciudad_C.currentText()))
            
            query = 'Exec SP_RegistrarClientes @TipoDoc = ?, @NumeroDoc = ?, @Nombres = ?, @Apellidos = ?, @Direccion = ?, @Telefono = ?, @ciudad = ?'
            
            aux = SetData(self, params, query)
            
            if aux == 1:
                QMessageBox.about(self, 'Procedimiento Exitoso!', 'Se realizó el registro correctamente')
                self.le_documento_C.clear()
                self.le_nombre_C.clear()
                self.le_apellido_C.clear()
                self.le_direccion_C.clear()
                self.le_telefono_C.clear()
                
        # Registrar Nuevo Proveedor
        def NewProeevedor():
            
            params = []
            
            params.append(str(self.cb_tipodoc_P.currentText()))
            params.append(self.le_documento_P.text())            
            params.append(self.le_nombre_P.text())
            params.append(self.le_apellido_P.text())
            params.append(self.le_nombrecomercial_P.text())
            params.append(self.le_direccion_P.text())
            params.append(str(self.cb_ciudad_P.currentText()))
            params.append(self.le_telefono_P.text())
            
            
            query = 'Exec SP_RegistrarProeevedores @TipoDoc = ?, @NumeroDoc = ?, @Nombres = ?, @Apellidos = ?, @NombreComercial= ?, @Direccion = ?, @ciudad = ?, @Telefono = ?'
            
            aux = SetData(self, params, query)
            
            if aux == 1:
                QMessageBox.about(self, 'Procedimiento Exitoso!', 'Se realizó el registro correctamente')
                self.le_documento_P.clear()
                self.le_nombre_P.clear()
                self.le_apellido_P.clear()
                self.le_direccion_P.clear()
                self.le_telefono_P.clear()
                self.le_nombrecomercial_P.clear()


        # Registrar Nuevo Artículo
        
        def NewArticulo():
            
            params = []
            params.append(self.le_descripcion_AR.text())
            params.append(self.le_precioventa_A.text())
            params.append(self.le_preciocosto_A.text())   
            params.append(self.le_cantidad_A.text())
            params.append(str(self.cb_categoria_A.currentText()))
            params.append(str(self.cb_proveedor_A.currentText()))
            query = 'Exec SP_RegistarArticulos @NombreArticulo = ?, @PrecioVenta = ?, @PrecioUnitario = ?, @Cantidad = ?, @NombreCategoria= ?, @IdProeevedor = ?'
            
            aux = SetData(self, params, query)
            
            if aux == 1:
                QMessageBox.about(self, 'Procedimiento Exitoso!', 'Se realizó el registro correctamente')
                self.cb_categoria_A.clear()
                self.le_descripcion_AR.clear()
                self.le_precioventa_A.clear()
                self.le_cantidad_A.clear()
                self.cb_proveedor_A.clear()

        # Actualizar Stock
        def ActStock():

            #if nuevo_stock < stock_actual error
            params = []
            params.append(str(self.cb_idarticulo_A.currentText()))
            params.append(self.le_registrarstock_A.text())
            query = 'Exec SP_ActualizarStock @ID_Articulo = ?, @Cantidad = ?'
            
            aux = SetData(self, params, query)
            
            if aux == 1:
                QMessageBox.about(self, 'Procedimiento Exitoso!', 'Se realizó el registro correctamente')
                self.le_registrarstock_A.clear()


        # Registrar Detalle
        def NewDetalle():
            params = []
            params.append(self.le_numerofactura_F.text())
            params.append(self.le_articulo_F.text())
            params.append(self.le_cantidad_F.text())   
            params.append(self.le_totalarticulosF.text())
            query = 'Exec SP_RegistrarDetalleFactura @NumFactura = ?, @Descripcion = ?, @Cantidad = ?, @TotalDetalle = ?'
            
            aux = SetData(self, params, query)
            
            if aux == 1:
                QMessageBox.about(self, 'Procedimiento Exitoso!', 'Se realizó el registro correctamente')
                self.le_numerofactura_F.clear()
                self.le_articulo_F.clear()
                self.le_cantidad_F.clear()
                self.le_totalarticulosF.clear()
                ListDetalle


        # Devolución Artículo
        
        # Registrar Factura
        
        """
             _______________________________
            °                               ° 
            °                               °
            °         CONSULTAS             °
            °                               °
            °_______________________________°

        """   


        def ListDetalle():
            data = []
            query = 'SELECT * FROM DetalleFactura'
            data = GetData(self, query)
            
            f = len(data)
            
            if f != 0:
                c = len(data[0])                
                self.table_FR.setRowCount(f)                  
                for i in range(f):
                    for j in range(c):
                        self.table_FR.setItem(i,j,QTableWidgetItem(str(data[i][j])))
            else:
                QMessageBox.warning(self, 'Advertencia!', 'No se encontraron registros')

        
        def ListClientes():
            data = []
            query = 'SELECT NumeroDocumento, TipoDoc, Nombres, Apellidos, Direccion, Ciudad, Telefono   FROM Clientes'
            data = GetData(self, query)
            
            f = len(data)
            
            if f != 0:
                c = len(data[0])                
                self.tableCL.setRowCount(f)                  
                for i in range(f):
                    for j in range(c):
                        self.tableCL.setItem(i,j,QTableWidgetItem(str(data[i][j])))
            else:
                QMessageBox.warning(self, 'Advertencia!', 'No se encontraron registros')


        # Listar proeevedores

        def ListProeevedor():
            data = []
            query = 'SELECT NumeroDocumento, TipoDoc, Nombres, Apellidos, NombreComercial, Direccion, Ciudad, Telefono   FROM Proeevedores'
            data = GetData(self, query)
            
            f = len(data)
            
            if f != 0:
                c = len(data[0])                
                self.table_PL.setRowCount(f)                  
                for i in range(f):
                    for j in range(c):
                        self.table_PL.setItem(i,j,QTableWidgetItem(str(data[i][j])))
            else:
                QMessageBox.warning(self, 'Advertencia!', 'No se encontraron registros')

    
        def combo_input():
            data=[]
            query = 'select IdProeevedor from Proeevedores'
            data = GetData(self, query)
            
            f = len(data)
            
            self.cb_proveedor_A.clear()
            datosLimpios = re.findall('[0-9]+',  str(data))
            
            for i in range(f):
                self.cb_proveedor_A.addItem(datosLimpios[i])
                #self.cb_proveedor_A.addItem(QComboBox(str(data[i])))
                #self.cb_proveedor_A.setItemText(str(data[i]))

                #self.cb_proveedor_A.setItemText(QComboBox(str(data[i])))

        # Listar proeevedores

        def ListArticulos():
            data = []
            query = 'select IdArticulo, NombreArticulo, PrecioVenta, PrecioUnitario, Cantidad, NombreCategoria, (p.Nombres + ' '+p.Apellidos) AS Nombre FROM Articulos at INNER JOIN Proeevedores p ON  p.IdProeevedor = at.IdProeevedor'
            data = GetData(self, query)
            
            f = len(data)
            
            if f != 0:
                c = len(data[0])                
                self.table_AL.setRowCount(f)                  
                for i in range(f):
                    for j in range(c):
                        self.table_AL.setItem(i,j,QTableWidgetItem(str(data[i][j])))
            else:
                QMessageBox.warning(self, 'Advertencia!', 'No se encontraron registros')
            

        def actualizarInfoArticulos():
            data=[]
            articuloActualo = str(self.cb_idarticulo_A.currentText())
            query = 'Select NombreArticulo, Cantidad from Articulos where IdArticulo = '
            query = query + articuloActualo
            #VALIDACION
            data = GetData(self, query)

            self.le_stockactual_A.setText(str(data[0][1]))
            self.le_descripcion_AA.setText(str(data[0][0]))

        

        def combo_articulos():
            data=[]
            query = 'select IdArticulo from Articulos'
            data = GetData(self, query)
            
            f = len(data)
            
            self.cb_idarticulo_A.clear()
            datosLimpios = re.findall('[0-9]+',  str(data))
            
            for i in range(f):
                self.cb_idarticulo_A.addItem(datosLimpios[i])

        def combo_documentos():
            data=[]
            query = 'select NumeroDocumento from Clientes'
            data = GetData(self, query)
            
            f = len(data)
            
            self.cb_numdocCliente_F.clear()
            datosLimpios = re.findall('[0-9]+',  str(data))
            
            for i in range(f):
                self.cb_numdocCliente_F.addItem(datosLimpios[i])

        def actualizarClienteFactura():
            numfac_tmp = 'FACT-00000000'

            data=[]
            query = 'select count (NumeroFactura) from Facturacion'
            data = GetData(self, query)
            
            f = len(data)
            
            self.cb_proveedor_A.clear()
            datosLimpios = re.findall('[0-9]+',  str(data))

            t = 0
            t = int(datosLimpios[0])
            t = t + 1

            numfac_tmp+=str(t)
            self.le_numerofactura_F.setText(numfac_tmp)


        def combo_articulosFactura():
            data=[]
            query = 'select IdArticulo from Articulos'
            data = GetData(self, query)
            
            f = len(data)
            
            self.cb_idArticulo_F.clear()
            datosLimpios = re.findall('[0-9]+',  str(data))
            
            for i in range(f):
                self.cb_idArticulo_F.addItem(datosLimpios[i])


        def actualizarArticuloFactura():
            data=[]
            idArticulo = str(self.cb_idArticulo_F.currentText())
            query = 'Select NombreArticulo, Cantidad, PrecioVenta from Articulos where IdArticulo = '
            query = query + idArticulo
            #VALIDACION
            data = GetData(self, query)

            self.le_articulo_F.setText(str(data[0][0]))
            self.le_stock_F.setText(str(data[0][1]))
            self.le_preciounidad_F.setText(str(data[0][2]))

        def IrDetalle():
            self.bt_registrarfactura_F.setEnabled(False)
            #self.bt_registrarfactura_F.setStyleSheet('QPushButton {background-color: #A3C1DA; color: gray;}')

            self.cb_numdocCliente_F.setEnabled(False)
            self.cb_formaPago_F.setEnabled(False)
            self.le_vendedor_F.setEnabled(False)
            
            self.cb_idArticulo_F.setEnabled(True)
            self.le_cantidad_F.setEnabled(True)

            self.bt_registrardetalle_F.setEnabled(True)



    
        
        def llenarTablaDetalle():
            z=0
            params = []
            params.append(self.le_numerofactura_F.text())
            params.append(self.le_articulo_F.text())
            params.append(self.le_cantidad_F.text())   
            params.append(self.le_totalarticulosF.text())

            self.table_FR.setRowCount(4) 
            print(z)       
        
            self.table_FR.setItem(z,0,QTableWidgetItem(str(params[0])))#num factura
            self.table_FR.setItem(z,1,QTableWidgetItem(str(params[1])))#nom articulo
            self.table_FR.setItem(z,2,QTableWidgetItem(str(params[2])))#cantidad a comprar
            self.table_FR.setItem(z,3,QTableWidgetItem(str(params[3])))#precio total de articulos
            z=z+1


        def calcularPrecioTotalArticulos():
            pv = int(self.le_preciounidad_F.text())

            if(len(self.le_cantidad_F.text())>0):
                cf = int(self.le_cantidad_F.text())

                if(cf>0 and pv>0):
                    p_subTotal= cf * pv
            else:
                p_subTotal=0

            self.le_totalarticulosF.setText(str(p_subTotal))

                
            
            

        """
             _______________________________
            °                               ° 
            °                               °
            °            BOTONES            °
            °                               °
            °_______________________________°

        """   
        #cargar comboxs
        self.bt_tres.clicked.connect(combo_input)
        self.bt_tres.clicked.connect(combo_articulos)
        self.bt_cuatro.clicked.connect(combo_documentos)
        self.bt_cuatro.clicked.connect(combo_articulosFactura)

        self.bt_registrarfactura_F.clicked.connect(IrDetalle)

        #actualizar contenido del stock
        #necesita validación
        self.cb_idarticulo_A.currentTextChanged.connect(actualizarInfoArticulos)
        self.cb_numdocCliente_F.currentTextChanged.connect(actualizarClienteFactura)
        self.cb_idArticulo_F.currentTextChanged.connect(actualizarArticuloFactura)

        self.le_cantidad_F.textChanged.connect(calcularPrecioTotalArticulos)


        # Registrar Cliente
        self.bt_registrar_C.clicked.connect(NewClient)

        # Listar Clientes
        self.bt_buscar_C.clicked.connect(ListClientes)

        # Registrar Proeevedores
        self.bt_registrar_P.clicked.connect(NewProeevedor)
        
        # Listar Proeevedores
        self.bt_buscar_P.clicked.connect(ListProeevedor)

        # Registrar Articulos
        self.bt_registrar_A.clicked.connect(NewArticulo)
        
        # Listar Articulos
        self.bt_buscar_A.clicked.connect(ListArticulos)

        # Actulizar stock
        self.bt_ActualizarStock.clicked.connect(ActStock)
    
        #Registrar detalle

        self.bt_registrardetalle_F.clicked.connect(llenarTablaDetalle)

        #self.bt_registrardetalle_F.clicked.connect(NewDetalle)

                
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())
            