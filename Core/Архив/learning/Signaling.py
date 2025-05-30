import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import QObject, Signal, Slot


class Communicate(QObject):
    # create two new signals on the fly: one will handle
    # int type, the other will handle strings
    speak = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        #self.speak[int].connect(self.say_something)
        self.speak[str].connect(self.say_something)

    # define a new slot that receives a C 'int' or a 'str'
    # and has 'say_something' as its name
    #@Slot(int)
    @Slot(str)
    def say_something(self, arg):
            _return_ =  "This is a string:" + arg
            print(type(_return_))
            return _return_

if __name__ == "__main__":
    app = QApplication(sys.argv)
    someone = Communicate()

    # emit 'speak' signal with different arguments.
    # we have to specify the str as int is the default
    #someone.speak.emit(10)
    print(someone.speak.emit("Hello everybody!"))