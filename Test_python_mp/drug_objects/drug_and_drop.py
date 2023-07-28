from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

"""
Постараюсь описать что тут просиходит своими словами.
"""


class DragButton(QPushButton):

    def mouseMoveEvent(self, e):
        """ 
        При нажатии левой клавиши мыши используется QDrug класс который применим на сам объект в нашем случае на DragButton который является измененным QPushButton

        """
        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)

            # QMimeData контейнер для передачи данных 
            mime = QMimeData()

            # Sets the data to be sent to the given MIME data. Ownership of the data is transferred to the QDrag object.
            # Устанавливает данные для отправки в заданные данные MIME. Право собственности на данные передается объекту QDrag.
            drag.setMimeData(mime)

            # Запускает процесс перемещения объекта  QDrag(self)
            drag.exec_(Qt.MoveAction)


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

        self.blayout = QHBoxLayout()
        for l in ['A', 'B', 'C', 'D']:
            btn = DragButton(l)
            self.blayout.addWidget(btn)

        self.setLayout(self.blayout)

    def dragEnterEvent(self, e):
        """
        Есть встроена фунция dragEnterEvent мы ссылаемся на нее же и передаем e как event == accept() 
        тем самым разрещая widget-у  перемещаться
        """
        e.accept()

    def dropEvent(self, e):
        pos = e.pos()
        widget = e.source()

        for n in range(self.blayout.count()):
            # Get the widget at each index in turn.
            w = self.blayout.itemAt(n).widget()
            if pos.y() < w.y() + w.size().width() // 2:
                # We didn't drag past this widget.
                # insert to the left of it.
                self.blayout.insertWidget(n-1, widget)
                break

        e.accept()


app = QApplication([])
w = Window()
w.show()

app.exec_()