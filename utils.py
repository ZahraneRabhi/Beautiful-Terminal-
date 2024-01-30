from time import *
from random import *
from styles import * 

def loading_bar(speed='FAST', length=100, color="terminal"):
    """
    Prints a loading bar 
    Args:
        - speed (int): (slow, normal, fast)
        - length (int): [1, 150]
        - color (str): ['purple', 'red', 'terminal'] 
    """
    if (speed.upper() not in['SLOW', 'NORMAL', 'FAST']):
        print("You should pick a speed zaab!")
        return None
    else:
        def gen_(): yield from [iteration for iteration in range(length)]
        _ =style[color.upper()]+"█"
        place_holder = "".join(["-" for _ in gen_()])+"|"
        pourcentage = "0%"
        for i in gen_():
            print("\r Progress: {} {}".format(place_holder, pourcentage), end = '')
            place_holder = place_holder.replace("-", _, 1)
            pourcentage = str(i) + "%"
            speed_rate = uniform(
                                speed_dic[speed][0],
                                speed_dic[speed][1])
            sleep(speed_rate)

