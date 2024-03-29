from time import *
from random import *
from styles import * 
import os

def loading_bar(speed='FAST', length=100, color="terminal"):
    """
    Prints a loading bar 
    Args:
        - speed (int): (slow, normal, fast)
        - length (int): [1, 150]
        - color (str): ['purple', 'red', 'terminal'] 
    """
    if (speed.upper() not in['SLOW', 'NORMAL', 'FAST'] and length == 0):
        print("Invalid nyk!")
        return None
    else:
        def gen_(): yield from [iteration for iteration in range(length+1)]
        _ =text_color[color.upper()]+"█"
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
        print(text_color["TERMINAL"])
    print("\n")

def message(message="your message", type="BRACKET", color="TERMINAL"): 
    """
    Prints a message  
    Args:
        - message (str)
        - type (str): [BRACKET, THICK, THIN]
        - color (str): [PURPLE, RED, TERMINAL, GREEN] 
    """
    match type.upper():
        case "THIN":
            print(text_color[color.upper()]+f"{'-'*len(message)}\n{message}\n{'-'*len(message)}")
        case "THICK":
            print(text_color[color.upper()]+f"{'='*len(message)}\n{message}\n{'='*len(message)}") 
        case "BRACKET":
            print("{}[ {} ]".format(text_color[color.upper()], message)) 
        case _:
            print("Pick a Type zaab!")
    print(text_color["TERMINAL"])


def change_terminal_background(color="BLACK"):
    """
    Changes the terminal background color  
    Args:
        - color (str): [PURPLE, RED, TERMINAL, GREEN ...] 
    """
    os.system('color {}'.format(background_color[color.upper()]))




