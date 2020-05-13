# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:06:22 2020

@author: S11De
"""

import sys  #нужен для передачи argv в QApplication
#from PyQt5 import QtCore, QtGui, QtWidgets #нужно для работы с формой
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QMessageBox)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import formBase #это наша форма
import locale #для конверта флоатов
import webbrowser #для перехода на форум

ActiveLan = 'ru'
RUSSIAN = ['Поиск корня','Поле для ввода', 'Поле для ответа', 'Нажать, чтоб посчитать корни', 'Округление', 'Язык', 'Русский', 'Английский', 'Немецкий', 'Помощь', 'Форум', 'Информация', 'тут текст для информации']
ENGLISH = ['Root searching']
DEUTCH = ['Wurzelsuche']

URL = 'https://github.com/MnT-for-collective-development/SqrtPythonProject' #ссылка на форум поддержки

class ExampleApp(QtWidgets.QMainWindow, formBase.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам и т.д. в файле формы
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.answerButton.clicked.connect(self.SqrtOp) #обрабатываем расчет корня
        self.actionHelp.triggered.connect(self.OpenURL) #обрабатываем кнопку помощи
        self.actionEnglish.triggered.connect(self.ChangeLangEn)
        self.actionRussian.triggered.connect(self.ChangeLangRu)
        self.actionDeutch.triggered.connect(self.ChangeLangDe) #привязываем кнопки к переводу
        self.actionInfo.triggered.connect(self.showdialog) #привязываем кнопки к информации и помощи
        
    def OpenURL(self):
        webbrowser.open_new(URL)
        
    def SqrtOp(self):
        temp = self.askTextBrowser.toPlainText() #забираем строку из первого текстБокса
        self.answerTextBrowser.setText(SqrtWrk(isMatch(temp), int(self.roundSpinBox_2.cleanText()))) #отправляем во второй текстовый обработанную строку 
                                            #из формы тащится значение спинбокса с кол-вом знаков после точки
    def ChangeLangEn(self):
        ActiveLan = 'en'
        ChangeLang(self)
        
    def ChangeLangRu(self):
        ChangeLang(self, 'ru')
        
    def ChangeLangDe(self):
        ChangeLang(self, 'de')

    def showdialog(self):
        msg = QMessageBox()
        
        msg.setText(RUSSIAN[12])
        msg.setWindowTitle(' ')
        retval = msg.exec_()

def ChangeLang(self, language):
    self.setWindowTitle('12112')

def isMatch(string): #тут надо проверять соответствие и возвращать какие-то индексы
    pointer = 0
    string = string.replace(" ","") #удаляем пробелы, мешающие работе
    string = string.replace('i', 'j') #приводим к перевариваемому питоном виду, если есть комплексная часть
    try: #пришел int, длинный int, ноль
        if (string.find('-') != -1 and  string.find('j') == -1):
            string += '0j'
        string = int(string)
        pointer = 1
    except (ValueError, TypeError):
        
        try: #пришел float в виде (1.2; 1.2E+11), длинный float, float-ноль
            string = locale.atof(string)
            pointer = 2
        except (ValueError, TypeError):
            
            try: #пришло комплексное число в виде 45+3i или 45+3j
                string = complex(string)
                pointer = 3
            except (ValueError, TypeError):
                string = 'неверный ввод'
    return [pointer, string]

def SqrtWrk(number, rounder): #тут работаем с самим корнем
    temp = '±' #корни симметричны #надо ли выводить при нуле?
    
    #арифметические +
    #из нуля +
    #комплексные
    #длинные числа +
    #заданная точность +
    #аналитические ???????????
    
    if (number[0] == 1 or number[0] == 2): 
        #пришел int, длинный int, ноль или float в виде (1.2; 1.2E+11), длинный float, float-ноль
        temp += str(round(pow(number[1], 0.5), rounder)) #возводим в степень 0.5, округляем до указанного числа после точки
        #также работает и с длинной арифметикой
        
    elif (number[0] == 3):
        #пришло комплексное число в виде 45+3i или 45+3j
        compTemp = pow(number[1], 0.5) #находим корень
        temp += str(round(compTemp.real, rounder) + round(compTemp.imag, rounder)*1j)
        
    else: #тут можно сделать еще кондишены на ошибки, но оно никому не надо
        temp = number[1]
    
    return temp

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()