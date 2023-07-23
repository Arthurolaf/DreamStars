
scene = QGraphicsScene()    
# def populate():
#     # Функция наплевала объектво размного размера на подобии звезд, возвращает как сцену
    

#     print('test2')
#     for i in range(90):
#         x = random.randint(40, 940)
#         y = random.randint(40, 940)
#         r = random.randint(2, 4)
#         rect = scene.addEllipse(x, y, r, r, QPen(QColor(255,128,0), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin), QBrush(QColor(255,128,20,128)))
#         rect.setFlag( QGraphicsItem.ItemIsSelectable )

#     return scene

# scene = populate()
scene.setSceneRect(0, 0, 1000, 1000)
scene.views

    
main_map = MyView(scene)
main_map.setStyleSheet("background:black;")

