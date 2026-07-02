import numpy as np
import math as mt
import sympy as sp
from Foward_kinematic import *
from Inverse_kinematic import *
from database import *
import serial
import time


T0 = forward_kinematic(0,30,90,30,0)
print(T0)
Tf = forward_kinematic(90,30,90,30,0)
print(Tf)
R0 = np.array([[T0[0][0],T0[0][1],T0[0][2]],[T0[1][0],T0[1][1],T0[1][2]],[T0[2][0],T0[2][1],T0[2][2]]])
Rf = np.array([[Tf[0][0],Tf[0][1],Tf[0][2]],[Tf[1][0],Tf[1][1],Tf[1][2]],[Tf[2][0],Tf[2][1],Tf[2][2]]])

# print(Rf)

R0_transpose = np.transpose(R0)

# print(R0_transpose)

R = np.dot(R0_transpose,Rf)
# print(R)

#first order
step = 10
t=0
px = ((Tf[0][3]-T0[0][3])/step)*(t) + T0[0][3]
py = ((Tf[1][3]-T0[1][3])/step)*(t) + T0[1][3]
pz = ((Tf[2][3]-T0[2][3])/step)*(t) + T0[2][3]

# vx = ((Tf[0][3]-T0[0][3])/t) 
# tx = ((Tf[0][3]-T0[0][3])/vx) 
# vy = ((Tf[1][3]-T0[1][3])/t)
# ty = ((Tf[0][3]-T0[0][3])/vy) 
# vz = ((Tf[2][3]-T0[2][3])/t)
# tz = ((Tf[0][3]-T0[0][3])/vz) 
v_total=5

t_total = ((((Tf[0][3]-T0[0][3])**(2))+((Tf[1][3]-T0[1][3])**(2))+((Tf[2][3]-T0[2][3])**(2)))**(1/2))/(v_total**2)
vx = ((Tf[0][3]-T0[0][3])/t_total) 
vy = ((Tf[1][3]-T0[1][3])/t_total)
vz = ((Tf[2][3]-T0[2][3])/t_total)
print(t_total)
print(vx)
print(vy)
print(vz)

theta1_dot = 0
theta2_dot = 0
theta3_dot = 0
theta4_dot = 0
theta5_dot = 0

theta1 = (90*math.pi)/180
theta2 = (30*math.pi)/180
theta3 = (90*math.pi)/180
theta4 = (30*math.pi)/180
theta5 = (0*math.pi)/180

L1 = 65
L2 = 27
L3 = 105
L4 = 133
L5 = 182



velocity5 = [[vx],[vy],[vz]]
jaqobian0 = [[-L1],[],[]]
jaqobian5 =np.dot(jaqobian0 , Rf)
seta_dot = [[theta1_dot],[theta2_dot],[theta3_dot],[theta4_dot],[theta5_dot]]

jaqobian_inverse = np.linalg.inv(jaqobian5)

seta_dot = np.dot(velocity5,jaqobian_inverse)

print(seta_dot)
