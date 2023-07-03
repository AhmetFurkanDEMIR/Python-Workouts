from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import PyQt5
from HandPos import HandPos
import os
from pathlib import Path

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.fspath(
    Path(PyQt5.__file__).resolve().parent / "Qt5" / "plugins"
)

Path = "{}/png.png".format(os.getcwd())

class Ui_MainWindow(QtWidgets.QMainWindow):

    def setupUi(self):

        self.handPos = HandPos()
        self.setWindowIcon(QtGui.QIcon(Path))


        self.setObjectName("MainWindow")

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setLineWidth(1)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.icon = QtGui.QIcon(Path)

        # Create the tray
        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)

        # Create the menu
        self.menu = QtWidgets.QMenu()

        # Add a Quit option to the menu.
        self.quit = QtWidgets.QAction("Quit")
        self.quit.triggered.connect(app.quit)
        self.menu.addAction(self.quit)

        # Add the menu to the tray
        self.tray.setContextMenu(self.menu)


        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Hand Keyboard", "Hand Keyboard"))

        self.timer=QTimer()
        self.timer.timeout.connect(self.readFrame)
        self.timer.start(30)

    def readFrame(self):

        self.frame, x, y = self.handPos.capRead()

        self.qimg = QtGui.QImage(self.frame,self.frame.shape[1], self.frame.shape[0], QtGui.QImage.Format_ARGB32)

        self.pixmapb = QtGui.QPixmap.fromImage(self.qimg)
        self.label.setPixmap(self.pixmapb)
 
        if len(self.frame) == 0:

            self.hide()


        else:

            self.show()

            self.move(x+3, y+3)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
