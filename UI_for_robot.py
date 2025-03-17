import tkinter
from tkinter import *
from PIL import Image, ImageTk
from database import *
from Inverse_kinematic import *
from Foward_kinematic import *
import time

import serial


root = Tk()
root.title("robot_movement_paddle กลุ่มสุดหล่อพร้อมลุย")
root.geometry("1920x1080")


head1 = Label(root, fg="white", bg="#bf2a5e" ,width="300", height="3" , text="Prod by chestertood" )  
head1.pack()
head2 = Label(root, fg="black", bg="pink" ,width="230", height="4", text="CONTROLLER OF ROBOT 5DOF",font=("Arial", 15, "bold") )  
head2.pack()


moveL = Frame(root,  bg="yellow", width="500", height="700",  )
moveL.pack(side="left", padx=10,pady=10 )  # Place head3 on the left

# # Second label (center)
moveJ = Frame(root,  bg="green", width="500", height="700", )
moveJ.pack(side="left", padx=10 ,pady=10)  # Expand head4 to take available space in the middle

# # Third label (right)
conflig = Frame(root,  bg="blue", width="500", height="700", )
conflig.pack(side="left", padx=10,pady=10 )  # Place head5 on the right


text1 = Label(text="MOVE_L",  )  # Set the background color to match the frame
text1.place(x=1280,y=500) # Use fill and expand

text2 = Label(text="MOVE_J",  )  # Set the background color to match the frame
text2.place(x=1280,y=200) # Use fill and expand

text3 = Label(text="INVERSE_TRANFORMATION",  )  # Set the background color to match the frame
text3.place(x=700,y=200) # Use fill and expand

r11 = Label(text="R11",  ) 
r11.place(x=610,y=260) 

r12 = Label(text="R12",  ) 
r12.place(x=710,y=260) 

r13 = Label(text="R13",  ) 
r13.place(x=810,y=260) 

r21 = Label(text="R21",  ) 
r21.place(x=610,y=360) 

r22 = Label(text="R22",  ) 
r22.place(x=710,y=360) 

r23 = Label(text="R23",  ) 
r23.place(x=810,y=360) 

r31 = Label(text="R31",  ) 
r31.place(x=610,y=460) 

r32 = Label(text="R32",  ) 
r32.place(x=710,y=460) 

r33 = Label(text="R33",  ) 
r33.place(x=810,y=460) 

px = Label(text="px",  ) 
px.place(x=910,y=260) 

py = Label(text="py",  ) 
py.place(x=910,y=360) 

pz = Label(text="pz",  ) 
pz.place(x=910,y=460) 

def update_label(root, name, text, x, y):
    # Check if label exists and update if necessary
    existing_label = root.nametowidget(name) if name in root.children else None
    if existing_label:
        existing_label.config(text=text)
    else:
        new_label = Label(root, text=text, font=('calibre', 10, 'normal'), name=name)
        new_label.place(x=x, y=y)

@connect_sql
def get_float_value_theta(cursor,a,b,c,d,e):
    try:
        THETA1_value_sql=float(a.get())
        THETA2_value_sql=float(b.get())
        THETA3_value_sql=float(c.get())
        THETA4_value_sql=float(d.get())
        THETA5_value_sql=float(e.get())

        t_05 = forward_kinematic(THETA1_value_sql,THETA2_value_sql,THETA3_value_sql,THETA4_value_sql,THETA5_value_sql)
        r11_value_fowardknm =t_05[0][0]
        r12_value_fowardknm =t_05[0][1]
        r13_value_fowardknm =t_05[0][2]
        r21_value_fowardknm =t_05[1][0]
        r22_value_fowardknm =t_05[1][1]
        r23_value_fowardknm =t_05[1][2]
        r31_value_fowardknm =t_05[2][0]
        r32_value_fowardknm =t_05[2][1]
        r33_value_fowardknm =t_05[2][2]
        px_value_fowardknm =t_05[0][3]
        py_value_fowardknm =t_05[1][3]
        pz_value_fowardknm =t_05[2][3]
        
        # sql_delete = "DELETE FROM tranformation_metrix"
        sql = f"INSERT INTO tranformation_metrix (r11,r12,r13,r21,r22,r23,r31,r32,r33,px,py,pz,THETA1,THETA2,THETA3,THETA4,THETA5) VALUES ({r11_value_fowardknm},{r12_value_fowardknm},{r13_value_fowardknm},{r21_value_fowardknm},{r22_value_fowardknm},{r23_value_fowardknm},{r31_value_fowardknm},{r32_value_fowardknm},{r33_value_fowardknm},{px_value_fowardknm},{py_value_fowardknm},{pz_value_fowardknm},{THETA1_value_sql},{THETA2_value_sql},{THETA3_value_sql},{THETA4_value_sql},{THETA5_value_sql})"
        # cursor.execute(sql_delete)
        cursor.execute(sql)

        update_label(root, "r11", f"{r11_value_fowardknm:.4f}", x=(610-510), y=260+200)
        update_label(root, "r12", f"{r12_value_fowardknm:.4f}", x=(710-510), y=260+200)
        update_label(root, "r13", f"{r13_value_fowardknm:.4f}", x=(810-510), y=260+200)
        update_label(root, "px", f"{px_value_fowardknm:.4f}", x=(910-510), y=260+200)
        update_label(root, "r21", f"{r21_value_fowardknm:.4f}", x=(610-510), y=360+200)
        update_label(root, "r22", f"{r22_value_fowardknm:.4f}", x=(710-510), y=360+200)
        update_label(root, "r23", f"{r23_value_fowardknm:.4f}", x=(810-510), y=360+200)
        update_label(root, "py", f"{py_value_fowardknm:.4f}", x=(910-510), y=360+200)
        update_label(root, "r31", f"{r31_value_fowardknm:.4f}", x=(610-510), y=460+200)
        update_label(root, "r32", f"{r32_value_fowardknm:.4f}", x=(710-510), y=460+200)
        update_label(root, "r33", f"{r33_value_fowardknm:.4f}", x=(810-510), y=460+200)
        update_label(root, "pz", f"{pz_value_fowardknm:.4f}", x=(910-510), y=460+200)
      
        
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid float.")
    


text4 = Label(text="FORWARD_TRANFORMATION",  )  # Set the background color to match the frame
text4.place(x=180,y=200)

THETA1_value,THETA2_value,THETA3_value,THETA4_value,THETA5_value = StringVar(),StringVar(),StringVar(),StringVar(),StringVar()

THETA1 = Label(text="THETA1",  ) 
THETA1.place(x=100-60,y=260) 

box_THETA1 = Entry(root,textvariable = THETA1_value, font=('calibre',10,'normal'),width=6)
box_THETA1.place(x=100-60,y=290)

THETA2 = Label(text="THETA2",  ) 
THETA2.place(x=200-60,y=260)

box_THETA2 = Entry(root,textvariable = THETA2_value, font=('calibre',10,'normal'),width=6)
box_THETA2.place(x=200-60,y=290)

THETA3 = Label(text="THETA3",  ) 
THETA3.place(x=300-60,y=260)

box_THETA3 = Entry(root,textvariable = THETA3_value, font=('calibre',10,'normal'),width=6)
box_THETA3.place(x=300-60,y=290)

THETA4 = Label(text="THETA4",  ) 
THETA4.place(x=400-60,y=260)

box_THETA4 = Entry(root,textvariable = THETA4_value, font=('calibre',10,'normal'),width=6)
box_THETA4.place(x=400-60,y=290)

THETA5 = Label(text="THETA5",  ) 
THETA5.place(x=500-60,y=260)

box_THETA5 = Entry(root,textvariable = THETA5_value, font=('calibre',10,'normal'),width=6)
box_THETA5.place(x=500-60,y=290)

button_theta = Button(root, text="SUBMIT",command=lambda:get_float_value_theta(THETA1_value,THETA2_value,THETA3_value,THETA4_value,THETA5_value))
button_theta.place(x=300-60,y=340)

r11_Tranfromarea = Label(text="R11",  ) 
r11_Tranfromarea.place(x=610-500,y=260+150) 

r12_Tranfromarea = Label(text="R12",  ) 
r12_Tranfromarea.place(x=710-500,y=260+150) 

r13_Tranfromarea = Label(text="R13",  ) 
r13_Tranfromarea.place(x=810-500,y=260+150) 

r21_Tranfromarea = Label(text="R21",  ) 
r21_Tranfromarea.place(x=610-500,y=360+150) 

r22_Tranfromarea = Label(text="R22",  ) 
r22_Tranfromarea.place(x=710-500,y=360+150) 

r23_Tranfromarea = Label(text="R23",  ) 
r23_Tranfromarea.place(x=810-500,y=360+150) 

r31_Tranfromarea = Label(text="R31",  ) 
r31_Tranfromarea.place(x=610-500,y=460+150) 

r32_Tranfromarea = Label(text="R32",  ) 
r32_Tranfromarea.place(x=710-500,y=460+150) 

r33_Tranfromarea = Label(text="R33",  ) 
r33_Tranfromarea.place(x=810-500,y=460+150) 

px_Tranfromarea = Label(text="px",  ) 
px_Tranfromarea.place(x=910-500,y=260+150) 

py_Tranfromarea = Label(text="py",  ) 
py_Tranfromarea.place(x=910-500,y=360+150) 

pz_Tranfromarea = Label(text="pz",  ) 
pz_Tranfromarea.place(x=910-500,y=460+150) 








image = Image.open("moveJ_picture.png")
resize_image = image.resize((150, 150))
img = ImageTk.PhotoImage(resize_image)
image_label = Label(image=img)
image_label.place(x=1230,y=250)

image1 = Image.open("moveL_picture.png")
resize_image1 = image1.resize((150, 150))
img1 = ImageTk.PhotoImage(resize_image1)
image_label1 = Label(image=img1)
image_label1.place(x=1230,y=550)



r11_value=StringVar()
r12_value=StringVar()
r13_value=StringVar()
r21_value=StringVar()
r22_value=StringVar()
r23_value=StringVar()
r31_value=StringVar()
r32_value=StringVar()
r33_value=StringVar()
px_value=StringVar()
py_value=StringVar()
pz_value=StringVar()

from tkinter import messagebox

@connect_sql
def get_float_value(cursor,a,b,c,d,e,f,g,h,i,j,k,l):
    try:
        r11_value_sql=float(a.get())
        r12_value_sql=float(b.get())
        r13_value_sql=float(c.get())
        r21_value_sql=float(d.get())
        r22_value_sql=float(e.get())
        r23_value_sql=float(f.get())
        r31_value_sql=float(g.get())
        r32_value_sql=float(h.get())
        r33_value_sql=float(i.get())
        px_value_sql=float(j.get())
        py_value_sql=float(k.get())
        pz_value_sql=float(l.get()) 

        theta1_degree,theta2_degree,theta3_degree,theta4_degree,theta5_degree = inverse_kinematic_non_sql(r11_value_sql,r12_value_sql,r13_value_sql,r21_value_sql,r22_value_sql,r23_value_sql,r31_value_sql,r32_value_sql,r33_value_sql,px_value_sql,py_value_sql,pz_value_sql)
        # sql_delete = "DELETE FROM tranformation_metrix"
        sql = f"INSERT INTO tranformation_metrix (r11,r12,r13,r21,r22,r23,r31,r32,r33,px,py,pz,THETA1,THETA2,THETA3,THETA4,THETA5) VALUES ({r11_value_sql},{r12_value_sql},{r13_value_sql},{r21_value_sql},{r22_value_sql},{r23_value_sql},{r31_value_sql},{r32_value_sql},{r33_value_sql},{px_value_sql},{py_value_sql},{pz_value_sql},{theta1_degree},{theta2_degree},{theta3_degree},{theta4_degree},{theta5_degree})"
        # cursor.execute(sql_delete)
        cursor.execute(sql)

        update_label(root, "t1", f"{theta1_degree}", x=(590 + 50), y=650)
        update_label(root, "t2", f"{theta2_degree}", x=(650 + 50), y=650)
        update_label(root, "t3", f"{theta3_degree}", x=(710 + 50), y=650)
        update_label(root, "t4", f"{theta4_degree}", x=(770 + 50), y=650)
        update_label(root, "t5", f"{theta5_degree}", x=(830 + 50), y=650)

        print("Float value:", 
        r11_value_sql,
        r12_value_sql,
        r13_value_sql,
        r21_value_sql,
        r22_value_sql,
        r23_value_sql,
        r31_value_sql,
        r32_value_sql,
        r33_value_sql,
        px_value_sql,
        py_value_sql,
        pz_value_sql, 
        )
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid float.")
    


box_r11 = Entry(root,textvariable = r11_value, font=('calibre',10,'normal'),width=6)
box_r11.place(x=600,y=290)

box_r12 = Entry(root,textvariable = r12_value, font=('calibre',10,'normal'),width=6)
box_r12.place(x=700,y=290)

box_r13 = Entry(root,textvariable = r13_value, font=('calibre',10,'normal'),width=6)
box_r13.place(x=800,y=290)

box_r21 = Entry(root,textvariable = r21_value, font=('calibre',10,'normal'),width=6)
box_r21.place(x=600,y=390)

box_r22 = Entry(root,textvariable = r22_value, font=('calibre',10,'normal'),width=6)
box_r22.place(x=700,y=390)

box_r23 = Entry(root,textvariable = r23_value, font=('calibre',10,'normal'),width=6 )
box_r23.place(x=800,y=390)

box_r31 = Entry(root,textvariable = r31_value, font=('calibre',10,'normal'),width=6)
box_r31.place(x=600,y=490)

box_r32 = Entry(root,textvariable = r32_value, font=('calibre',10,'normal'),width=6)
box_r32.place(x=700,y=490)

box_r33 = Entry(root,textvariable = r33_value, font=('calibre',10,'normal'),width=6)
box_r33.place(x=800,y=490)

box_px = Entry(root,textvariable = px_value, font=('calibre',10,'normal'),width=6)
box_px.place(x=900,y=290)

box_py = Entry(root,textvariable = py_value, font=('calibre',10,'normal'),width=6)
box_py.place(x=900,y=390)

box_pz = Entry(root,textvariable = pz_value, font=('calibre',10,'normal'),width=6)
box_pz.place(x=900,y=490)


button1 = Button(root, text="SUBMIT", command=lambda: get_float_value(
    r11_value,
    r12_value,
    r13_value,
    r21_value,
    r22_value,
    r23_value,
    r31_value,
    r32_value,
    r33_value,
    px_value,
    py_value,
    pz_value,
    )
)
button1.place(x=735,y=550)

# button2 = Button(root, text="Use inverse kinematic",command=lambda:inverse_kinematic(root))
# button2.place(x=715,y=590)



theta1_box = Label(text="theta1",font=('calibre',10,'normal')) 
theta1_box.place(x=(590+40),y=605)
theta2_box= Label(text="theta2",font=('calibre',10,'normal'))
theta2_box.place(x=(650+40),y=605)
theta3_box= Label(text="theta3",font=('calibre',10,'normal'))
theta3_box.place(x=(710+40),y=605)
theta4_box= Label(text="theta4",font=('calibre',10,'normal'))
theta4_box.place(x=(770+40),y=605)
theta5_box= Label(text="theta5",font=('calibre',10,'normal'))
theta5_box.place(x=(830+40),y=605)


@connect_sql
def send_theta_values(cursor):
    sql_getdata = "SELECT * FROM tranformation_metrix"
    cursor.execute(sql_getdata)
    data = cursor.fetchall()

    datas = data[-1]
    theta1 = datas[13]
    theta2 = datas[14]
    theta3 = datas[15]
    theta4 = datas[16]
    theta5 = datas[17]
    
    # Create a formatted message with values separated by commas
    message = f"{theta1},{theta2},{theta3},{theta4},{theta5}\n"
    arduino.write(message.encode())  # Send the message to Arduino
    # print(f"Sent {message.strip()} to Arduino")
    time.sleep(0.1)
    while arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        print(f"Arduino says: {line}")

# Example button action to send specific theta values


arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
def send_moveJ():
    arduino.write(b'6\n')  # Send '1' to Arduino
    print("Sent 6 to Arduino")

def send_moveL():
    arduino.write(b'8\n')  # Send '1' to Arduino
    print("Sent 7 to Arduino")

# Function to send '0' to Arduino when stopping
def stop_servo():
    arduino.write(b'7\n')  # Send '0' to Arduino
    print("Sent 7 to Arduino")

@connect_sql
def send_moveL(cursor):
    sql_getdata = "SELECT * FROM tranformation_metrix"
    cursor.execute(sql_getdata)
    data = cursor.fetchall()

    datas = data[-1]
    theta1 = datas[13]
    theta2 = datas[14]
    theta3 = datas[15]
    theta4 = datas[16]
    theta5 = datas[17]

    MOVEL(theta1,theta2,theta3,theta4,theta5,100)

def MOVEL(theta1,theta2,theta3,theta4,theta5,step):

    T0 = forward_kinematic(0,30,90,30,0)
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


    

    theta1 = []
    theta2 = []
    theta3 = []
    theta4 = []
    theta5 = []
    for i in range (step):
        
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
    for i in range(step):
        data = f"{theta1[i]},{theta2[i]},{theta3[i]},{theta4[i]},{theta5[i]}\n"
        arduino.write(data.encode())  # Send data as bytes
        print(f"Sent to Arduino {i+1} : {data.strip()} {(theta_new_axis_per_step*180)/math.pi}")
        time.sleep(0.1)  # Add a slight delay for Arduino to process the data

    return theta1 , theta2 , theta3 , theta4 , theta5 


# MOVEL(120,30,90,30,0,100)


    
    
   



button_movej_run = Button(root, text="RUN",command=send_moveJ)
button_movej_run.place(x=1250,y=420)

button_movej_load = Button(root, text="LOAD" ,command=send_theta_values)
button_movej_load.place(x=1150,y=320)

button_movej_stop = Button(root, text="STOP", command=stop_servo)
button_movej_stop.place(x=1330,y=420)


button_moveL_run = Button(root, text="RUN",command=send_moveL)
button_moveL_run.place(x=1250,y=720)

button_moveL_load = Button(root, text="LOAD" ,command=send_moveL)
button_moveL_load.place(x=1150,y=620)

button_moveL_stop = Button(root, text="STOP",)
button_moveL_stop.place(x=1330,y=720)



root.mainloop()






