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
        self.answerTextBrowser.setText(SqrtWrk(temp, isMatch(temp), 5)) #отправляем во второй текстовый обработанную строку 
                                            #добавить в форму поле с кол-вом знаков для округления и тащить сюда вместо 5
def isMatch(string):
    return 1
    #тут надо проверять соответствие и возвращать какие-то индексы
    

def SqrtWrk(number, condition, rounder): #тут работаем с самим корнем
    temp = '±' #корни симметричны #надо ли выводить при нуле?
    
    #арифметические +
    #из нуля +, в двух форматах
    #комплексные
    #длинные числа +, в двух форматах
    #заданная точность +, но дописать интерфейс
    #аналитические
    
    if (condition == 2): 
        #пришел int, длинный int, ноль
        temp += str(round(pow(int(number), 0.5), rounder)) #возводим в степень 0.5, округляем до указанного числа после точки
        #также работает и с длинной арифметикой
        
    elif (condition == 3): 
        #пришел float в виде (1.2; 1.2E+11), длинный float, float-ноль
        temp += str(round(pow(locale.atof(number), 0.5), rounder))
        
    elif (condition == 1):
        #пришло комплексное число в виде 45+3i или 45+3j
        number = number.replace('i', 'j') #приводим к перевариваемому питоном виду
        compTemp = pow(complex(number), 0.5) #находим корень
        temp += str(round(compTemp.real, rounder) + round(compTemp.imag, rounder)*1j)
        
    # if (condition == 3):
        
    # else:
    #     temp += str(eval('round(number**0.5,5)')) #5 - точность, надо пофиксить
    return temp
#     tfdNum.setText("±"+
# 			engine.eval("pow("+input+",0.5)").toString());
#             else
#                 tfdNum.setText("±" + engine.eval("round(" + input + 
# 		"**0.5," + spnAccuracy.getValue() + ")").toString()); #кусок обращения к питон-машине у Зимы

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()