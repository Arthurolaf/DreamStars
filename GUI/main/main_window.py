import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from Hidenbutton import changeVisibility
from map import main_map_scen,Cursor
from widget_panel_part import Mini_Widget
from control_panel import Top_left_window
import random



class Custom_Grid(QHBoxLayout):
    import pandas as pd

    # def __init__(self, name=None):
    #     self.wprsd = 0
    #     self.defoult_grid = self.df
    #     print(self.df)
    #
    #
    #     self.cp_colum_1 = QVBoxLayout()
    #     self.cp_colum_2 = QVBoxLayout()
    #     self.cp_colum_3 = QVBoxLayout()
    #     self.cp_colum_3.setAlignment(Qt.AlignTop)
    #
    #     self.cp_colum_1.addWidget(Mini_Widget("planet_info1"))
    #     self.cp_colum_2.addWidget(Mini_Widget("corgo_info1"))
    #     self.cp_colum_3.addWidget(Mini_Widget("other_info1"))
    #     self.cp_colum_1.addWidget(Mini_Widget("planet_info2"))
    #     self.cp_colum_2.addWidget(Mini_Widget("corgo_info2"))
    #     self.cp_colum_3.addWidget(Mini_Widget("other_info2"))
    #     self.tst_wgt = self.cp_colum_1.itemAt(0).widget()
    #
    #     print(self.tst_wgt.geometry())
    #     self.top_left_lt = QHBoxLayout()
    #     self.top_left_lt.addLayout(self.cp_colum_1)
    #     self.top_left_lt.addLayout(self.cp_colum_2)
    #     self.top_left_lt.addLayout(self.cp_colum_3)
    #     self.description = QPushButton(f'Newname')
    #     self.description.setStyleSheet("QPushButton {border-style: solid; border-width: 2px; border-left-color: white; border-top-color: white;}")
    #
    #     self.tst_wgt.layout_m.addWidget(self.description)
    #     self.tst_wgt.button.clicked.connect(self.tst_wgt.handleButton)

class Main_Window(QWidget):
    def __init__(self, load_game=None):
        super(Main_Window, self).__init__()
        self.load_game = load_game
        self.initUI()
        self.start_path = None
    #def keyPressEvent(self, event):
        #print('key: %s -' % event.key())
        #print('modifiers:', str(event.modifiers()))
    def initUI(self):

        main_layout_box = QHBoxLayout(self)
        #self.setLayout(main_layout_box)
        # temporary placeholder
        bottom_left = QFrame()
        bottom_left.setFrameShape(QFrame.StyledPanel)
        top_left = Top_left_window()
        top_left2 = QFrame()
        # Control_panel




        # This area should contain the "Objects control panel" and the Map. Lets add it. 
        
        splitter_ocp_nd_map = QSplitter(Qt.Horizontal) # The splitter moves along the horizontal (but the splitter itself is vertical)
        
        # Add Objects control panel (control_panel)
        splitter_ocp_nd_map.addWidget(top_left)


        if self.load_game is not None:            
            self.map = main_map_scen(load_game=self.load_game)
        else:
            self.map = main_map_scen()


        splitter_ocp_nd_map.addWidget(self.map.model) # Place the map in the splitter area
        
        splitter_ocp_nd_map.setSizes([100,200])


        # This area should contain event messages and additional object descriptions.
        splitter_msgs_nd_dscr = QSplitter(Qt.Horizontal)


        splitter_msgs_nd_dscr.addWidget(bottom_left)
        splitter_msgs_nd_dscr.addWidget(changeVisibility())

        splitter2 = QSplitter(Qt.Vertical) 
        splitter2.addWidget(splitter_ocp_nd_map)
        splitter2.addWidget(splitter_msgs_nd_dscr)

        main_layout_box.addWidget(splitter2)

        self.setLayout(main_layout_box)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        player = "artur"
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle(f'Dream Stars {player}')
        self.show()
        self.map.model.itemDoubleClicked.connect(self.handleItemDoubleClicked)
        self.map.model.itemSelect.connect(self.item_selected)
        self.map.model.itemAddWay.connect(self.drow_path)
        #self.map.model.itemDoubleClicked.connect(lambda item: self.printer(item))
    def handleItemDoubleClicked(self, item):
            print(round(item.boundingRect().x()))
            print(round(item.boundingRect().y()))
            print(type(item))

    def item_selected(self, item):
        self.start_path = item
        print(item)
        print(type(item))

    def drow_path(self, item):
        if self.start_path is not None:
            print(self.start_path)
            print(item)
            print(type(item))
            self.map.drow_path(self.start_path["x"],item["x"],self.start_path["y"],item["y"])



#            self.map.cursor = Cursor(x.data(0)[0],x.data(0)[1]+100)
def main():
   app = QApplication(sys.argv)
   ex = Main_Window()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()