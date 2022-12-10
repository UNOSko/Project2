# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autoclicker.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import keyboard, mouse, time


class Ui_MainWindow(object):

    inputInterval = 0.01
    onState = False
    autoInput = 'q'
    hotkeyEnabled = True
    hotkey = '`'
    locX = 1
    locY = 1
    repeat = 10
    hotkeyKey = True

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 390, 651, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.startKey = QtWidgets.QPushButton(self.centralwidget)
        self.startKey.setGeometry(QtCore.QRect(10, 410, 611, 61))
        self.startKey.setObjectName("startKey")
        self.hotkeyEnter = QtWidgets.QLineEdit(self.centralwidget)
        self.hotkeyEnter.setGeometry(QtCore.QRect(290, 260, 21, 20))
        self.hotkeyEnter.setMaxLength(1)
        self.hotkeyEnter.setObjectName("hotkeyEnter")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(110, 220, 531, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.menuLabel = QtWidgets.QLabel(self.centralwidget)
        self.menuLabel.setGeometry(QtCore.QRect(40, 220, 71, 20))
        self.menuLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.menuLabel.setObjectName("menuLabel")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(-10, 220, 51, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.hotkeyChange = QtWidgets.QPushButton(self.centralwidget)
        self.hotkeyChange.setGeometry(QtCore.QRect(10, 250, 101, 41))
        self.hotkeyChange.setObjectName("hotkeyChange")
        self.hotkeyReset = QtWidgets.QPushButton(self.centralwidget)
        self.hotkeyReset.setGeometry(QtCore.QRect(10, 300, 101, 41))
        self.hotkeyReset.setObjectName("hotkeyReset")
        self.hotkeyShift = QtWidgets.QRadioButton(self.centralwidget)
        self.hotkeyShift.setGeometry(QtCore.QRect(280, 340, 82, 17))
        self.hotkeyShift.setObjectName("hotkeyShift")
        self.extraButtonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.extraButtonGroup.setObjectName("extraButtonGroup")
        self.extraButtonGroup.addButton(self.hotkeyShift)
        self.hotkeyAlt = QtWidgets.QRadioButton(self.centralwidget)
        self.hotkeyAlt.setGeometry(QtCore.QRect(190, 370, 82, 17))
        self.hotkeyAlt.setObjectName("hotkeyAlt")
        self.extraButtonGroup.addButton(self.hotkeyAlt)
        self.hotkeyCtrl = QtWidgets.QRadioButton(self.centralwidget)
        self.hotkeyCtrl.setGeometry(QtCore.QRect(280, 370, 82, 17))
        self.hotkeyCtrl.setObjectName("hotkeyCtrl")
        self.extraButtonGroup.addButton(self.hotkeyCtrl)
        self.hotkeyNone = QtWidgets.QRadioButton(self.centralwidget)
        self.hotkeyNone.setGeometry(QtCore.QRect(190, 340, 82, 17))
        self.hotkeyNone.setChecked(True)
        self.hotkeyNone.setObjectName("hotkeyNone")
        self.extraButtonGroup.addButton(self.hotkeyNone)
        self.hotkeyRemove = QtWidgets.QPushButton(self.centralwidget)
        self.hotkeyRemove.setGeometry(QtCore.QRect(10, 350, 101, 41))
        self.hotkeyRemove.setObjectName("hotkeyRemove")
        self.menuLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.menuLabel2.setGeometry(QtCore.QRect(190, 310, 131, 16))
        self.menuLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.menuLabel2.setObjectName("menuLabel2")
        self.menuLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.menuLabel1.setGeometry(QtCore.QRect(200, 260, 81, 21))
        self.menuLabel1.setObjectName("menuLabel1")
        self.menuLabel3 = QtWidgets.QLabel(self.centralwidget)
        self.menuLabel3.setGeometry(QtCore.QRect(400, 280, 111, 41))
        self.menuLabel3.setAlignment(QtCore.Qt.AlignCenter)
        self.menuLabel3.setObjectName("menuLabel3")
        self.hotkeyDisplay = QtWidgets.QLabel(self.centralwidget)
        self.hotkeyDisplay.setGeometry(QtCore.QRect(400, 333, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hotkeyDisplay.setFont(font)
        self.hotkeyDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.hotkeyDisplay.setObjectName("hotkeyDisplay")
        self.menuLabel4 = QtWidgets.QLabel(self.centralwidget)
        self.menuLabel4.setGeometry(QtCore.QRect(20, 140, 47, 13))
        self.menuLabel4.setObjectName("menuLabel4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(300, 147, 31, 81))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(70, 140, 261, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 140, 61, 16))
        self.label.setObjectName("label")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(390, 140, 241, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(0, 140, 20, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.mouseLeft = QtWidgets.QRadioButton(self.centralwidget)
        self.mouseLeft.setGeometry(QtCore.QRect(50, 170, 82, 17))
        self.mouseLeft.setChecked(True)
        self.mouseLeft.setAutoExclusive(True)
        self.mouseLeft.setObjectName("mouseLeft")
        self.clickTypeGroup = QtWidgets.QButtonGroup(MainWindow)
        self.clickTypeGroup.setObjectName("clickTypeGroup")
        self.clickTypeGroup.addButton(self.mouseLeft)
        self.characterChoice = QtWidgets.QRadioButton(self.centralwidget)
        self.characterChoice.setGeometry(QtCore.QRect(140, 180, 82, 17))
        self.characterChoice.setObjectName("characterChoice")
        self.clickTypeGroup.addButton(self.characterChoice)
        self.characterRepeat = QtWidgets.QLineEdit(self.centralwidget)
        self.characterRepeat.setGeometry(QtCore.QRect(220, 178, 21, 20))
        self.characterRepeat.setMaxLength(1)
        self.characterRepeat.setAlignment(QtCore.Qt.AlignCenter)
        self.characterRepeat.setObjectName("characterRepeat")
        self.mouseRight = QtWidgets.QRadioButton(self.centralwidget)
        self.mouseRight.setGeometry(QtCore.QRect(50, 190, 82, 17))
        self.mouseRight.setObjectName("mouseRight")
        self.clickTypeGroup.addButton(self.mouseRight)
        self.repeatFinite = QtWidgets.QRadioButton(self.centralwidget)
        self.repeatFinite.setGeometry(QtCore.QRect(330, 190, 71, 17))
        self.repeatFinite.setObjectName("repeatFinite")
        self.clickAmountGroup = QtWidgets.QButtonGroup(MainWindow)
        self.clickAmountGroup.setObjectName("clickAmountGroup")
        self.clickAmountGroup.addButton(self.repeatFinite)
        self.repeatInfinite = QtWidgets.QRadioButton(self.centralwidget)
        self.repeatInfinite.setGeometry(QtCore.QRect(330, 170, 200, 17))
        self.repeatInfinite.setChecked(True)
        self.repeatInfinite.setObjectName("repeatInfinite")
        self.clickAmountGroup.addButton(self.repeatInfinite)
        self.repeatTimes = QtWidgets.QLineEdit(self.centralwidget)
        self.repeatTimes.setGeometry(QtCore.QRect(400, 190, 51, 20))
        self.repeatTimes.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.repeatTimes.setObjectName("repeatTimes")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 190, 51, 16))
        self.label_2.setObjectName("label_2")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(115, 80, 521, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 80, 71, 20))
        self.label_3.setObjectName("label_3")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(-10, 80, 58, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.onMouse = QtWidgets.QRadioButton(self.centralwidget)
        self.onMouse.setGeometry(QtCore.QRect(50, 110, 82, 17))
        self.onMouse.setChecked(True)
        self.onMouse.setObjectName("onMouse")
        self.clickLocationGroup = QtWidgets.QButtonGroup(MainWindow)
        self.clickLocationGroup.setObjectName("clickLocationGroup")
        self.clickLocationGroup.addButton(self.onMouse)
        self.chosenLocation = QtWidgets.QRadioButton(self.centralwidget)
        self.chosenLocation.setGeometry(QtCore.QRect(220, 110, 101, 17))
        self.chosenLocation.setObjectName("chosenLocation")
        self.clickLocationGroup.addButton(self.chosenLocation)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 110, 16, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 110, 21, 16))
        self.label_5.setObjectName("label_5")
        self.locationX = QtWidgets.QLineEdit(self.centralwidget)
        self.locationX.setGeometry(QtCore.QRect(350, 108, 61, 20))
        self.locationX.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.locationX.setObjectName("locationX")
        self.locationY = QtWidgets.QLineEdit(self.centralwidget)
        self.locationY.setGeometry(QtCore.QRect(440, 108, 61, 20))
        self.locationY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.locationY.setObjectName("locationY")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(112, 10, 511, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 10, 61, 16))
        self.label_6.setObjectName("label_6")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(-10, 10, 60, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 40, 31, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(170, 40, 41, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(290, 40, 41, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(420, 40, 61, 16))
        self.label_10.setObjectName("label_10")
        self.hours = QtWidgets.QLineEdit(self.centralwidget)
        self.hours.setGeometry(QtCore.QRect(90, 40, 41, 20))
        self.hours.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hours.setObjectName("hours")
        self.minutes = QtWidgets.QLineEdit(self.centralwidget)
        self.minutes.setGeometry(QtCore.QRect(210, 40, 41, 20))
        self.minutes.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.minutes.setObjectName("minutes")
        self.seconds = QtWidgets.QLineEdit(self.centralwidget)
        self.seconds.setGeometry(QtCore.QRect(340, 40, 41, 20))
        self.seconds.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.seconds.setObjectName("seconds")
        self.miliseconds = QtWidgets.QLineEdit(self.centralwidget)
        self.miliseconds.setGeometry(QtCore.QRect(480, 40, 41, 20))
        self.miliseconds.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.miliseconds.setObjectName("miliseconds")
        self.locationPick = QtWidgets.QPushButton(self.centralwidget)
        self.locationPick.setGeometry(QtCore.QRect(510, 107, 71, 22))
        self.locationPick.setObjectName("locationPick")
        self.line.raise_()
        self.startKey.raise_()
        self.hotkeyEnter.raise_()
        self.line_2.raise_()
        self.menuLabel.raise_()
        self.line_3.raise_()
        self.hotkeyChange.raise_()
        self.hotkeyReset.raise_()
        self.hotkeyShift.raise_()
        self.hotkeyAlt.raise_()
        self.hotkeyCtrl.raise_()
        self.hotkeyNone.raise_()
        self.hotkeyRemove.raise_()
        self.menuLabel2.raise_()
        self.menuLabel1.raise_()
        self.menuLabel3.raise_()
        self.hotkeyDisplay.raise_()
        self.menuLabel4.raise_()
        self.line_5.raise_()
        self.line_4.raise_()
        self.label.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.mouseLeft.raise_()
        self.characterChoice.raise_()
        self.characterRepeat.raise_()
        self.mouseRight.raise_()
        self.repeatFinite.raise_()
        self.repeatInfinite.raise_()
        self.repeatTimes.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.line_8.raise_()
        self.line_9.raise_()
        self.onMouse.raise_()
        self.chosenLocation.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.locationX.raise_()
        self.locationY.raise_()
        self.line_10.raise_()
        self.label_6.raise_()
        self.line_11.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.hours.raise_()
        self.minutes.raise_()
        self.seconds.raise_()
        self.miliseconds.raise_()
        self.locationPick.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.startKey.clicked.connect(self.start)
        self.hotkeyChange.clicked.connect(self.hotkeySave)
        self.hotkeyReset.clicked.connect(self.hotkeyBack)
        self.hotkeyRemove.clicked.connect(self.hotkeyOff)
        self.locationPick.clicked.connect(self.mouseLocation)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startKey.setText(_translate("MainWindow", "Start Autoclicker"))
        self.hotkeyEnter.setText(_translate("MainWindow", "`"))
        self.menuLabel.setText(_translate("MainWindow", "Hotkey editor"))
        self.hotkeyChange.setText(_translate("MainWindow", "Change Hotkey"))
        self.hotkeyReset.setText(_translate("MainWindow", "Reset Hotkey"))
        self.hotkeyShift.setText(_translate("MainWindow", "Shift"))
        self.hotkeyAlt.setText(_translate("MainWindow", "Alt"))
        self.hotkeyCtrl.setText(_translate("MainWindow", "Ctrl"))
        self.hotkeyNone.setText(_translate("MainWindow", "None"))
        self.hotkeyRemove.setText(_translate("MainWindow", "Remove Hotkey"))
        self.menuLabel2.setText(_translate("MainWindow", "Special Button"))
        self.menuLabel1.setText(_translate("MainWindow", "Hotkey button:"))
        self.menuLabel3.setText(_translate("MainWindow", "Current Hotkey:"))
        self.hotkeyDisplay.setText(_translate("MainWindow", self.hotkey))
        self.menuLabel4.setText(_translate("MainWindow", "Click Type"))
        self.label.setText(_translate("MainWindow", "Click Amount"))
        self.mouseLeft.setText(_translate("MainWindow", "Left Click"))
        self.characterChoice.setText(_translate("MainWindow", "Character:"))
        self.characterRepeat.setText(_translate("MainWindow", "q"))
        self.mouseRight.setText(_translate("MainWindow", "Right Click"))
        self.repeatFinite.setText(_translate("MainWindow", "Repeat:"))
        self.repeatInfinite.setText(_translate("MainWindow", "Repeat While Holding Down Hotkey"))
        self.repeatTimes.setText(_translate("MainWindow", "10"))
        self.label_2.setText(_translate("MainWindow", "Time(s)"))
        self.label_3.setText(_translate("MainWindow", "Click Location"))
        self.onMouse.setText(_translate("MainWindow", "On Mouse"))
        self.chosenLocation.setText(_translate("MainWindow", "Exact Location"))
        self.label_4.setText(_translate("MainWindow", "X:"))
        self.label_5.setText(_translate("MainWindow", "Y: "))
        self.locationX.setText(_translate("MainWindow", "1"))
        self.locationY.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "Click Interval"))
        self.label_7.setText(_translate("MainWindow", "Hours"))
        self.label_8.setText(_translate("MainWindow", "Minutes"))
        self.label_9.setText(_translate("MainWindow", "Seconds"))
        self.label_10.setText(_translate("MainWindow", "Miliseconds"))
        self.hours.setText(_translate("MainWindow", "0"))
        self.minutes.setText(_translate("MainWindow", "0"))
        self.seconds.setText(_translate("MainWindow", "0"))
        self.miliseconds.setText(_translate("MainWindow", "10"))
        self.locationPick.setText(_translate("MainWindow", "Pick Location"))


    def mouseLocation(self):
        keyboard.wait(self.hotkey)
        pos = mouse.get_position()
        self.locX = pos[0]
        self.locY = pos[1]
        self.locationX.setText(str(self.locX))
        self.locationY.setText(str(self.locY))

    def hotkeyOff(self):
        self.hotkey = ''
        self.hotkeyEnter.setText('')
        self.hotkeyNone.setChecked(True)
        self.hotkeyDisplay.setText('None')

    def hotkeyBack(self):
        self.hotkey = '`'
        self.hotkeyEnter.setText('`')
        self.hotkeyNone.setChecked(True)
        self.hotkeyDisplay.setText(self.hotkey)

    def hotkeySave(self):
        self.hotkey = self.hotkeyEnter.text()
        if self.hotkeyNone.isChecked():
            self.hotkeyDisplay.setText(self.hotkey)
        if self.hotkeyShift.isChecked():
            self.hotkey = 'shift'
            self.hotkeyEnter.setText('')
            self.hotkeyDisplay.setText("Shift")
        elif self.hotkeyCtrl.isChecked():
            self.hotkey = 'ctrl'
            self.hotkeyEnter.setText('')
            self.hotkeyDisplay.setText("Ctrl")
        elif self.hotkeyAlt.isChecked():
            self.hotkey = 'alt'
            self.hotkeyEnter.setText('')
            self.hotkeyDisplay.setText("Alt")
        elif self.hotkeyEnter.text() == '':
            self.hotkeyNone.setChecked(True)
            self.hotkeyDisplay.setText('None')

    def start(self):
        if self.onState:
            pass
        else:
            self.onState = True
            try:
                int(self.miliseconds.text())
                int(self.seconds.text())
                int(self.minutes.text())
                int(self.hours.text())
            except Exception:
                self.miliseconds.setText('10')
                self.seconds.setText('0')
                self.minutes.setText('0')
                self.hours.setText('0')

            self.inputInterval = (int(self.miliseconds.text()) * 0.001) + int(self.seconds.text()) + (int(self.minutes.text()) * 60) + (int(self.hours.text()) * 3600)

            if self.chosenLocation.isChecked():

                try:
                    int(self.locationX.text())
                    int(self.locationY.text())
                except Exception:
                    self.locationX.setText('1')
                    self.locationY.setText('1')

                self.locX = int(self.locationX.text())
                self.locY = int(self.locationY.text())

                if self.repeatInfinite.isChecked():
                    keyboard.wait(self.hotkey)
                    while keyboard.is_pressed(self.hotkey):
                        if self.mouseLeft.isChecked():
                            mouse.move(self.locX, self.locY, absolute=True, duration=0)
                            mouse.click('left')
                        if self.mouseRight.isChecked():
                            mouse.move(self.locX, self.locY, absolute=True, duration=0)
                            mouse.click('right')
                        if self.characterChoice.isChecked():
                            keyboard.send(self.characterRepeat.text())
                        time.sleep(self.inputInterval)

                if self.repeatFinite.isChecked():
                    for i in range(int(self.repeatTimes.text()) - 1):
                        if self.mouseLeft.isChecked():
                            mouse.move(self.locX, self.locY, absolute=True, duration=0)
                            mouse.click('left')
                        if self.mouseRight.isChecked():
                            mouse.move(self.locX, self.locY, absolute=True, duration=0)
                            mouse.click('right')
                        if self.characterChoice.isChecked():
                            keyboard.send(self.characterRepeat.text())
                        time.sleep(self.inputInterval)

            if self.onMouse.isChecked():
                if self.repeatInfinite.isChecked():
                    keyboard.wait(self.hotkey)
                    while keyboard.is_pressed(self.hotkey):
                        if self.mouseLeft.isChecked():
                            mouse.click('left')
                        if self.mouseRight.isChecked():
                            mouse.click('right')
                        if self.characterChoice.isChecked():
                            keyboard.send(self.characterRepeat.text())
                        time.sleep(self.inputInterval)


                if self.repeatFinite.isChecked():

                    for i in range(int(self.repeatTimes.text()) - 1):
                        if self.mouseLeft.isChecked():
                            mouse.click('left')
                        if self.mouseRight.isChecked():
                            mouse.click('right')
                        if self.characterChoice.isChecked():
                            keyboard.send(self.characterRepeat.text())
                        time.sleep(self.inputInterval)
            self.onState = False





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
