from PyQt5 import QtCore, QtGui, QtWidgets
import sys 
  
class Ui_MainWindow(QtWidgets.QWidget): 
    def setupUi(self, MainWindow): 
        MainWindow.resize(422, 255) 
        self.centralwidget = QtWidgets.QWidget(MainWindow) 
  
        self.pushButton = QtWidgets.QPushButton(self.centralwidget) 
        self.pushButton.setGeometry(QtCore.QRect(160, 130, 93, 28)) 
  
        # For displaying confirmation message along with user's info.  
        self.label = QtWidgets.QLabel(self.centralwidget)     
        self.label.setGeometry(QtCore.QRect(170, 40, 201, 111)) 
  
        # Keeping the text of label empty initially.        
        self.label.setText("")      
  
        MainWindow.setCentralWidget(self.centralwidget) 
        self.takeinputs() 
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 
  
    def retranslateUi(self, MainWindow): 
        _translate = QtCore.QCoreApplication.translate 
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow")) 
        self.pushButton.setText(_translate("MainWindow", "Proceed")) 
        self.pushButton.clicked.connect(self.takeinputs) 
          
    def takeinputs(self): 
        roll, done2 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter your roll:')
        roll1, done3 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter your roll:')
        roll2, done4 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter your roll:')
        if done2 :
             # Showing confirmation message along 
             # with information provided by user.  
             self.label.setText('Information stored Successfully\nName: '+str(roll))    
   
             # Hide the pushbutton after inputs provided by the use. 
             self.pushButton.hide()       
                
               
               
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)  
    MainWindow = QtWidgets.QMainWindow()  
    ui = Ui_MainWindow()  
    ui.setupUi(MainWindow)  
    MainWindow.show()
  
    sys.exit(app.exec_())