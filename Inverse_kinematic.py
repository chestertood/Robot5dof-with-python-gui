import math as mt
from Foward_kinematic import *
import numpy as np
import math
from database import *
import tkinter
from tkinter import *
from PIL import Image, ImageTk

# print(Fwd.t_05[0][0])

# theta_01 = 120
# theta_02 = 30
# theta_03 = 80
# theta_04 = 10
# theta_05 = 0

# T_home =[[0 , 0 , 1 , 201.5],
# [0 , 1 , 0 , 0],
# [-1 , 0 , 0 , 287.5],
# [0 , 0 , 0 , 1]]

# Px = Fwd.t_05[0][3] #กำหนด position matrix 0-6
# Py = Fwd.t_05[1][3]
# Pz = Fwd.t_05[2][3]

# r11 = Fwd.t_05[0][0] #กำหนด rotation matrix 0-6
# r12 = Fwd.t_05[0][1]
# r13 = Fwd.t_05[0][2]
# r21 = Fwd.t_05[1][0]
# r22 = Fwd.t_05[1][1]
# r23 = Fwd.t_05[1][2]
# r31 = Fwd.t_05[2][0]
# r32 = Fwd.t_05[2][1]
# r33 = Fwd.t_05[2][2]

# L1 = 65
# L2 = 27   
# L3 = 105
# L4 = 133
# L5 = 182




# wx = Fwd.t_05[0][3] - (Fwd.t_05[0][2] * Fwd.L5) 
# wy = Fwd.t_05[1][3] - (Fwd.t_05[1][2] * Fwd.L5)
# wz =  Fwd.t_05[2][3] - (Fwd.t_05[2][2] * Fwd.L5) 

# wx_home = Px - (r13 * L5) 
# wy_home = Py - (r23 * L5)
# wz_home =  Pz - (r33 * L5) 

# print(wx)
# print(wy)
# print(wz)

# if wy >=0 and wx >= 0 :
#     theta1 = (mt.atan2(wy,wx))
#     theta1_degree = round((theta1* 180)/mt.pi)
#     theta1_radian = (theta1_degree* mt.pi)/180
  

# elif (wy < 0 and wx > 0)  :
#     theta1 = (mt.atan2(-wy,wx))
#     theta1_degree = round((theta1* 180)/mt.pi)
#     theta1_degree = 180 - theta1_degree 
#     theta1_radian = (theta1_degree* mt.pi)/180


# elif (wy > 0 and wx < 0 ) :
#     theta1 = (mt.atan2(wy,-wx))
#     theta1_degree = 180-round((theta1* 180)/mt.pi)
#     theta1_radian = (theta1_degree* mt.pi)/180 

# elif wy < 0 and wx < 0 :
#     theta1 = (mt.atan2(wy,wx))
#     theta1_degree = round((theta1* 180)/mt.pi) + 180
#     theta1_radian = (theta1_degree* mt.pi)/180 

# elif round(wy/wx) == 0 :
#     theta1 = (mt.atan2(wy,wx))
#     theta1_degree = round((theta1* 180)/mt.pi)  - 180
#     theta1_radian = (theta1_degree* mt.pi)/180 





# Vector = math.sqrt((wx)**2 + (wy)**2)

# if wx <= 0 and wy <= 0 : #เช็คว่า Vector ควรติด - หรือ +
#     Vector = -Vector
# elif theta1_radian > math.pi/2 and wx >= 0:
#     Vector = -Vector

# R = Vector - L2  #กำหนด R, S สำหรับคำนวณ theta 2, 3
# S = wz - L1

# print(Pz)
# print(S)
# theta3 = 0
# theta3_degree = 0
# if (Pz >= 0 ) :
#     c3 = ((((R**2)+(S**2)-((L3)**2)-((L4)**2))/(2*L3*L4 )))
#     # (wx_home)**2) + ((wy_home)**2) -(2*R*(Fwd.L2)) +((Fwd.L2)**2))+(S**2)
#     theta3 = mt.acos(c3)
#     theta3_degree = round((theta3* 180)/mt.pi)



#     phi =mt.atan2(R,S)
#     beta = mt.atan2(Fwd.L4 * mt.sin(theta3), Fwd.L3 + (Fwd.L4 * mt.cos(theta3))) 

#     theta2 = 1.5708 -  (phi + beta )
#     theta2_degree = round((theta2* 180)/mt.pi)
#     if theta2_degree < 0 :
#         theta2_degree = 360 + round((theta2* 180)/mt.pi) #Gu mua 

# elif Pz<0:
#     print("หุ่นติดจมดินไอ้ควาย")







# R13 = Fwd.t_05[0][2]
# R23 = Fwd.t_05[1][2]
# R33 =Fwd.t_05[2][2]
# theta4 = 0
# if theta2_degree+theta3_degree <= 90:
#     theta4 = mt.acos((-mt.cos(theta1_radian)*mt.sin(theta2+theta3)*R13) -(mt.sin(theta1_radian)*mt.sin(theta2+theta3)*R23) + (mt.cos(theta2+theta3)*R33))
#     theta4_degree = round((theta4* 180)/mt.pi)
    

# else:
#     theta4 = mt.acos((-mt.cos(theta1_radian)*mt.sin(theta2+theta3)*R13) -(mt.sin(theta1_radian)*mt.sin(theta2+theta3)*R23) + (mt.cos(theta2+theta3)*R33))
#     theta4_degree = round((theta4* 180)/mt.pi)
    


# R11 = Fwd.t_05[0][0]
# R21 = Fwd.t_05[1][0]  
# R12 = Fwd.t_05[0][1] 
# R22 =Fwd.t_05[1][1]

# if theta1_degree <= 90 :
#     theta5 = mt.acos(((-1)*mt.sin(theta1_radian)*R12)+ (mt.cos(theta1_radian)*R22)) 
#     theta5_degree = round((theta5* 180)/mt.pi)
# elif theta1_degree > 90 :
#     theta5 = mt.acos(((-1)*mt.sin(theta1_radian)*R12) + (mt.cos(theta1_radian)*R22)) 
#     theta5_degree = round((theta5* 180)/mt.pi)



# print("Theta1 = "+str((theta1_degree)))
# print("Theta2 = "+str((theta2_degree)))
# print("Theta3 = "+str((theta3_degree)))
# print("Theta4 = "+str((theta4_degree)))
# print("Theta5 = "+str((theta5_degree)))

@connect_sql
def inverse_kinematic(cursor, root):       
    sql_getdata = "SELECT * FROM tranformation_metrix"
    cursor.execute(sql_getdata)
    data = cursor.fetchall()

    last_row_value = data[-1]
    Px, Py, Pz = last_row_value[10], last_row_value[11], last_row_value[12]
    r11, r12, r13 = last_row_value[1], last_row_value[2], last_row_value[3]
    r21, r22, r23 = last_row_value[4], last_row_value[5], last_row_value[6]
    r31, r32, r33 = last_row_value[7], last_row_value[8], last_row_value[9]
    theta1_degree,theta2_degree,theta3_degree,theta4_degree,theta5_degree = last_row_value[13], last_row_value[14], last_row_value[15],last_row_value[16], last_row_value[17]


    
    
    update_label(root, "t1", f"{theta1_degree}", x=(590 + 50), y=700)
    update_label(root, "t2", f"{theta2_degree}", x=(650 + 50), y=700)
    update_label(root, "t3", f"{theta3_degree}", x=(710 + 50), y=700)
    update_label(root, "t4", f"{theta4_degree}", x=(770 + 50), y=700)
    update_label(root, "t5", f"{theta5_degree}", x=(830 + 50), y=700)
  






def inverse_kinematic_non_sql(r11_value_sql,r12_value_sql,r13_value_sql,r21_value_sql,r22_value_sql,r23_value_sql,r31_value_sql,r32_value_sql,r33_value_sql,px_value_sql,py_value_sql,pz_value_sql):   
    last_row_value = [r11_value_sql,r12_value_sql,r13_value_sql,r21_value_sql,r22_value_sql,r23_value_sql,r31_value_sql,r32_value_sql,r33_value_sql,px_value_sql,py_value_sql,pz_value_sql]
   
    Px, Py, Pz = last_row_value[9], last_row_value[10], last_row_value[11]
    r11, r12, r13 = last_row_value[0], last_row_value[1], last_row_value[2]
    r21, r22, r23 = last_row_value[3], last_row_value[4], last_row_value[5]
    r31, r32, r33 = last_row_value[6], last_row_value[7], last_row_value[8]

    # Constants for link lengths
    L1, L2, L3, L4, L5 = 65, 27, 105, 133, 182

    # Calculate wrist position
    wx = Px - (r13 * L5) 
    wy = Py - (r23 * L5)
    wz = Pz - (r33 * L5) 

    # Determine theta1 based on wx, wy
    theta1_degree, theta1_radian = calculate_theta1(wx, wy)

    # Calculate vector and R, S for theta 2 and 3
    Vector = math.sqrt((wx)**2 + (wy)**2)
    Vector = adjust_vector_sign(Vector, wx, wy, theta1_radian)
    R, S = Vector - L2, wz - L1

    # Calculate theta2 and theta3
    theta2_degree, theta3_degree = calculate_theta2_theta3(Pz, R, S, L3, L4)

    # Calculate theta4
    theta4_degree = calculate_theta4(theta1_radian, theta2_degree, theta3_degree, r13, r23, r33)

    # Calculate theta5
    theta5_degree = calculate_theta5(theta1_degree, theta1_radian, r12, r22)

    print(f"Theta1 = {theta1_degree}")
    print(f"Theta2 = {theta2_degree}")
    print(f"Theta3 = {theta3_degree}")
    print(f"Theta4 = {theta4_degree}")
    print(f"Theta5 = {theta5_degree}")
    return theta1_degree,theta2_degree,theta3_degree,theta4_degree,theta5_degree


def calculate_theta1(wx, wy):
    if wy >= 0 and wx >= 0 :
        theta1 = mt.atan2(wy, wx)
    elif wy < 0 and wx > 0:
        theta1 = mt.atan2(-wy, wx)
        theta1 = math.pi-theta1
    elif wy > 0 and wx < 0:
        theta1 = mt.atan2(wy, -wx)
        theta1 = math.pi - theta1
    elif wy < 0 and wx < 0:
        theta1 = mt.atan2(wy, wx) + math.pi 
    else:
        theta1 = -mt.atan2(wy, wx)  # Assign a default value when wx and wy are both 0.
    
   

    theta1_degree = round(math.degrees(theta1))
    theta1_radian = math.radians(theta1_degree)
    return theta1_degree, theta1_radian

def adjust_vector_sign(Vector, wx, wy, theta1_radian):
    if wx <= 0 and wy <= 0:
        return -Vector
    elif theta1_radian > math.pi / 2 and wx >= 0:
        return -Vector
    return Vector

def calculate_theta2_theta3(Pz, R, S, L3, L4):
    if Pz >= 0:
        c3 = ((R**2 + S**2 - L3**2 - L4**2) / (2 * L3 * L4))
        theta3 = math.acos(c3)
        theta3_degree = round(math.degrees(theta3))
        
        phi = math.atan2(R, S)
        beta = math.atan2(L4 * math.sin(theta3), L3 + L4 * math.cos(theta3))
        theta2 = math.pi / 2 - (phi + beta)
        theta2_degree = round(math.degrees(theta2))

        # if theta2_degree < 0:
        #     theta2_degree += 360
        return theta2_degree, theta3_degree
    else:
        print("The robot arm is underground.")
        return None, None

def calculate_theta4(theta1_radian, theta2_degree, theta3_degree, r13, r23, r33):
    theta2_radian = math.radians(theta2_degree)
    theta3_radian = math.radians(theta3_degree)
    cos_theta4 = (-math.cos(theta1_radian) * math.sin(theta2_radian + theta3_radian) * r13 -
                  math.sin(theta1_radian) * math.sin(theta2_radian + theta3_radian) * r23 +
                  math.cos(theta2_radian + theta3_radian) * r33)
    theta4 = math.acos(cos_theta4)
    return round(math.degrees(theta4))

def calculate_theta5(theta1_degree, theta1_radian, r12, r22):
    cos_theta5 = -math.sin(theta1_radian) * r12 + math.cos(theta1_radian) * r22
    # Clamp cos_theta5 to the range [-1, 1] to avoid math domain errors
    cos_theta5 = max(-1, min(1, cos_theta5))
    theta5 = math.acos(cos_theta5)
    return round(math.degrees(theta5))

def update_label(root, name, text, x, y):
    # Check if label exists and update if necessary
    existing_label = root.nametowidget(name) if name in root.children else None
    if existing_label:
        existing_label.config(text=text)
    else:
        new_label = Label(root, text=text, font=('calibre', 10, 'normal'), name=name)
        new_label.place(x=x, y=y)


def inverse_kinematic_non_sql_metix(metrix):   
    
    r11_value_sql,r12_value_sql,r13_value_sql,r21_value_sql,r22_value_sql,r23_value_sql,r31_value_sql,r32_value_sql,r33_value_sql,px_value_sql,py_value_sql,pz_value_sql = metrix[0][0],metrix[0][1],metrix[0][2],metrix[1][0],metrix[1][1],metrix[1][2],metrix[2][0],metrix[2][1],metrix[2][2],metrix[0][3],metrix[1][3],metrix[2][3]

    last_row_value = [r11_value_sql,r12_value_sql,r13_value_sql,r21_value_sql,r22_value_sql,r23_value_sql,r31_value_sql,r32_value_sql,r33_value_sql,px_value_sql,py_value_sql,pz_value_sql]
   
    Px, Py, Pz = last_row_value[9], last_row_value[10], last_row_value[11]
    r11, r12, r13 = last_row_value[0], last_row_value[1], last_row_value[2]
    r21, r22, r23 = last_row_value[3], last_row_value[4], last_row_value[5]
    r31, r32, r33 = last_row_value[6], last_row_value[7], last_row_value[8]

    # Constants for link lengths
    L1, L2, L3, L4, L5 = 65, 27, 105, 133, 182

    # Calculate wrist position
    wx = Px - (r13 * L5) 
    wy = Py - (r23 * L5)
    wz = Pz - (r33 * L5) 

    # Determine theta1 based on wx, wy
    theta1_degree, theta1_radian = calculate_theta1(wx, wy)

    # Calculate vector and R, S for theta 2 and 3
    Vector = math.sqrt((wx)**2 + (wy)**2)
    Vector = adjust_vector_sign(Vector, wx, wy, theta1_radian)
    R, S = Vector - L2, wz - L1

    # Calculate theta2 and theta3
    theta2_degree, theta3_degree = calculate_theta2_theta3(Pz, R, S, L3, L4)

    # Calculate theta4
    theta4_degree = calculate_theta4(theta1_radian, theta2_degree, theta3_degree, r13, r23, r33)

    # Calculate theta5
    theta5_degree = calculate_theta5(theta1_degree, theta1_radian, r12, r22)


    return theta1_degree,theta2_degree,theta3_degree,theta4_degree,theta5_degree


t_05 = forward_kinematic(10,30,90,30,0)

print(t_05)

inverse = inverse_kinematic_non_sql_metix(t_05)

print(inverse)