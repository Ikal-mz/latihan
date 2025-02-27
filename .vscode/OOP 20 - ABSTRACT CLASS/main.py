# membuat class abstract

# abc = abstract base class
from abc import ABC,abstractclassmethod

class Button(ABC):
    
    @abstractclassmethod
    def click(self):
        pass

class PushButton(Button):
    
    def click(self):
        print('push button click')

class RadioButton(Button):

    def click(self):
        print('radio button class')

tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()