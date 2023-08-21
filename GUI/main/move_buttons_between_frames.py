import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
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

class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.create_widget()
        self.setStyleSheet("""QFrame{
                                        border: 1px solid #aaa
                                        } """)

    def create_widget(self):
        self.left_frame = QFrame(self)
        self.left_frame.setGeometry(0, 0,300, 400)

        self.central_frame = QFrame(self)
        self.central_frame.setGeometry(400,0, 300, 400)

        self.right_frame = QFrame(self)
        self.right_frame.setGeometry(800,0, 300, 400)

      #

        self.top_label = QLabel("top_layout")
        self.content_label = QLabel("content_layout")
        self.top_widget_layout = QHBoxLayout()
        self.content_widget_layout = QVBoxLayout()

        self.main_widget_layout = QVBoxLayout(self.left_frame)


        self.description = QPushButton(f'Planet')
        self.description.setGeometry(0,15,150,25)
        self.description.setStyleSheet("QPushButton {border-style: solid; border-width: 2px; border-right-color: white; border-bottom-color: white;}")
        self.description.setMaximumHeight(25)
        self.description.pressed.connect(self.drug_event)

        self.button_pressed = 1
        self.button = QPushButton('')
        self.button.setGeometry(200,10,25,25)
        self.button.setFixedSize(25, 25)
        self.button.clicked.connect(self.handleButton)
        self.button.setIcon(QIcon(r'../../Images/arrow_down.png'))
        self.button.setIconSize(QSize(20, 20))
        self.button.setStyleSheet(
            "QPushButton {border-style: solid; border-width: 2px; border-left-color: white; border-top-color: white;}")
        self.texted = QTextEdit()

        self.top_widget_layout.addWidget(self.description)
        self.top_widget_layout.addWidget(self.button)
        self.content_widget_layout.addWidget(self.texted)

        self.main_widget_layout.addLayout(self.top_widget_layout)
        self.main_widget_layout.addLayout(self.content_widget_layout)


    def handleButton(self):

        if self.button_pressed == 0:
            self.button_pressed = 1
            self.button.setIcon(QIcon(r'../../Images/arrow_down.png'))
            self.button.setIconSize(QSize(20, 20))
            self.button.setGeometry(200, 10, 25, 25)
            self.button.setStyleSheet(
                "QPushButton {border-style: solid; border-width: 2px; border-left-color: white; border-top-color: white;}")
            self.texted.show()
            self.left_frame.resize(300, 400)


        elif self.button_pressed == 1:
            self.button_pressed = 0
            self.button.setIcon(QIcon(r'../../Images/arrow_up.png'))
            self.button.setStyleSheet(
                "QPushButton {border-style: solid; border-width: 2px; border-right-color: white; border-bottom-color: white;}")
            self.button.setIconSize(QSize(20, 20))
            self.button.setGeometry(200, 10, 25, 25)
            self.texted.hide()
            self.left_frame.resize(300, 50)
    def drug_event(self):
        print("Druged")
        drag = QDrag(self)

        # QMimeData контейнер для передачи данных
        mime = QMimeData()

        # Sets the data to be sent to the given MIME data. Ownership of the data is transferred to the QDrag object.
        # Устанавливает данные для отправки в заданные данные MIME. Право собственности на данные передается объекту QDrag.
        drag.setMimeData(mime)

        # Запускает процесс перемещения объекта  QDrag(self)
        drag.exec_(Qt.MoveAction)
    def dragEnterEvent(self, event):

        if event.mimeData().hasImage():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        print("hello")
        if not event.source().geometry().contains(event.pos()):
            source = self.get_index(event.pos())
            if source is None:
                return

            i, j = max(self.target, source), min(self.target, source)
            p1, p2 = self.gridLayout.getItemPosition(i), self.gridLayout.getItemPosition(j)

            self.gridLayout.addItem(self.gridLayout.takeAt(i), *p2)
            self.gridLayout.addItem(self.gridLayout.takeAt(j), *p1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())