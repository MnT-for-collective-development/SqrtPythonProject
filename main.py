# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:06:22 2020

@author: S11De
"""

import sys  #нужен для передачи argv в QApplication
from PyQt5 import QtWidgets #нужно для работы с формой
import formBaseUi #это наша форма

class ExampleApp(QtWidgets.QMainWindow, formBaseUi.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам и т.д. в файле формы
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        
        self.answerButton.clicked.connect(self.SqrtOp) #обрабатываем клик кнопки
        
    def SqrtOp(self):
        temp = self.askTextBrowser.toPlainText() #забираем строку из первого текстБокса
        self.answerTextBrowser.setText(SqrtWrk(temp, isMatch(temp))) #отправляем во второй текстовый обработанную строку 
        
def isMatch(string):
    #тут надо проверять соответствие и возвращать какие-то индексы
    

def SqrtWrk(number): #тут работаем с самим корнем
    tfdNum.setText("±"+
			engine.eval("pow("+input+",0.5)").toString());
            else
                tfdNum.setText("±" + engine.eval("round(" + input + 
		"**0.5," + spnAccuracy.getValue() + ")").toString());


    return number 

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()