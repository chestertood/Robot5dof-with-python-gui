import numpy as np
import math as mt
import sympy as sp
from Foward_kinematic import *
from Inverse_kinematic import *
from database import *
import serial
import time

def MOVEL(theta1,theta2,theta3,theta4,theta5,step):

    T0 = forward_kinematic(0,69,42,159,0)
    print(T0)
    Tf = forward_kinematic(theta1,theta2,theta3,theta4,theta5)
    print(Tf)
    R0 = np.array([[T0[0][0],T0[0][1],T0[0][2]],[T0[1][0],T0[1][1],T0[1][2]],[T0[2][0],T0[2][1],T0[2][2]]])
    Rf = np.array([[Tf[0][0],Tf[0][1],Tf[0][2]],[Tf[1][0],Tf[1][1],Tf[1][2]],[Tf[2][0],Tf[2][1],Tf[2][2]]])

    # print(Rf)

    R0_transpose = np.transpose(R0)

    # print(R0_transpose)

    R = np.dot(R0_transpose,Rf)
    # print(R)

    #first order
    step = step
    t=0
    px = ((Tf[0][3]-T0[0][3])/step)*(t) + T0[0][3]
    py = ((Tf[1][3]-T0[1][3])/step)*(t) + T0[1][3]
    pz = ((Tf[2][3]-T0[2][3])/step)*(t) + T0[2][3]

    theta_new_axis = np.arccos((R[0][0]+R[1][1]+R[2][2]-1)/2)
    print(theta_new_axis)

    theta_new_axis_per_step = theta_new_axis/step

    K_axis = np.dot(1/(2*(np.sin(theta_new_axis))),[[R[2][1]-R[1][2]],[R[0][2]-R[2][0]],[R[1][0]-R[0][1]]] )
    kx = K_axis[0][0]
    ky = K_axis[1][0]
    kz = K_axis[2][0]
    cos = np.cos(theta_new_axis_per_step)
    sin = np.sin(theta_new_axis_per_step)



    V_theta_new_axis_per_step = 1 - np.cos(theta_new_axis_per_step)
    delta_R = np.array([[(kx*kx*V_theta_new_axis_per_step+cos),(kx*ky*V_theta_new_axis_per_step-kz*sin),(kz*kx*V_theta_new_axis_per_step+ky*sin)]
            ,[(kx*ky*V_theta_new_axis_per_step+kz*sin),(ky*ky*V_theta_new_axis_per_step+cos),(ky*kz*V_theta_new_axis_per_step-kx*sin)]
            ,[(kx*kz*V_theta_new_axis_per_step-ky*sin),(ky*kz*V_theta_new_axis_per_step+kx*sin),(kx*kx*V_theta_new_axis_per_step+cos)]])




    R_tranject = np.dot(R0,delta_R)

    #print(R_tranject)

    tranformation10 = []
    for i in range(1,step+1):
        tranformation = np.array([[],[],[],[]])
        theta = theta_new_axis_per_step*i
        cos = np.cos(theta)
        sin = np.sin(theta)
        px = ((Tf[0][3]-T0[0][3])/step)*(i) + T0[0][3]
        py = ((Tf[1][3]-T0[1][3])/step)*(i) + T0[1][3]
        pz = ((Tf[2][3]-T0[2][3])/step)*(i) + T0[2][3]
        V_theta = 1 - np.cos(theta)
        delta_R = np.array([[(kx*kx*V_theta+cos),(kx*ky*V_theta-kz*sin),(kz*kx*V_theta+ky*sin)]
                ,[(kx*ky*V_theta+kz*sin),(ky*ky*V_theta+cos),(ky*kz*V_theta-kx*sin)]
                ,[(kx*kz*V_theta-ky*sin),(ky*kz*V_theta+kx*sin),(kz*kz*V_theta+cos)]])

        R_tranject = np.dot(R0,delta_R)
        R11 = R_tranject[0][0] 
        R12 = R_tranject[0][1] 
        R13 = R_tranject[0][2] 
        R21 = R_tranject[1][0] 
        R22 = R_tranject[1][1] 
        R23 = R_tranject[1][2] 
        R31 = R_tranject[2][0] 
        R32 = R_tranject[2][1] 
        R33 = R_tranject[2][2]  

        tranformation = np.array([[R11,R12,R13,px],[R21,R22,R23,py],[R31,R32,R33,pz],[0,0,0,1]])


        tranformation10.append(tranformation)
        print(f"step = {i}  : " +str(tranformation))

    tranformation10  = np.array(tranformation10)


    print(tranformation10[1][0])

    theta1 = []
    theta2 = []
    theta3 = []
    theta4 = []
    theta5 = []
    for i in range (step):
        inverse_kinematic_non_sql_metix(tranformation10[i])
        theta1_degree,theta2_degree,theta3_degree,theta4_degree,theta5_degree = inverse_kinematic_non_sql_metix(tranformation10[i])
        theta1.append(theta1_degree)
        theta2.append(theta2_degree)
        theta3.append(theta3_degree)
        theta4.append(theta4_degree)
        theta5.append(theta5_degree)
    print(theta1)
    print(theta2)
    print(theta3)
    print(theta4)
    print(theta5)
    
    # 
    # for i in range(step):
    #     data = f"{theta1[i]},{theta2[i]},{theta3[i]},{theta4[i]},{theta5[i]}\n"
    #     arduino.write(data.encode())  # Send data as bytes
    #     print(f"Sent to Arduino: {data.strip()}")
    #     time.sleep(0.1)  # Add a slight delay for Arduino to process the data

    # return theta1 , theta2 , theta3 , theta4 , theta5 


K_axis = MOVEL(30,45,70,30,0,100)
print(K_axis)
