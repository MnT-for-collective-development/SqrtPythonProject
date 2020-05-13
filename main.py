# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:06:22 2020

@author: S11De
"""

import sys  #нужен для передачи argv в QApplication
#from PyQt5 import QtCore, QtGui, QtWidgets #нужно для работы с формой
#from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QMessageBox)
#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import formBase #это наша форма
import locale #для конверта флоатов
import webbrowser #для перехода на форум


LANGUAGE = [1,
           ['Поиск корня','Поле для ввода', 'Поле для ответа', 'Нажать, чтоб посчитать корни', 'Округление', 'Язык', 'Помощь', 'Русский', 'Английский', 'Немецкий', 'Форум', 'Информация', "Программа для вычисления корня числа<br><br>Авторы:<br>Ушаков А.С<br>Кириллов Я.А.<br>Петров П.П.<br><p align='center'>г.Пермь, ПГНИУ, 2020</p>", 'Неверный ввод'],
           ['Root searching','Input field', 'Output field', 'Push to take roots', 'Round', 'Language', 'Help', 'Russian', 'English', 'Deutch', 'Forum', 'Information', "A program for calculating the root of a number<br><br>Authors:<br>Ushakov A.S.<br>Kirillov Y.A.<br>Petrov P.P.<br><p align='center'>Perm, PSU, 2020</p>", 'Invalid input'], 
           ['Wurzelsuche', 'Eingabefeld', 'Antwortfeld', 'Klicken Sie, um die Wurzeln zu zählen', 'Rundung', 'Zunge', 'Hilfe', 'Russisch', 'Englisch', 'Deutsche', 'Forum', 'Information', "Programm zur Berechnung der Wurzel einer Zahl<br><br>Autoren:<br>Ushakov A.S.<br>Kirillov Y.A.<br>Petrov P.P.<br><p align='center'>Perm, PSU, 2020</p>", 'Ungültige Eingabe']]

URL = 'https://github.com/MnT-for-collective-development/SqrtPythonProject/issues' #ссылка на форум поддержки

class ExampleApp(QtWidgets.QMainWindow, formBase.Ui_MainWindow):
    
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам и т.д. в файле формы
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        ChangeLang(self) #начальное задание языка

        self.answerButton.clicked.connect(self.SqrtOp) #обрабатываем расчет корня
        self.actionHelp.triggered.connect(self.OpenURL) #обрабатываем кнопку помощи
        self.actionEnglish.triggered.connect(self.ChangeLangEn)
        self.actionRussian.triggered.connect(self.ChangeLangRu)
        self.actionDeutch.triggered.connect(self.ChangeLangDe) #привязываем кнопки к переводу
        self.actionInfo.triggered.connect(self.showdialog) #привязываем кнопки к информации и помощи
        
    def OpenURL(self): 
        webbrowser.open_new(URL) #открываем заданную ссылку (тут - мейн репозитория гитхаб)
        
    def SqrtOp(self):
        temp = self.askTextBrowser.toPlainText() #забираем строку из первого текстБокса
        self.answerTextBrowser.setText(SqrtWrk(isMatch(temp), int(self.roundSpinBox_2.cleanText()))) #отправляем во второй текстовый обработанную строку 
                                            #из формы тащится значение спинбокса с кол-вом знаков после точки
    def ChangeLangRu(self):
        LANGUAGE[0] = 1 #меняем нынешний язык на русский
        ChangeLang(self) #применяем изменения
        
    def ChangeLangEn(self):
        LANGUAGE[0] = 2 #меняем нынешний язык на английский
        ChangeLang(self) #применяем изменения
        
    def ChangeLangDe(self):
        LANGUAGE[0] = 3 #меняем нынешний язык на немецкий
        ChangeLang(self) #применяем изменения

    def showdialog(self):
        msg = QMessageBox()
        msg.setText(LANGUAGE[LANGUAGE[0]][12])
        msg.setWindowTitle(LANGUAGE[LANGUAGE[0]][11])
        retval = msg.exec_()

def ChangeLang(self):
    self.setWindowTitle(LANGUAGE[LANGUAGE[0]][0]) #заголовок окна
    self.askTextLabel.setText(LANGUAGE[LANGUAGE[0]][1]) #поле ввода
    self.answerTextLabel.setText(LANGUAGE[LANGUAGE[0]][2]) #поле вывода
    self.answerButton.setText(LANGUAGE[LANGUAGE[0]][3]) #кнопка решения
    self.roundLabel.setText(LANGUAGE[LANGUAGE[0]][4]) #кол-во точек после запятой
    self.menuLanguage.setTitle(LANGUAGE[LANGUAGE[0]][5]) #меню языков
    self.menuHelp.setTitle(LANGUAGE[LANGUAGE[0]][6]) #меню помощи
    self.actionRussian.setText(LANGUAGE[LANGUAGE[0]][7]) #русский
    self.actionEnglish.setText(LANGUAGE[LANGUAGE[0]][8]) #английский
    self.actionDeutch.setText(LANGUAGE[LANGUAGE[0]][9]) #немецкий
    self.actionHelp.setText(LANGUAGE[LANGUAGE[0]][10]) #помощь
    self.actionInfo.setText(LANGUAGE[LANGUAGE[0]][11]) #информация
    self.answerTextBrowser.setText('')

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
                string = LANGUAGE[LANGUAGE[0]][13]
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