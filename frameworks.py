#------ Import
from tkinter import *
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import matplotlib.pyplot as plt 
import tkinter as tk
import tkinter.ttk as ttk
import serial
import numpy as np
import threading 
#------------- End

root = tk.Tk()
root.title("liquid frameworks")
root.geometry("500x800")
root.resizable(False,False)



# combo box 만드는 class , member 변수 초기화 위에서 시켜주고
# input으로 글자 입력받으면 각기 다른 네임으로 초기화 시켜줌 --> def make_combo 의 역할
# 글자 넣어주면 해당 글자의 배열에서 값을 출력해줌.get() --> def getU 의 역할
# combobox 만들어서 Digital, Analog 범주 고르면, 해당 핀 체크 박스로 쭈욱 뜨면서 몇번 필 쓸건지 체크
class combo_make() :
    def __init__ (self) :
        self.box_data_board = ["Arduino","STM32","Atmega128","Atmega328P"]
        self.box_data_baud = [4800, 9600, 19200, 31250, 38400, 57600, 115200]
        self.box_data_dev = ["/dev/ttyUSB0","/dev/ttyUSB1","/dev/ttyUSB2","COM1","COM2","COM3","COM4"]
        self.box_data_ino = ["digital","Analog"]
        self.x = 0
        self.y = 0
        self.box_name_init = 0
        self.selection = 0
        self.name = 0

    def make_combo (self,name : str, x: int, y: int ) :
        self.x = x
        self.y = y
        
        if name == "board" :
            self.box_name_init = ttk.Combobox(root)
            self.box_name_init.config(height = 5)
            self.box_name_init.config(value = self.box_data_board)
            self.box_name_init.place(x = self.x, y = self.y)
            self.box_name_init.config(state = "readonly")
            self.box_name_init.set(name)
            self.name = name
            
        elif name == "baud" :
            self.box_name_init = ttk.Combobox(root)
            self.box_name_init.config(height = 5)
            self.box_name_init.config(value = self.box_data_baud)
            self.box_name_init.place(x = self.x, y = self.y)
            self.box_name_init.config(state = "readonly")
            self.box_name_init.set(name)
            self.name = name
            
        elif name == "dev" :
            self.box_name_init = ttk.Combobox(root)
            self.box_name_init.config(height = 5)
            self.box_name_init.config(value = self.box_data_dev)
            self.box_name_init.place(x = self.x, y = self.y)
            self.box_name_init.config(state = "readonly")
            self.box_name_init.set(name)
            self.name = name
            
        elif name == "pin_":
            self.box_name_init = ttk.Combobox(root)
            self.box_name_init.config(height = 5)
            self.box_name_init.config(value = self.box_data_ino)
            self.box_name_init.place(x = self.x, y = self.y)
            self.box_name_init.config(state = "readonly")
            self.box_name_init.set(name)
            self.name = name
            
    def getU(self,name : str):
        if name == "board":
            return self.box_name_init.get()
        if name == "baud":
            return self.box_name_init.get()
        if name == "dev":
            return self.box_name_init.get()
        if name == "pin_" :
            return self.box_name_init.get()

class check_make(combo_make) :
    ## Using inheritance, make check box class
    def __init__ (self ) : 
        super().__init__() 
        self.Digital_Pin = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.Analog_Pin = ["A0","A1","A2","A3","A4","A5"]
        self.temp = []
        self.checking = []
    def check_(self,using_combo):  
        # if annotion string is digial 
        # make type of variable " INT " i for checkbox indexes
        self.temp = self.Digital_Pin
        self.checking = using_combo.getU("pin_")
        for i in range(len(self.Digital_Pin)) :
            globals()['check_box_{}'.format(i)] = self.Digital_Pin[i]
            print(globals())
            # check_box1 = 0
            # check_box2 = 1
            
"""
check_var1 = IntVar()
c1 = Checkbutton(root, text='digital', variable=check_var1)
c1.place(x=10, y = 200)
        
"""
     
                
                
#############################
######## Definition of Button
##############################

#button  만드는 class, 위의 combomake class 처럼 
# 맴버변수로 초기화, 이름으로 라벨링을 따로해줘서  btn 클래스 위에 있는 
# 함수들을 이름대로 가져다 쓸 수 있게 만들어야 함 
def btnpress() :
    a = []
    a.append(board_combo.getU("board"))
    a.append(baud_combo.getU("baud"))
    a.append(dev_combo.getU("dev"))

    lb.config(text = a )
    print("Initiating Arudino Serial")
    py_serial = serial.Serial(port=dev_combo.getU("dev"), baudrate = baud_combo.getU("baud"))
    check_sum.check_(using_combo)
###############################
######### Definition end ######
################################
class btn_make() :
    def __init__(self) :
        self.btn_make_init = 0
        self.btn_msg = 0
        self.btn_size = 0
        self.x = 0 # location data
        self.y = 0
    def make_btn(self, text : str, cmd : str, x, y, size : int):
        self.btn_make_init = tk.Button(root)
        self.btn_make_init.config(width= size)
        self.btn_make_init.config(text = text)
        self.btn_make_init.config(command = cmd)
        self.btn_make_init.place(x = x, y = y)
        # 이부분 어떻게 처리할지 몰라서 그냥 if 문으로 처리중
        # 방법을알면 금방할거같은데 
        
        if cmd == "btnpress" : 
            self.btn_make_init.config(command= btnpress)
        
###################################################
###################################################
# END OF button class #############################
###################################################


"""
    그래프 보여지면, 해당핀-->data 까지 읽어올 수 있게 끔 만들고 싶음
    위의 콤보박스 class로 만들어서 관리할 필요 있음 
    아래의 matplotlib 관련된 내용도 반복문이나 클래스로 해야할 필요 있음 
    
"""


board_combo = combo_make()
baud_combo  = combo_make()
dev_combo = combo_make()
using_combo = combo_make()

board_combo.make_combo("board",10,10)
baud_combo.make_combo("baud",10,40)
dev_combo.make_combo("dev",10,70)    
using_combo.make_combo("pin_",10,100) 
        

check_sum = check_make()


btn_1 = btn_make()
btn_1.make_btn("connect", "btnpress" , 5, 130, 15)


lb = tk.Label(root)
lb.config(text = "normal_state")
lb.place(x= 5, y = 780)

root.mainloop()
 
