import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


def class_name(o):
    return o.metaObject().className()

def init_widget(w, name):
    """Init a widget for the gallery, give it a tooltip showing the
       class name"""
    w.setObjectName(name)
    w.setToolTip(class_name(w))
class Top_left_window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.main_widget()
        self.setStyleSheet("""QFrame{
                                        border: 1px solid #aaa
                                        } """)



    def main_widget(self):
        self.main_widget_layout = QVBoxLayout()
        self.setLayout(self.main_widget_layout)

        self.top_widget_layout = QHBoxLayout()
        self.mid_widget_layout = QHBoxLayout()

        self.tool_tst = self.create_text_toolbox()
        self.tool_tst2 = self.create_text_toolbox()
        self.mid_area = self.create_tabwidget()

        self.top_widget_layout.addWidget(self.tool_tst)
        self.top_widget_layout.addWidget(self.tool_tst2)

        self.mid_widget_layout.addWidget(self.mid_area)



        self.main_widget_layout.addLayout(self.top_widget_layout)
        self.main_widget_layout.addLayout(self.mid_widget_layout)
    def create_tabwidget(self):
        class Color(QWidget):

            def __init__(self, color):
                super(Color, self).__init__()
                self.setAutoFillBackground(True)

                palette = self.palette()
                palette.setColor(QPalette.Window, QColor(color))
                self.setPalette(palette)

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)
        init_widget(tabs, "mid_area")
        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)
        return tabs
    def create_text_toolbox(self):
        result = QToolBox()
        init_widget(result, "toolBox")

        # Create centered/italic HTML rich text
        rich_text = "<html><head/><body><i>"

        rich_text += "</i></body></html>"

        text_edit = QTextEdit(rich_text)
        init_widget(text_edit, "textEdit")
        init_widget(text_edit, "plainTextEdit")

        self._systeminfo_textbrowser = QTextBrowser()
        init_widget(self._systeminfo_textbrowser, "systemInfoTextBrowser")
        #button_pressed = 1
        button = QPushButton('test')
        result.addItem((text_edit), "Text Edit")
        #result.addItem((text_edit),"Plain Text Edit")
        #result.addItem((self._systeminfo_textbrowser),"Text Browser")
        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Top_left_window()
    w.show()
    sys.exit(app.exec_())