# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:06:22 2020

@author: S11De
"""

import sys  #нужен для передачи argv в QApplication
from PyQt5 import QtWidgets #нужно для работы с формой
import formBaseUi #это наша форма
import locale #для конверта флоатов

class ExampleApp(QtWidgets.QMainWindow, formBaseUi.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам и т.д. в файле формы
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        
        self.answerButton.clicked.connect(self.SqrtOp) #обрабатываем клик кнопки
        
    def SqrtOp(self):
        temp = self.askTextBrowser.toPlainText() #забираем строку из первого текстБокса
        self.answerTextBrowser.setText(SqrtWrk(isMatch(temp), int(self.rounderSpinBox.cleanText()))) #отправляем во второй текстовый обработанную строку 
                                            #из формы тащится значение спинбокса с кол-вом знаков после точки

def isMatch(string): #тут надо проверять соответствие и возвращать какие-то индексы
    pointer = 0
    try: #пришел int, длинный int, ноль
        string = int(string)
        pointer = 1
    except ValueError:
        
        try: #пришел float в виде (1.2; 1.2E+11), длинный float, float-ноль
            string = locale.atof(string)
            pointer = 2
        except ValueError:
            
            try: #пришло комплексное число в виде 45+3i или 45+3j
                string = string.replace('i', 'j') #приводим к перевариваемому питоном виду
                string = complex(string)
                pointer = 3
            except ValueError:
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
    
    if (number[0] == 1): 
        #пришел int, длинный int, ноль
        temp += str(round(pow(number[1], 0.5), rounder)) #возводим в степень 0.5, округляем до указанного числа после точки
        #также работает и с длинной арифметикой
        
    elif (number[0] == 2): 
        #пришел float в виде (1.2; 1.2E+11), длинный float, float-ноль
        temp += str(round(pow(number[1], 0.5), rounder))
        
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