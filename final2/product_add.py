import product_db
import warehouse_db
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QLabel,QInputDialog
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QDialog, QIcon, QDesktopWidget, QPixmap
import shutil 
import os 
import ntpath

class product_add(QDialog):
    def __init__(self):
       	super().__init__()
        self.setWindowTitle('Thông tin sản phẩm mới')
        self.init_ui()
        
    def init_ui(self):       
        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText('Mã sản phẩm')
        self.l1.move(110, 110)
        self.line_edit1 = QtWidgets.QLineEdit(self)
        self.line_edit1.setGeometry(200, 100, 200, 30)
        
        self.l2 = QtWidgets.QLabel(self)
        self.l2.setText('Tên sản phẩm')
        self.l2.move(110, 160)
        self.line_edit2 = QtWidgets.QLineEdit(self)
        self.line_edit2.setGeometry(200, 150, 200, 30)
        
        self.l3 = QtWidgets.QLabel(self)
        self.l3.setText('Danh mục')
        self.l3.move(110, 210)
        self.line_edit3 = QtWidgets.QLineEdit(self)
        self.line_edit3.setGeometry(200, 200, 200, 30)
        
        self.l4 = QtWidgets.QLabel(self)
        self.l4.setText('Hình ảnh')
        self.l4.move(110, 260)
        self.line_edit4 = QtWidgets.QLineEdit(self)
        self.line_edit4.setGeometry(200, 250, 200, 30)

        self.button_1 = QtWidgets.QPushButton('Get',self)
        self.button_1.setGeometry(410, 250, 50, 30)
        self.button_1.clicked.connect(self.get_image)
        
        self.l5 = QtWidgets.QLabel(self)
        self.l5.setText('Nhãn hiệu')
        self.l5.move(110, 310)
        self.line_edit5 = QtWidgets.QLineEdit(self)
        self.line_edit5.setGeometry(200, 300, 200, 30)
        
        self.l6 = QtWidgets.QLabel(self)
        self.l6.setText('Giá')
        self.l6.move(110, 360)
        self.line_edit6 = QtWidgets.QLineEdit(self)
        self.line_edit6.setGeometry(200, 350, 200, 30)

        self.l7 = QtWidgets.QLabel(self)
        self.l7.setText('Mô tả')
        self.l7.move(110, 410)
        self.line_edit7 = QtWidgets.QLineEdit(self)
        self.line_edit7.setGeometry(200, 400, 200, 30)
        
        self.button = QtWidgets.QPushButton('Lưu',self)
        self.button.setGeometry(200, 450, 100, 30)
        self.button.clicked.connect(self.insert)
    
    def insert(self):
        product_list, product_count = product_db.select(self.line_edit1.text())
        warehouse_list , warehouse_count = warehouse_db.select(self.line_edit1.text())
        if product_count != 0:
            self.error = error_form('Mã sản phẩm đã tồn tại')
            self.error.show()
        elif self.line_edit1.text() == '':
            self.error = error_form('Vui lòng nhập mã sản phẩm')
            self.error.show()
        elif self.line_edit2.text() == '':
            self.error = error_form('Vui lòng nhập tên sản phẩm')
            self.error.show()
        elif self.line_edit6.text() == '':
            if warehouse_count == 0:
                warehouse_db.insert(self.line_edit1.text(),0)
            self.desPath = 'C:/Users/NguyenDucHuy/Desktop/final/images/' +  self.line_edit4.text() 
            shutil.copyfile(self.imagePath,self.desPath)
            product_db.insert(self.line_edit1.text(),self.line_edit2.text(),self.line_edit3.text(),self.line_edit4.text(),self.line_edit5.text(),0,self.line_edit7.text())
            self.error = success_form()
            self.error.show()
            self.close()
        else: 
            if warehouse_count == 0:
                warehouse_db.insert(self.line_edit1.text(),0)
            self.desPath = 'C:/Users/NguyenDucHuy/Desktop/final/images/' +  self.line_edit4.text() 
            shutil.copyfile(self.imagePath,self.desPath)
            product_db.insert(self.line_edit1.text(),self.line_edit2.text(),self.line_edit3.text(),self.line_edit4.text(),self.line_edit5.text(),int(self.line_edit6.text()),self.line_edit7.text())
            self.error = success_form()
            self.error.show()
            self.close()

    def get_image(self):
        self.imagePath, _ = QFileDialog.getOpenFileName()
        self.line_edit4.setText(self.line_edit1.text() + '.jpg')

        
class error_form(QDialog):
    def __init__(self,text):
        super().__init__()
        self.text = text
        self.init_ui()

    def init_ui(self): 
        self.setWindowTitle('Lỗi')
        self.resize(200, 100)
        self.l1 = QtWidgets.QLabel(self)
        self.l1.move(50, 30)
        self.l1.setText(self.text)
        self.button = QtWidgets.QPushButton('Đóng',self)
        self.button.move(60, 60)
        self.button.clicked.connect(self.close)


class success_form(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self): 
        self.setWindowTitle('Thông báo')
        self.resize(250, 100)
        self.l1 = QtWidgets.QLabel(self)
        self.l1.move(40, 30)
        self.l1.setText('Đã thêm vào danh sách sản phẩm')
        self.button = QtWidgets.QPushButton('Đóng',self)
        self.button.move(60, 60)
        self.button.clicked.connect(self.close)