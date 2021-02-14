from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from caclulator_Maksim_Derkach import Ui_Calculator
app = QtWidgets.QApplication(sys.argv)
Calculator = QtWidgets.QDialog()
ui = Ui_Calculator()
ui.setupUi(Calculator)
Calculator.show()

def action_plus():
    text = ui.label_output.text()
    ui.label_output.setText(text+"+")
def action_equals():
    text = ui.label_output.text()
    ui.label_output.setText(text+"=")

def pushbutton_one():
    text = ui.label_output.text()
    ui.label_output.setText(text + "1")
def pushbutton_two():
    text = ui.label_output.text()
    ui.label_output.setText(text + "2")
#multiply
#divide

ui.pushButton_plus.clicked.connect(action_plus)
ui.pushButton_two.clicked.connect(action_equals)
ui.pushButton_one.clicked.connect(pushbutton_one)
ui.pushButton_two.clicked.connect(pushbutton_two)

sys.exit(app.exec_())