from math import pi
from numpy import arctan2, sqrt
import argparse

# TODO: Accept List, Complex type as well!

def get_x_y():
    """ . """
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=float)
    parser.add_argument("y", type=float)    
    args = parser.parse_args()
    return args.x, args.y

def ret2pol(x, y):
    """ Converts rectangular coordinates to polar (in degrees). """
    modulo = sqrt(x**2 + y**2)
    theta = arctan2(y, x)
    theta = theta*(180/pi)
    print(f'Módulo: {modulo} \nÂngulo: {theta} graus.')

# Parsing the retrieved list
"""
for item in complex_list:
    re_part = item.real
    img_part = item.imag
    modulo, theta = ret2pol(re_part, img_part)
    print(f'Valor em retangular: {item}')
    print(f'Módulo: {modulo} \nÂngulo:(Graus) {theta}')
    print("\n")
"""

if __name__ == "__main__":
    x, y = get_x_y()
    ret2pol(x, y)