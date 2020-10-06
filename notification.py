from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
app = QApplication([])
app.setQuitOnLastWindowClosed(False)

icon = QIcon('icon.png')
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)
def hello(action):
	
menu = QMenu()
option1 = QAction("Sreekanth")
option2 = QAction('GFG')
menu.addAction(option1)
menu.addAction(option2)

option1.setText('hi')
#a=option1.sender()
#option1.triggered.connect(hello)
#print(a)
quit = QAction('quit')
quit.triggered.connect(app.quit)
menu.addAction(quit)
#tray.setupui(menu)
tray.setContextMenu(menu)
#tray.toolTip("hello")
app.exec_()