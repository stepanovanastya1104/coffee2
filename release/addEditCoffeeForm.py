# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(783, 581)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 269, 801, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.add_btn = QtWidgets.QPushButton(Form)
        self.add_btn.setGeometry(QtCore.QRect(330, 250, 75, 23))
        self.add_btn.setObjectName("add_btn")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.name_coff = QtWidgets.QLineEdit(Form)
        self.name_coff.setGeometry(QtCore.QRect(150, 20, 291, 20))
        self.name_coff.setObjectName("name_coff")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.degree_of_roasting_coff = QtWidgets.QLineEdit(Form)
        self.degree_of_roasting_coff.setGeometry(QtCore.QRect(150, 60, 291, 20))
        self.degree_of_roasting_coff.setObjectName("degree_of_roasting_coff")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.type_coff = QtWidgets.QLineEdit(Form)
        self.type_coff.setGeometry(QtCore.QRect(150, 100, 291, 20))
        self.type_coff.setObjectName("type_coff")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.taste_coff = QtWidgets.QLineEdit(Form)
        self.taste_coff.setGeometry(QtCore.QRect(150, 140, 291, 20))
        self.taste_coff.setObjectName("taste_coff")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 180, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.price_coff = QtWidgets.QLineEdit(Form)
        self.price_coff.setGeometry(QtCore.QRect(150, 180, 291, 20))
        self.price_coff.setObjectName("price_coff")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(30, 220, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.volume_coff = QtWidgets.QLineEdit(Form)
        self.volume_coff.setGeometry(QtCore.QRect(150, 220, 291, 20))
        self.volume_coff.setObjectName("volume_coff")
        self.mistake = QtWidgets.QLabel(Form)
        self.mistake.setGeometry(QtCore.QRect(490, 90, 251, 91))
        self.mistake.setText("")
        self.mistake.setObjectName("mistake")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 320, 21, 21))
        self.label_8.setObjectName("label_8")
        self.id_coffe = QtWidgets.QLineEdit(Form)
        self.id_coffe.setGeometry(QtCore.QRect(60, 320, 381, 20))
        self.id_coffe.setObjectName("id_coffe")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 360, 761, 71))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.save_btn = QtWidgets.QPushButton(Form)
        self.save_btn.setGeometry(QtCore.QRect(320, 480, 121, 31))
        self.save_btn.setObjectName("save_btn")
        self.show_btn = QtWidgets.QPushButton(Form)
        self.show_btn.setGeometry(QtCore.QRect(520, 310, 121, 31))
        self.show_btn.setObjectName("show_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"))
        self.add_btn.setText(_translate("Form", "Добавить"))
        self.label_2.setText(_translate("Form", "название сорта:"))
        self.label_3.setText(_translate("Form", "степень обжарки:"))
        self.label_4.setText(_translate("Form", "молотый/в зернах:"))
        self.label_5.setText(_translate("Form", "описание вкуса:"))
        self.label_6.setText(_translate("Form", "цена:"))
        self.label_7.setText(_translate("Form", "объем упаковки:"))
        self.label_8.setText(_translate("Form", "id:"))
        self.save_btn.setText(_translate("Form", "Сохранить"))
        self.show_btn.setText(_translate("Form", "Показать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
