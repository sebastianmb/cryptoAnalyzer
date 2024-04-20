import sqlite3
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from ui_sidebar import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow





class MySideBar(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Crypto Analyzer Trade")


        self.icon_name_widget.setHidden(True)

        self.dashboard_1.clicked.connect(self.switch_to_dashboardPage)
        self.dashboard_2.clicked.connect(self.switch_to_dashboardPage)

        self.profile_1.clicked.connect(self.switch_to_profilePage)
        self.profile_2.clicked.connect(self.switch_to_profilePage)

        self.messages_1.clicked.connect(self.switch_to_messagesPage)
        self.messages_2.clicked.connect(self.switch_to_messagesPage)

        self.notifications_1.clicked.connect(self.switch_to_notificationsPage)
        self.notifications_2.clicked.connect(self.switch_to_notificationsPage)

        self.settings_1.clicked.connect(self.switch_to_settingsPage)
        self.settings_2.clicked.connect(self.switch_to_settingsPage)

        self.addNew_2.clicked.connect(self.add_new_data)
        self.loadData_2.clicked.connect(self.load_data)
        self.callData_2.clicked.connect(self.call_data)
        self.uploadData_2.clicked.connect(self.upload_data)
        self.deleteData_2.clicked.connect(self.delete_data)

        
    

    def create_connection(self):
        # Conectar a la base de datos (creará la base de datos si no existe)
        self.connection = sqlite3.connect("cryptotrade.db")

                
        return self.connection

    def add_new_data(self):
        # Crear un cursor para ejecutar comandos SQL
        self.cursor=self.create_connection().cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Datos_Trading (id INTEGER PRIMARY KEY, fecha text, coin text, kc_19_1_5 text, ema_12 text, ema_24 text, rsi text, sma_14 text, volumen_operaciones text, patrones_velas text, niveles_soporte_resistencia text, indicador_volumen text, analisis_direccion_mercado text, direccion_mercado_pasado_tiempo text, cambio_porcentual text)")

        self.new_trade = [
                
                self.fecha_LineEdit_2.text(),  # Fecha y hora de la operación obtenida del QLineEdit
                self.coin_LineEdit_2.text(), 
                self.kc_19_1_5LineEdit_2.text(),  # Valor del indicador Keltner Channel obtenido del QLineEdit
                self.ema_12LineEdit_2.text(),  # Valor de la media móvil exponencial con período 12 obtenido del QLineEdit
                self.ema_24LineEdit_2.text(),  # Valor de la media móvil exponencial con período 24 obtenido del QLineEdit
                self.rsiLineEdit_2.text(),  # Valor del índice de fuerza relativa obtenido del QLineEdit
                self.sma_14LineEdit_2.text(),  # Valor de la media móvil simple con período 14 obtenido del QLineEdit
                self.volumenOperacionesLineEdit_2.text(),  # Volumen de operaciones obtenido del QLineEdit
                self.patronesVelaLineEdit_2.text(),  # Descripción o código de los patrones de velas identificados obtenido del QLineEdit
                self.nSoporteResistenciaLineEdit_2.text(),  # Descripción o código de los niveles de soporte y resistencia obtenido del QLineEdit
                self.indicadorVolumenLineEdit_2.text(),  # Valor de algún indicador de volumen adicional obtenido del QLineEdit
                self.analisisDireccionMercadoLineEdit_2.text(),  # Indicación de si se considera que el mercado está subiendo o bajando obtenido del QLineEdit
                self.direccionMercadoLineEdit_2.text(),  # Indicación de si el mercado subió o bajó después de un período de tiempo específico obtenido del QLineEdit
                self.cambioPorcentualLineEdit_2.text()  # Porcentaje de cambio en el precio desde la operación anterior obtenido del QLineEdit
                
                
            ]

        # Insertando los valores en la tabla Datos_Trading
        self.cursor.execute("INSERT INTO Datos_Trading VALUES (?, ?, ? , ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?)", self.new_trade)
        print("Nuevo registro insertado: ", self.new_trade)
        last_id = self.cursor.lastrowid
        print("Nuevo registro insertado con ID:", last_id)

        self.connection.commit()
        self.connection.close()
        # Clear line edit text
        self.fecha_LineEdit_2.clear() 
        self.coin_LineEdit_2.clear() 
        self.kc_19_1_5LineEdit_2.clear()
        self.ema_12LineEdit_2.clear()  
        self.ema_24LineEdit_2.clear()  
        self.rsiLineEdit_2.clear()  
        self.sma_14LineEdit_2.clear() 
        self.volumenOperacionesLineEdit_2.clear() 
        self.patronesVelaLineEdit_2.clear()
        self.nSoporteResistenciaLineEdit_2.clear()  
        self.indicadorVolumenLineEdit_2.clear()
        self.analisisDireccionMercadoLineEdit_2.clear()
        self.direccionMercadoLineEdit_2.clear()
        self.cambioPorcentualLineEdit_2.clear() 
   
    def load_data(self):
        self.cursor = self.create_connection().cursor()
        rowCount_sqlquery="SELECT COUNT(*) FROM Datos_Trading"
        trades_sqlquery="SELECT * FROM Datos_Trading"

        #Find the number of rows in the table
        self.cursor.execute(rowCount_sqlquery)
        results= self.cursor.fetchone()

        print("Number of rows: ",results[0])
        self.table_2.setRowCount(results[0])




        #Add employees from table to Qtable
        table_row=0

        for i in self.cursor.execute(trades_sqlquery):
            self.table_2.setItem(table_row,0,QTableWidgetItem(str(i[0])))
            self.table_2.setItem(table_row,1,QTableWidgetItem(str(i[1])))
            self.table_2.setItem(table_row,2,QTableWidgetItem(i[2]))
            self.table_2.setItem(table_row,3,QTableWidgetItem(i[3]))
            self.table_2.setItem(table_row,4,QTableWidgetItem(i[4]))
            self.table_2.setItem(table_row,5,QTableWidgetItem(i[5]))
            self.table_2.setItem(table_row,6,QTableWidgetItem(i[6]))
            self.table_2.setItem(table_row,7,QTableWidgetItem(i[7]))
            self.table_2.setItem(table_row,8,QTableWidgetItem(i[8]))
            self.table_2.setItem(table_row,9,QTableWidgetItem(i[9]))
            self.table_2.setItem(table_row,10,QTableWidgetItem(i[10]))
            self.table_2.setItem(table_row,11,QTableWidgetItem(i[11]))
            self.table_2.setItem(table_row,12,QTableWidgetItem(i[12]))
            self.table_2.setItem(table_row,13,QTableWidgetItem(i[13]))
            
           
            table_row = table_row+1 
       
    def call_data(self):
        current_row_index=self.table_2.currentRow()
        
        
        #Call employee details and assignto variable
        self.fecha_edit = str(self.table_2.item(current_row_index, 0).text())
        self.coin_edit = str(self.table_2.item(current_row_index, 6).text())        
        self.kc_19_1_5_edit=str(self.table_2.item(current_row_index,1).text())
        self.ema_12_edit=str(self.table_2.item(current_row_index,2).text())
        self.ema_24_edit=str(self.table_2.item(current_row_index,3).text())
        self.rsi_edit=str(self.table_2.item(current_row_index,4).text())
        self.sma_14_edit=str(self.table_2.item(current_row_index,5).text())
        self.volumenOperaciones_edit=str(self.table_2.item(current_row_index,13).text())
        self.patronesVela_edit=str(self.table_2.item(current_row_index,7).text())
        self.indicadorVolumen_edit=str(self.table_2.item(current_row_index,9).text())
        self.nSoporteResistencia_edit=str(self.table_2.item(current_row_index,8).text())
        self.analisisDireccionMercado_edit=str(self.table_2.item(current_row_index,10).text())
        self.direccionMercado_edit=str(self.table_2.item(current_row_index,11).text())
        self.cambioPorcentual_edit=str(self.table_2.item(current_row_index,12).text())
         


        #Change QLine edits to above variables
       
        
        
        self.fecha_LineEdit_2.setText(self.fecha_edit)
        self.coin_LineEdit_2.setText(self.coin_edit)
        self.kc_19_1_5LineEdit_2.setText(self.kc_19_1_5_edit)
        self.ema_12LineEdit_2.setText(self.ema_12_edit)
        self.ema_24LineEdit_2.setText(self.ema_24_edit)
        self.rsiLineEdit_2.setText(self.rsi_edit)
        self.sma_14LineEdit_2.setText(self.sma_14_edit)
        self.volumenOperacionesLineEdit_2.setText(self.volumenOperaciones_edit)
        self.patronesVelaLineEdit_2.setText(self.patronesVela_edit)
        self.indicadorVolumenLineEdit_2.setText(self.indicadorVolumen_edit)
        self.nSoporteResistenciaLineEdit_2.setText(self.nSoporteResistencia_edit)
        self.analisisDireccionMercadoLineEdit_2.setText(self.analisisDireccionMercado_edit)
        self.direccionMercadoLineEdit_2.setText(self.direccionMercado_edit)
        self.cambioPorcentualLineEdit_2.setText(self.cambioPorcentual_edit)

    def upload_data(self):
        self.cursor=self.create_connection().cursor()
        #Get current text from QlineEdits

        params = (
            self.coin_LineEdit_2.text(),  
            self.kc_19_1_5LineEdit_2.text(),  
            self.ema_12LineEdit_2.text(), 
            self.ema_24LineEdit_2.text(),  
            self.rsiLineEdit_2.text(),  
            self.sma_14LineEdit_2.text(),  
            self.volumenOperacionesLineEdit_2.text(),  
            self.patronesVelaLineEdit_2.text(), 
            self.nSoporteResistenciaLineEdit_2.text(),  
            self.indicadorVolumenLineEdit_2.text(),  
            self.analisisDireccionMercadoLineEdit_2.text(),  
            self.direccionMercadoLineEdit_2.text(), 
            self.cambioPorcentualLineEdit_2.text(),
            self.fecha_LineEdit_2.text()            
        )

        # Ejecutar la consulta de actualización
        self.cursor.execute("UPDATE Datos_Trading SET coin = ?, kc_19_1_5 = ?, ema_12 = ?, ema_24 = ?, rsi = ?, sma_14 = ?, volumen_operaciones = ?, patrones_velas = ?, niveles_soporte_resistencia = ?, indicador_volumen = ?, analisis_direccion_mercado = ?, direccion_mercado_pasado_tiempo = ?, cambio_porcentual = ? WHERE fecha = ?", params)

        print("The old date was ", self.fecha_edit)
        print("The new daye is ", self.fecha_LineEdit_2.text())

        #Clear LineEdit Text 

        self.fecha_LineEdit_2.clear() 
        self.coin_LineEdit_2.clear() 
        self.kc_19_1_5LineEdit_2.clear()
        self.ema_12LineEdit_2.clear()  
        self.ema_24LineEdit_2.clear()  
        self.rsiLineEdit_2.clear()  
        self.sma_14LineEdit_2.clear() 
        self.volumenOperacionesLineEdit_2.clear() 
        self.patronesVelaLineEdit_2.clear()
        self.nSoporteResistenciaLineEdit_2.clear()  
        self.indicadorVolumenLineEdit_2.clear()
        self.analisisDireccionMercadoLineEdit_2.clear()
        self.direccionMercadoLineEdit_2.clear()
        self.cambioPorcentualLineEdit_2.clear() 


        self.connection.commit()
        self.connection.close

    def delete_data(self):
        self.cursor=self.create_connection().cursor()
        current_row_index=self.table_2.currentRow()

        print(current_row_index)

        #Call name in row and assign to variable

        fecha_item= str(self.table_2.item(current_row_index,0).text())

        if current_row_index < 0:
            Warning= QMessageBox.warning(self, 'Warning', 'Please select a record to delete')
        else:
            message=QMessageBox.question(self,'Confirmation','Are you sure you want to delete the selected row? ',QMessageBox.StandardButton.Yes| QMessageBox.StandardButton.No)

        if message == QMessageBox.StandardButton.Yes:
            sqlquery="DELETE FROM Datos_Trading WHERE fecha=?"
            self.cursor.execute(sqlquery,(fecha_item,))
            print("You deleted: ",fecha_item)

            self.connection.commit()
            self.connection.close

    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def switch_to_profilePage(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def switch_to_messagesPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_notificationsPage(self):
        self.stackedWidget.setCurrentIndex(3)
    
    def switch_to_settingsPage(self):
        self.stackedWidget.setCurrentIndex(4)