import numpy as np
#import math
def vector_long(x,y,x1,y1):
    import math
    """
    Calculates the length of a vector and returns a value 
    """
    # print(x,y,x1,y1)

    return math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

def warp_long(x1:float,y1:float,tx1:float,ty1:float,speed=0.,debug=False):
    """
    def warp_long(x1: float,
              y1: float,
              tx1: float,
              ty1: float,
              speed: int = 0,
              debug: bool = False) -> list[int]

    Creates a vector of given length (speed) from another vector and returns the coordinates as a list.

    The function takes the coordinates of the ship x1,x2(float),
    and target coordinates tx1,tx2(float), as well the speed of movement speed(int):

    The purpose of the function is to create the coordinates of the new Warp vector based on the speed

    return list(x1,y1,x2,y2)

    debug: False by default
    print debug info if set True
    """



    if debug is True:
        print(" =b-------- def warp_long debug --------=")
        print("args:",x1,y1,tx1,ty1,speed)
    if x1 == tx1:
        lvec = abs(ty1 - y1)
    elif y1 == tx1:
        lvec = abs(tx1 - x1)
    else:
        lvec = vector_long(x1,y1,tx1,ty1)
    if debug is True:
        print(f"way long:{lvec}, warp_speed {speed}")
    if speed != 0:
        accurate = lvec/speed
        if 1 < accurate  < 1:
            accurate = 1
        if debug is True:
            print(f"accurate: {accurate}")
    elif speed == 0:
        accurate = 1


    # Laying out the vector on the axis
    vector_x = tx1-x1
    vector_y = ty1-y1

    # Computing new coordinates
    if vector_y == 0 and vector_x < 0:
        if debug is True:
            print("vector_x = 0")
            print(speed)
        x2,y2 = x1-speed,y1
    elif vector_x == 0 and vector_y < 0:
        if debug is True:
            print("vector_y = 0")
        x2,y2 = x1,y1-speed
    elif vector_x == 0 and vector_x == 0:
        x2, y2 = x1, y1
    else:

        x2,y2 = round((vector_x / accurate)+x1,5),round((vector_y/accurate)+y1,5)
        if debug is True:
            print(vector_x,vector_y)
            print(f"New end point x2,y2:{x2,y2}")

    # Returning new coordinates
    coordinates = [x1, y1, x2, y2]
    # Print Check if debug
    if debug is True:
        check = round(vector_long(x1,x2,y1,y2))
        if check <= speed:
                print(f"Long Warp correct: {check}, coordinates {coordinates}")

        else:
                print(f"Incorrect long Warp: {check-speed}, coordinates {coordinates}")
        print(" =e-------- def warp_long debug --------=\n")
    return coordinates


def pursuit(px1:float, py1:float, s1:int, tx1:float,ty1:float, tx2:float, ty2:float, s2:int, debug=False):
    """
    Calculates new Warp coordinate in case of target tracking return new pursuer Warp coordinates

    pursuer current point (px1,py1)
    target current warp (tx1,ty1,tx2,ty2)
    pursuer warp speed (s1)
    target warp speed (s2)

    """

    #find out distance between tartget and pursuer in moment
    distance = vector_long(px1,py1,tx1,ty1)

    #find out number of turns Necessary to overtake the target
    max_rounds = round(distance/s1)
    max_turns = distance/s1


    # Point where Target will be after max_rounds ended
    max_long_target_way = max_rounds * s2
    # print(max_rounds, "r", max_turns)
    # print(s2)
    correct_long = max_long_target_way/3*2

    # Route Correction Point

    correction_line = warp_long(tx1,ty1,tx2,ty2,correct_long,debug)
    correction_point = correction_line[2:]
    if debug is not False:
        correction_check = round(
            abs(vector_long(correction_line[0], correction_line[1], correction_line[2], correction_line[3])
                - correct_long ))
        print(f"correction_data:  check:{correction_check},vector:{correction_line},point:{correction_point}")

    # New warp for pursuer

    corrected_pursuer_warp = warp_long(px1,py1,correction_point[0],correction_point[1],s1,debug)

    if distance <= abs(vector_long(corrected_pursuer_warp[0],corrected_pursuer_warp[1],corrected_pursuer_warp[2],corrected_pursuer_warp[3])):
        return [px1, py1,tx2, ty2]

    if debug is not False:
        print(" =b-------- def pursuit debug --------=")
        print(f"pursuer/target  distance {distance}")
        print(f"max_long_target_way  {max_long_target_way}")
        print(f"Approximate round need {max_rounds}")
        print(f"New pursuer warp  {corrected_pursuer_warp}")
        print(" =e-------- def pursuit debug --------=\n")

    return (corrected_pursuer_warp)



