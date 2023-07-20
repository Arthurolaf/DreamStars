import multiprocessing
from multiprocessing import Process
def testing():
    print("Объектов")
def square(n):
    print("Число квадратов в ",n**2)
def cube(n):
    print("Количество кубиков в ",n**3)
if __name__=="__main__":
    p1=Process(target=square,args=(7,))
    p2=Process(target=cube,args=(7,))
    p3=Process(target=testing)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print("Мы закончили")