import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Hidenbutton import changeVisibility
from map import main_map_scen
from widget_panel_part import Window
import random

class Main_Window(QWidget):
    def __init__(self, load_game=None):
        super(Main_Window, self).__init__()
        self.load_game = load_game
        self.initUI()
        

    def initUI(self):
        
        
        
        hbox = QHBoxLayout(self)

        # temporary placeholder
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        
        widget_pl_info = Window("planet_info")
        corgo_info = Window("corgo_info")
        # temporary placeholder
        layout = QVBoxLayout(self)
        layout.addWidget(corgo_info)
        layout.addWidget(widget_pl_info)
        self.control_panel = QWidget()
        self.control_panel.setLayout(layout)

        #bottom.setFrameShape(QFrame.StyledPanel)

        # This area should contain the "Objects control panel" and the Map. Lets add it. 
        
        splitter_ocp_nd_map = QSplitter(Qt.Horizontal) # The splitter moves along the horizontal (but the splitter itself is vertical)
        
        # Add Objects control panel (control_panel)
        splitter_ocp_nd_map.addWidget(self.control_panel)


        if self.load_game is not None:            
            map = main_map_scen(load_game=self.load_game)
        else:
            map = main_map_scen()


        splitter_ocp_nd_map.addWidget(map.model) # Place the map in the splitter area 
        
        splitter_ocp_nd_map.setSizes([100,200])


        # This area should contain event messages and additional object descriptions.
        splitter_msgs_nd_dscr = QSplitter(Qt.Horizontal)


        splitter_msgs_nd_dscr.addWidget(bottom)
        splitter_msgs_nd_dscr.addWidget(changeVisibility())

        splitter2 = QSplitter(Qt.Vertical) 
        splitter2.addWidget(splitter_ocp_nd_map)
        splitter2.addWidget(splitter_msgs_nd_dscr)

        hbox.addWidget(splitter2)

        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter demo')
        self.show()
		
# def main():
#    app = QApplication(sys.argv)
#    ex = Main_Window()
#    sys.exit(app.exec_())
	
# if __name__ == '__main__':
#    main()