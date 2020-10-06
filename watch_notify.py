import time
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from threading import *
class main():
    def __init__(self):

        app = QApplication([])
        app.setQuitOnLastWindowClosed(False)

        icon = QIcon('icon.png')
        tray = QSystemTrayIcon()
        tray.setIcon(icon)
        tray.setVisible(True)
        menu = QMenu()
        self.option1 = QAction("Sreekanth")
        option2 = QAction('Start')
        menu.addAction(self.option1)
        self.option1.setStatusTip("This is bottom")
        menu.addAction(option2)

        self.count=66600
        #option1.setText('hi')
        option2.triggered.connect(self.loop)
        quit = QAction('quit')
        quit.triggered.connect(app.quit)

        menu.addAction(quit)
        #tray.setupui(menu)
        tray.setContextMenu(menu)
        #tray.toolTip("hello")
        #app = QtCore.QCoreApplication(sys.argv)


        #sys.exit(app.exec_())
        app.exec_()
    def timerEvent(self):

        '''
        global ttime
        ttime = ttime.addSecs(1)
        option1.setText(ttime.toString("hh:mm:ss"))
        '''
        a = 5
        while a<7:
            realtime = time.ctime(self.count)
            realtime = realtime.split(" ")
            watch = realtime[4]
            self.option1.setText(watch)
            print(watch)
            self.count+=1
            time.sleep(1)
            a+=1
        else:
            self.call = True
    def loop(self):
        self.call=False
        print('yes')
        thread = Timer(1,self.timerEvent())
        thread.start()
        if self.call == True:
            print(thread.is_alive())
            thread.cancel()
            del thread 
            #print(thread.is_alive())
            print(thread)

main()