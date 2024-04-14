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

        self.addNew.clicked.connect(self.add_new_data)
        self.loadData.clicked.connect(self.load_data)
        self.callData.clicked.connect(self.call_data)
        self.uploadData.clicked.connect(self.upload_data)
        self.deleteData.clicked.connect(self.delete_data)

        
    

    def create_connection(self):
        # Conectar a la base de datos (creará la base de datos si no existe)
        self.connection = sqlite3.connect("cryptotrade.db")

                
        return self.connection

    def add_new_data(self):
        # Crear un cursor para ejecutar comandos SQL
        self.cursor=self.create_connection().cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Datos_Trading (id INTEGER PRIMARY KEY , fecha text, kc_19_1_5 text, ema_12 text, ema_24 text, rsi text, sma_14 text, volumen_operaciones text, patrones_velas text, niveles_soporte_resistencia text, indicador_volumen text, analisis_direccion_mercado text, direccion_mercado_pasado_tiempo text, cambio_porcentual text )")
        self.new_trade = [
                
                self.fecha_LineEdit.text(),  # Fecha y hora de la operación obtenida del QLineEdit
                self.kc_19_1_5LineEdit.text(),  # Valor del indicador Keltner Channel obtenido del QLineEdit
                self.ema_12LineEdit.text(),  # Valor de la media móvil exponencial con período 12 obtenido del QLineEdit
                self.ema_24LineEdit.text(),  # Valor de la media móvil exponencial con período 24 obtenido del QLineEdit
                self.rsiLineEdit.text(),  # Valor del índice de fuerza relativa obtenido del QLineEdit
                self.sma_14LineEdit.text(),  # Valor de la media móvil simple con período 14 obtenido del QLineEdit
                self.volumenOperacionesLineEdit.text(),  # Volumen de operaciones obtenido del QLineEdit
                self.patronesVelaLineEdit.text(),  # Descripción o código de los patrones de velas identificados obtenido del QLineEdit
                self.nSoporteResistenciaLineEdit.text(),  # Descripción o código de los niveles de soporte y resistencia obtenido del QLineEdit
                self.indicadorVolumenLineEdit.text(),  # Valor de algún indicador de volumen adicional obtenido del QLineEdit
                self.analisisDireccionMercadoLineEdit.text(),  # Indicación de si se considera que el mercado está subiendo o bajando obtenido del QLineEdit
                self.direccionMercadoLineEdit.text(),  # Indicación de si el mercado subió o bajó después de un período de tiempo específico obtenido del QLineEdit
                self.cambioPorcentualLineEdit.text()  # Porcentaje de cambio en el precio desde la operación anterior obtenido del QLineEdit
            ]
        # Insertando los valores en la tabla Datos_Trading
        self.cursor.execute("INSERT INTO Datos_Trading VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", self.new_trade)
        print("Nuevo registro insertado: ", self.new_trade)
        last_id = self.cursor.lastrowid
        print("Nuevo registro insertado con ID:", last_id)

        self.connection.commit()
        self.connection.close()
        # Clear line edit text
        self.fecha_LineEdit.clear() 
        self.kc_19_1_5LineEdit.clear()
        self.ema_12LineEdit.clear()  
        self.ema_24LineEdit.clear()  
        self.rsiLineEdit.clear()  
        self.sma_14LineEdit.clear() 
        self.volumenOperacionesLineEdit.clear() 
        self.patronesVelaLineEdit.clear()
        self.nSoporteResistenciaLineEdit.clear()  
        self.indicadorVolumenLineEdit.clear()
        self.analisisDireccionMercadoLineEdit.clear()
        self.direccionMercadoLineEdit.clear()
        self.cambioPorcentualLineEdit.clear() 
   
    def load_data(self):
        self.cursor = self.create_connection().cursor()
        rowCount_sqlquery="SELECT COUNT(*) FROM Datos_Trading"
        trades_sqlquery="SELECT * FROM Datos_Trading"

        #Find the number of rows in the table
        self.cursor.execute(rowCount_sqlquery)
        results= self.cursor.fetchone()

        print("Number of rows: ",results[0])
        self.table.setRowCount(results[0])




        #Add employees from table to Qtable
        table_row=0

        for i in self.cursor.execute(trades_sqlquery):
            self.table.setItem(table_row,0,QTableWidgetItem(str(i[0])))
            self.table.setItem(table_row,1,QTableWidgetItem(str(i[1])))
            self.table.setItem(table_row,2,QTableWidgetItem(i[2]))
            self.table.setItem(table_row,3,QTableWidgetItem(i[3]))
            self.table.setItem(table_row,4,QTableWidgetItem(i[4]))
            self.table.setItem(table_row,5,QTableWidgetItem(i[5]))
            self.table.setItem(table_row,6,QTableWidgetItem(i[6]))
            self.table.setItem(table_row,7,QTableWidgetItem(i[7]))
            self.table.setItem(table_row,8,QTableWidgetItem(i[8]))
            self.table.setItem(table_row,9,QTableWidgetItem(i[9]))
            self.table.setItem(table_row,10,QTableWidgetItem(i[10]))
            self.table.setItem(table_row,11,QTableWidgetItem(i[11]))
            self.table.setItem(table_row,12,QTableWidgetItem(i[12]))
            
           
            table_row = table_row+1 
       
    def call_data(self):
        current_row_index=self.table.currentRow()
        
        
        #Call employee details and assignto variable
        self.fecha_edit = str(self.table.item(current_row_index, 0).text())       
        self.kc_19_1_5_edit=str(self.table.item(current_row_index,1).text())
        self.ema_12_edit=str(self.table.item(current_row_index,2).text())
        self.ema_24_edit=str(self.table.item(current_row_index,3).text())
        self.rsi_edit=str(self.table.item(current_row_index,4).text())
        self.sma_14_edit=str(self.table.item(current_row_index,5).text())
        self.volumenOperaciones_edit=str(self.table.item(current_row_index,6).text())
        self.patronesVela_edit=str(self.table.item(current_row_index,7).text())
        self.indicadorVolumen_edit=str(self.table.item(current_row_index,8).text())
        self.nSoporteResistencia_edit=str(self.table.item(current_row_index,9).text())
        self.analisisDireccionMercado_edit=str(self.table.item(current_row_index,10).text())
        self.direccionMercado_edit=str(self.table.item(current_row_index,11).text())
        self.cambioPorcentual_edit=str(self.table.item(current_row_index,12).text()) 


        #Change QLine edits to above variables
       
        # Estableciendo el formato de la cadena de fecha y hora
        
        self.fecha_LineEdit.setText(self.fecha_edit)
        self.kc_19_1_5LineEdit.setText(self.kc_19_1_5_edit)
        self.ema_12LineEdit.setText(self.ema_12_edit)
        self.ema_24LineEdit.setText(self.ema_24_edit)
        self.rsiLineEdit.setText(self.rsi_edit)
        self.sma_14LineEdit.setText(self.sma_14_edit)
        self.volumenOperacionesLineEdit.setText(self.volumenOperaciones_edit)
        self.patronesVelaLineEdit.setText(self.patronesVela_edit)
        self.indicadorVolumenLineEdit.setText(self.indicadorVolumen_edit)
        self.nSoporteResistenciaLineEdit.setText(self.nSoporteResistencia_edit)
        self.analisisDireccionMercadoLineEdit.setText(self.analisisDireccionMercado_edit)
        self.direccionMercadoLineEdit.setText(self.direccionMercado_edit)
        self.cambioPorcentualLineEdit.setText(self.cambioPorcentual_edit)

    def upload_data(self):
        self.cursor=self.create_connection().cursor()
        #Get current text from QlineEdits

        params=(
            self.fecha_LineEdit.text(),  
            self.kc_19_1_5LineEdit.text(),  
            self.ema_12LineEdit.text(), 
            self.ema_24LineEdit.text(),  
            self.rsiLineEdit.text(),  
            self.sma_14LineEdit.text(),  
            self.volumenOperacionesLineEdit.text(),  
            self.patronesVelaLineEdit.text(), 
            self.nSoporteResistenciaLineEdit.text(),  
            self.indicadorVolumenLineEdit.text(),  
            self.analisisDireccionMercadoLineEdit.text(),  
            self.direccionMercadoLineEdit.text(), 
            self.cambioPorcentualLineEdit.text(),
            self.fecha_LineEdit.text()
                 
            
        )

        #Get Current text from QlineEdits

        self.cursor.execute("UPDATE Datos_Trading SET fecha = ?, kc_19_1_5 = ?, ema_12 = ?, ema_24 = ?, rsi = ?, sma_14 = ?, volumen_operaciones = ?, patrones_velas = ?, niveles_soporte_resistencia = ?, indicador_volumen = ?, analisis_direccion_mercado = ?, direccion_mercado_pasado_tiempo = ?, cambio_porcentual = ? WHERE fecha = ?", params)
        print("The old date was ", self.fecha_edit)
        print("The new daye is ", self.fecha_LineEdit.text())

        #Clear LineEdit Text 

        self.fecha_LineEdit.clear() 
        self.kc_19_1_5LineEdit.clear()
        self.ema_12LineEdit.clear()  
        self.ema_24LineEdit.clear()  
        self.rsiLineEdit.clear()  
        self.sma_14LineEdit.clear() 
        self.volumenOperacionesLineEdit.clear() 
        self.patronesVelaLineEdit.clear()
        self.nSoporteResistenciaLineEdit.clear()  
        self.indicadorVolumenLineEdit.clear()
        self.analisisDireccionMercadoLineEdit.clear()
        self.direccionMercadoLineEdit.clear()
        self.cambioPorcentualLineEdit.clear()


        self.connection.commit()
        self.connection.close

    def delete_data(self):
        self.cursor=self.create_connection().cursor()
        current_row_index=self.table.currentRow()

        print(current_row_index)

        #Call name in row and assign to variable

        fecha_item= str(self.table.item(current_row_index,0).text())

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