import numpy as np
import math as mt
import sympy as sp
from database import *


# DH = 0     0    L1  theta1
#      90    0    0   theta2
#      0  L2   0   theta3
#      0     L3   0   theta4
#      -90    0    L4  theta5  

# L1 = 65
# L2 = 27
# L3 = 105
# L4 = 133
# L5 = 182

# theta_01 = 120
# theta_02 = 45
# theta_03 = 90
# theta_04 = 30
# theta_05 = 0

# def trans05 (th1, th2, th3, th4, th5) :
#     t01 = np.array([[mt.cos(mt.radians(th1)), (-1)* mt.sin(mt.radians(th1)),0,0], 
#                     [mt.sin(mt.radians(th1)),mt.cos(mt.radians(th1)),0,0],
#                     [0, 0, 1, L1],
#                     [0, 0, 0, 1]])
#     t12 = np.array([[mt.cos(mt.radians(th2)), (-1)* mt.sin(mt.radians(th2)),0,L2], 
#                     [0, 0, -1, 0],
#                     [mt.sin(mt.radians(th2)), mt.cos(mt.radians(th2)),0,0],
#                     [0, 0, 0, 1]])
#     t23 = np.array([[mt.cos(mt.radians(th3)),  (-1)*mt.sin(mt.radians(th3)),0,L3], 
#                     [(1)* mt.sin(mt.radians(th3)),(1)* mt.cos(mt.radians(th3)),0,0],
#                     [0, 0, 1, 0],
#                     [0, 0, 0, 1]])
#     t34 = np.array([[mt.cos(mt.radians(th4)), (-1)* mt.sin(mt.radians(th4)),0,L4], 
#                     [(-1)*mt.sin(mt.radians(th4)), (-1)*mt.cos(mt.radians(th4)),0,0],
#                     [0, 0, -1, 0],
#                     [0, 0, 0, 1]])
#     t45 = np.array([[mt.cos(mt.radians(th5)), (-1)*mt.sin(mt.radians(th5)),0,0], 
#                     [0, 0, -1, -L5],
#                     [ mt.sin(mt.radians(th5)), mt.cos(mt.radians(th5)),0,0],
#                     [0, 0, 0, 1]])

#     t02 = np.dot(t01,t12)
#     t03 = np.dot(t02,t23)
#     t04 = np.dot(t03,t34)
#     t05 = np.dot(t04,t45)
#     return t05



# t_05 =  trans05(theta_01,theta_02,theta_03,theta_04,theta_05)
# print (t_05)


def forward_kinematic(a,b,c,d,e):
    L1 = 65
    L2 = 27
    L3 = 105
    L4 = 133
    L5 = 182

    theta_01 = a
    theta_02 = b
    theta_03 = c
    theta_04 = d
    theta_05 = e

    def trans05 (th1, th2, th3, th4, th5) :
        t01 = np.array([[mt.cos(mt.radians(th1)), (-1)* mt.sin(mt.radians(th1)),0,0], 
                        [mt.sin(mt.radians(th1)),mt.cos(mt.radians(th1)),0,0],
                        [0, 0, 1, L1],
                        [0, 0, 0, 1]])
        t12 = np.array([[mt.cos(mt.radians(th2)), (-1)* mt.sin(mt.radians(th2)),0,L2], 
                        [0, 0, -1, 0],
                        [mt.sin(mt.radians(th2)), mt.cos(mt.radians(th2)),0,0],
                        [0, 0, 0, 1]])
        t23 = np.array([[mt.cos(mt.radians(th3)),  (-1)*mt.sin(mt.radians(th3)),0,L3], 
                        [(1)* mt.sin(mt.radians(th3)),(1)* mt.cos(mt.radians(th3)),0,0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])
        t34 = np.array([[mt.cos(mt.radians(th4)), (-1)* mt.sin(mt.radians(th4)),0,L4], 
                        [(-1)*mt.sin(mt.radians(th4)), (-1)*mt.cos(mt.radians(th4)),0,0],
                        [0, 0, -1, 0],
                        [0, 0, 0, 1]])
        t45 = np.array([[mt.cos(mt.radians(th5)), (-1)*mt.sin(mt.radians(th5)),0,0], 
                        [0, 0, -1, -L5],
                        [ mt.sin(mt.radians(th5)), mt.cos(mt.radians(th5)),0,0],
                        [0, 0, 0, 1]])

        t02 = np.dot(t01,t12)
        t03 = np.dot(t02,t23)
        t04 = np.dot(t03,t34)
        t05 = np.dot(t04,t45)
        return t05



    t_05 =  trans05(theta_01,theta_02,theta_03,theta_04,theta_05)
    
    return t_05 


import sympy as sp

def forward_kinematic_position():
    # Define symbolic variables for joint angles and link lengths
    theta_1, theta_2, theta_3, theta_4, theta_5 = sp.symbols('theta_1 theta_2 theta_3 theta_4 theta_5')
    L1, L2, L3, L4, L5 = sp.symbols('L1 L2 L3 L4 L5')
    
    # Define transformation matrices symbolically
    t01 = sp.Matrix([[sp.cos(sp.rad(theta_1)), -sp.sin(sp.rad(theta_1)), 0, 0],
                     [sp.sin(sp.rad(theta_1)), sp.cos(sp.rad(theta_1)), 0, 0],
                     [0, 0, 1, L1],
                     [0, 0, 0, 1]])

    t12 = sp.Matrix([[sp.cos(sp.rad(theta_2)), -sp.sin(sp.rad(theta_2)), 0, L2],
                     [0, 0, -1, 0],
                     [sp.sin(sp.rad(theta_2)), sp.cos(sp.rad(theta_2)), 0, 0],
                     [0, 0, 0, 1]])

    t23 = sp.Matrix([[sp.cos(sp.rad(theta_3)), -sp.sin(sp.rad(theta_3)), 0, L3],
                     [sp.sin(sp.rad(theta_3)), sp.cos(sp.rad(theta_3)), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

    t34 = sp.Matrix([[sp.cos(sp.rad(theta_4)), -sp.sin(sp.rad(theta_4)), 0, L4],
                     [-sp.sin(sp.rad(theta_4)), -sp.cos(sp.rad(theta_4)), 0, 0],
                     [0, 0, -1, 0],
                     [0, 0, 0, 1]])

    t45 = sp.Matrix([[sp.cos(sp.rad(theta_5)), -sp.sin(sp.rad(theta_5)), 0, 0],
                     [0, 0, -1, -L5],
                     [sp.sin(sp.rad(theta_5)), sp.cos(sp.rad(theta_5)), 0, 0],
                     [0, 0, 0, 1]])

    # Compute the final transformation matrix
    t05 = t01 * t12 * t23 * t34 * t45
    
    # Extract end-effector position from the last column of the matrix
    px, py, pz = t05[0, 3], t05[1, 3], t05[2, 3]
    
    return sp.simplify(px), sp.simplify(py), sp.simplify(pz)

# Get the symbolic end-effector position
px, py, pz = forward_kinematic_position()
print(px)
print(py)
print(pz)
