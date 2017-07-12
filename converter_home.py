import sys

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QDoubleSpinBox, QPushButton, QVBoxLayout
 

#QDoubleSpinBox
#QLable - текст
#QApplication - приложение
#два поля - исходная валюта и исходная
#потом можно его научить работать в обратную сторону + кнопка очистить
#проверить есл ив каждом из полей 0 конвертировать нельзя. как и если в обоих есть. блокируем кнопку
#если в обном из полей 0, то запускаем конвертацию оттуда, откуда не 0
#конвертация по нажатию enter?
#конвертация на лету?

class Course(QObject):
    def get(self):
        return 30.0
    
    
class CurrencyConverter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initUi()
        self._initLayouts()
        self._initSignals()

    def _initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self) #исходная. label похож на кнопку, сначала то, что отражено, потом родитель
        self.resultLabel = QLabel('Сумма в долларах', self)

        self.srcAmount = QDoubleSpinBox(self) #этому виджету можем передать только родителя. по умолчанию максимальное число для ввода 99
        self.srcAmount.setMaximum(999999999)

        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)

        self.convertBtn = QPushButton('Перевести', self)
        
        self.clearBtn = QPushButton('Очистить', self)#описываем нов кнопку

        self.updateConvertBtnStatus()#блокируем кнопку при запуске, потому что значения в нуле

    def _initLayouts(self):
        w = QWidget(self)#промежуточный виджет. мейн же менять нельзя. к нему и применим слой
        self.mainLayout = QVBoxLayout(w) #применяем в конструкторе слой к виджету
        self.mainLayout.addWidget(self.srcLabel) #добавляем в сой все виджеты
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)

        self.mainLayout.addWidget(self.clearBtn)#визуализируем нов кнопку

        self.setCentralWidget(w) #добавляем промежуточный виджет как центральный

    def _initSignals(self):
        self.convertBtn.clicked.connect(self.onClick)
        self.srcAmount.valueChanged.connect(self.updateConvertBtnStatus)#смотрим что поменялось значение в поле ввода
        self.resultAmount.valueChanged.connect(self.updateConvertBtnStatus)

        '''
        #мгновенная конвертация, тогда кнопка не нужна
        
        self.srcAmount.valueChanged.connect(self.realTime)
        self.resultAmount.valueChanged.connect(self.realTime)
        '''

        self.clearBtn.clicked.connect(self.onClickClear)#сигнал на нов кнопку
        
    def onClick(self):
        value = self.srcAmount.value #получаем то что лежит в ячейке методом value
        value2 = self.resultAmount.value

        if value: #проверили, что не 0
            self.resultAmount.setValue(value / Course().get())

        if value2: #проверили, что не 0
            self.resultAmount.setValue(value * Course().get())
            

    def onClickClear(self):
        value = self.srcAmount.value
        value2 = self.resultAmount.value
        if value:
            self.srcAmount.setValue(0.0)
        if value2:
            self.resultAmount.setValue(0.0)
        

    def updateConvertBtnStatus(self):
        value = self.srcAmount.value()
        value2 = self.resultAmount.value()
        x = bool(value) ^ bool(value2)
        self.convertBtn.setEnabled(bool(x))

    """
    #мгновенная конвертация
    def realTime(self):
        self.onClick()
    """

    def keyPressEvent(self, qKeyEvent):
        print('enter нажали')
        value = self.srcAmount.value()
        value2 = self.resultAmount.value()
        x = bool(value) ^ bool(value2)
        if x and qKeyEvent.key() == QtCore.Qt.Key_Return: 
            self.onClick()
        else:
            super().keyPressEvent(qKeyEvent)
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    converter = CurrencyConverter()
    converter.show()

    sys.exit(app.exec_())

