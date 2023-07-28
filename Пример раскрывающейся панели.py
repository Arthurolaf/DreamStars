import sys   
from PyQt5 import QtCore, QtGui, QtWidgets    
from PyQt5.QtGui import QColor, QIcon 
from PyQt5.uic import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.menuvisible = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 653)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.263699 rgba(28, 33, 44, 255), stop:0.784247 rgba(41, 48, 60, 255));")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.root = QtWidgets.QFrame(self.centralwidget)
        self.root.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.root.setFrameShadow(QtWidgets.QFrame.Raised)
        self.root.setObjectName("root")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.root)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_ = QtWidgets.QFrame(self.root)
        self.frame_.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_.setStyleSheet("")
        self.frame_.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_.setObjectName("frame_")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_)
        self.frame_2.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton.setStyleSheet("border:none;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Изображения/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(55, 55))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout_3.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(609, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(self.frame_)
        self.frame_3.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.miniBtn = QtWidgets.QPushButton(self.frame_3)
        self.miniBtn.setMinimumSize(QtCore.QSize(26, 26))
        self.miniBtn.setMaximumSize(QtCore.QSize(26, 26))
        self.miniBtn.setStyleSheet("QPushButton{\n"
"    background-color:rgb(97, 97, 97);\n"
"    border:none;\n"
"    border-radius: 13;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(134, 134, 134);\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.miniBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Изображения/minus (2).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.miniBtn.setIcon(icon1)
        self.miniBtn.setIconSize(QtCore.QSize(22, 22))
        self.miniBtn.setObjectName("miniBtn")
        self.horizontalLayout_2.addWidget(self.miniBtn)
        self.closeBtn = QtWidgets.QPushButton(self.frame_3)
        self.closeBtn.setMinimumSize(QtCore.QSize(26, 26))
        self.closeBtn.setMaximumSize(QtCore.QSize(26, 26))
        self.closeBtn.setStyleSheet("QPushButton{\n"
"    background-color:rgb(97, 97, 97);\n"
"    border:none;\n"
"    border-radius: 13;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(134, 134, 134);\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.closeBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Изображения/close (3).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon2)
        self.closeBtn.setIconSize(QtCore.QSize(22, 22))
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_2.addWidget(self.closeBtn)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.frame_)
        self.frame_5 = QtWidgets.QFrame(self.root)
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QtWidgets.QFrame(self.frame_5)
        self.frame.setMaximumWidth(48)
        self.frame.setMinimumSize(QtCore.QSize(48, 589))
        self.frame.setMaximumSize(QtCore.QSize(200, 16000))
        self.frame.setStyleSheet("background-color: rgb(58, 65, 82);\n"
"border-radius: 23;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.menu = QtWidgets.QPushButton(self.frame)
        self.menu.clicked.connect(self.showmenu)  # Показываем окно
        self.menu.setMinimumSize(QtCore.QSize(30, 25))
        self.menu.setMaximumSize(QtCore.QSize(16000, 25))
        self.menu.setStyleSheet("border:none;")
        self.menu.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/Изображения/5050.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu.setIcon(icon3)
        self.menu.setIconSize(QtCore.QSize(35, 34))
        self.menu.setObjectName("menu")
        self.verticalLayout_4.addWidget(self.menu)
        spacerItem2 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setMinimumSize(QtCore.QSize(180, 80))
        self.frame_6.setMaximumSize(QtCore.QSize(180, 80))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(0, 9, 31, -1)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/assets/document.svg"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setMinimumSize(QtCore.QSize(30, 30))
        self.label_3.setMaximumSize(QtCore.QSize(30, 30))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/Изображения/document.svg"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.weapon = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weapon.sizePolicy().hasHeightForWidth())
        self.weapon.setSizePolicy(sizePolicy)
        self.weapon.setMinimumSize(QtCore.QSize(111, 40))
        self.weapon.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.weapon.setFont(font)
        self.weapon.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    color: rgb(78, 75, 94);      \n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"   \n"
"    \n"
"    \n"
"    color: rgb(168, 168, 168);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"   \n"
"    \n"
"    color: rgb(214, 214, 214);\n"
"    }")
        self.weapon.setInputMethodHints(QtCore.Qt.ImhNone)
        self.weapon.setIconSize(QtCore.QSize(35, 35))
        self.weapon.setAutoExclusive(False)
        self.weapon.setObjectName("weapon")
        self.horizontalLayout_4.addWidget(self.weapon)
        self.verticalLayout_4.addWidget(self.frame_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 338, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.spravka = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spravka.sizePolicy().hasHeightForWidth())
        self.spravka.setSizePolicy(sizePolicy)
        self.spravka.setMinimumSize(QtCore.QSize(170, 40))
        self.spravka.setMaximumSize(QtCore.QSize(170, 40))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.spravka.setFont(font)
        self.spravka.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    color: rgb(78, 75, 94);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    padding: 5px;\n"
"\n"
"    }\n"
"QPushButton:hover {\n"
"   \n"
"    \n"
"    color: rgb(168, 168, 168);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"   \n"
"    color: rgb(214, 214, 214);\n"
"    }")
        self.spravka.setInputMethodHints(QtCore.Qt.ImhNone)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/Nikita_Pfeyfer4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.spravka.setIcon(icon4)
        self.spravka.setIconSize(QtCore.QSize(55, 55))
        self.spravka.setAutoExclusive(False)
        self.spravka.setObjectName("spravka")
        self.verticalLayout_4.addWidget(self.spravka)
        self.horizontalLayout_5.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.root)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Apex - Helper</span></p></body></html>"))
        self.weapon.setText(_translate("MainWindow", "Weapons"))
        self.spravka.setText(_translate("MainWindow", "Reference"))



    def showmenu(self):
        self.anim = QPropertyAnimation(self.frame, b'size')
        self.anim.setDuration(250)
        if self.menuvisible==0:
            self.anim.setStartValue(QSize(48,589))
            self.anim.setEndValue(QSize(200, 589))
            self.menuvisible = 1
        else:
            self.anim.setStartValue(QSize(200,589))
            self.anim.setEndValue(QSize(48, 589))
            self.menuvisible = 0
            #self.anim.finished.connect(self.hidemenu)
        self.frame.show()
        self.anim.start()
#import icons_rc




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())