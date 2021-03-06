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
        self.setStyleSheet('background-color:#1effff')
        self.init_ui()
        
    def init_ui(self):       
        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText('Mã sản phẩm')
        self.l1.move(110, 110)
        self.l1.setStyleSheet('color:black;bold 12px;font :10.5pt Comic Sans MS')
        self.line_edit1 = QtWidgets.QLineEdit(self)
        self.line_edit1.setGeometry(210, 105, 200, 30)
        self.line_edit1.setStyleSheet('background-color:#f7f7f7; color:#8e8e8e;padding-top:0px;\
        font-size:10px;padding-left:10px;font: bold 12px')
        
        self.l2 = QtWidgets.QLabel(self)
        self.l2.setText('Tên sản phẩm')
        self.l2.move(110, 160)
        self.l2.setStyleSheet('color:black;bold 12px;font :10.5pt Comic Sans MS')
        self.line_edit2 = QtWidgets.QLineEdit(self)
        self.line_edit2.setGeometry(210, 155, 200, 30)
        self.line_edit2.setStyleSheet('background-color:#f7f7f7; color:#8e8e8e;padding-top:0px;\
        font-size:10px;padding-left:10px;font: bold 12px')
        
        self.l3 = QtWidgets.QLabel(self)
        self.l3.setText('Danh mục')
        self.l3.move(110, 210)
        self.l3.setStyleSheet('color:black;bold 12px;font :10.5pt Comic Sans MS')
        self.line_edit3 = QtWidgets.QLineEdit(self)
        self.line_edit3.setGeometry(210, 205, 200, 30)
        self.line_edit3.setStyleSheet('background-color:#f7f7f7; color:#8e8e8e;padding-top:0px;\
        font-size:10px;padding-left:10px;font: bold 12px')
        
        self.l4 = QtWidgets.QLabel(self)
        self.l4.setText('Hình ảnh')
        self.l4.move(110, 260)
        self.l4.setStyleSheet('color:black;bold 12px;font :10.5pt Comic Sans MS')
        self.line_edit4 = QtWidgets.QLineEdit(self)
        self.line_edit4.setGeometry(210, 255, 200, 30)
        self.line_edit4.setStyleSheet('background-color:#f7f7f7; color:#8e8e8e;padding-top:0px;\
        font-size:10px;padding-left:10px;font: bold 12px')

        self.button_1 = QtWidgets.QPushButton('Get',self)
        self.button_1.setGeometry(425, 255, 50, 30)
        self.button_1.setStyleSheet('color:#fafafa;font-size =15px;font: bold 14px;background-color:qlineargradient(spread:pad, x1:0.45,y1:0.3695,x2:0.426\
        ,y2:0,stop:0 rgba(255,170,0,228),stop:1 rgba(255,255,255,255));border-radius:10px;border:none')
        self.button_1.clicked.connect(self.get_image)
        
        self.l5 = QtWidgets.QLabel(self)
        self.l5.setText('Nhãn hiệu')
        self.l5.move(110, 310)
        self.l5.setStyleSheet('color:black;bold 12px;font :10.5pt Comic Sans MS')
        self.line_edit5 = QtWidgets.QLineEdit(self)
        self.line_edit5.setGeometry(210, 305, 200, 30)
        self.line_edit5.setStyleSheet('background-color:#f7f7f7; color:#8e8e8e;padding-top:0px;\
        font-size:10px;padding-left:10px;font: bold 12px')
        
        self.l6 = QtWidgets.QLabel(self)
        self.l6.setText('Giá')
        self.l6.move(110, 360)
        self.l6.setStyleSheet('color:black;bold 12px;font :10.5pt Comic Sans MS')
        self.line_edit6 = QtWidgets.QLineEdit(self)
        self.line_edit6.setGeometry(210, 355, 200, 30)
        self.line_edit6.setStyleSheet('background-color:#f7f7f7; color:#8e8e8e;padding-top:0px;\
        font-size:10px;padding-left:10px;font: bold 12px')

        self.l7 = QtWidgets.QLabel(self)
        self.l7.setText('Mô tả')
        self.l7.move(110, 410)
        self.l7.setStyleSheet('color:black;bold 12px;font :10.5pt Comic Sans MS')
        self.line_edit7 = QtWidgets.QLineEdit(self)
        self.line_edit7.setGeometry(210, 405, 200, 30)
        self.line_edit7.setStyleSheet('background-color:#f7f7f7; color:#8e8e8e;padding-top:0px;\
        font-size:10px;padding-left:10px;font: bold 12px')
        
        self.button = QtWidgets.QPushButton('Lưu',self)
        self.button.setGeometry(200, 455, 100, 30)
        self.button.resize(80,30)
        self.button.setStyleSheet('background-color:#4e4e4e; color:#fafafa ; font-size =15px;\
         border = 1px solid #4e4e4e;border-radius:10px;font: bold 14px')
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
            if self.line_edit4.text() != '':
                self.desPath = 'C:/Users/DELL/Documents/pycharm/final/images/' +  self.line_edit4.text()
                shutil.copyfile(self.imagePath,self.desPath)
            product_db.insert(self.line_edit1.text(),self.line_edit2.text(),self.line_edit3.text(),self.line_edit4.text(),self.line_edit5.text(),0,self.line_edit7.text())
            self.error = success_form()
            self.error.show()
            self.close()
        else:
            if warehouse_count == 0:
                warehouse_db.insert(self.line_edit1.text(),0)
            if self.line_edit4.text() != '':
                self.desPath = 'C:/Users/DELL/Documents/pycharm/final/images/' +  self.line_edit4.text()
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