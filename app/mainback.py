import pyodbc
from PyQt5.QtWidgets import QMessageBox


server = 'DESKTOP-VS0AF6Q'
bd = 'BDSGA'
user = 'AdminBDSGA'
password = '1234'


def SetData(self, param, query):
    
    try:
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='
                                 +bd+';UID='+user+';PWD='+password)        
        cursor = conexion.cursor()
        
        cursor.execute(query,param)
        
        conexion.commit()
        
        return 1 #Retorna 1 si la operación se da correctamente
    
    except pyodbc.Error as ex:   
        sqlstate = ex.args[0]
        
        if sqlstate == '23000':
            QMessageBox.warning(self, '¡Ha ocurrido un Error!',  'Infracción de la restricción PRIMARY KEY, No se puede insertar una clave duplicada')
        
        else:
            QMessageBox.warning(self, '¡Error Inesperado!', ex)
            print(ex)
                 
        
    finally:
        conexion.close()
        print("Conexión Finalizada.")
        
        
def GetData(self,query):
    
    try:
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='
                                 +bd+';UID='+user+';PWD='+password)        
        cursor = conexion.cursor()
        
        cursor.execute(query)
        
        array = []
        
        row = cursor.fetchone()
        
        while row:
            array.append(row)
            row = cursor.fetchone()
            
        return array
        
    except pyodbc.Error as ex:   
        QMessageBox.warning(self, '¡Error Inesperado!', ex)
        print(ex)
             
        
    finally:
        conexion.close()
        print("Conexión Finalizada.")
        