#------ Import
from tkinter import *
from pandas import DataFrame
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import matplotlib.pyplot as plt 
import tkinter as tk
import tkinter.ttk as ttk
import serial
import numpy as np
from threading import Thread
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
      
            
    def getU(self,name : str):
        if name == "board":
            return self.box_name_init.get()
        if name == "baud":
            return self.box_name_init.get()
        if name == "dev":
            return self.box_name_init.get()


            
class pin_check(combo_make) : # 해당핀 고르면 전체핀이 그냥 뜨는걸로
    def __init__ (self) :
        self.x_place = 0
        self.y_place = 0
        self.Arduino_Pin = ["A0", "A1", "A2", "A3", "A4", "A5", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.check_boxes = [] 
        
        
    def make_pin_check(self,board_combo) :

        Pins = self.Arduino_Pin if board_combo.getU("board") == "Arduino" else 0
        
        for i, pin in enumerate(Pins) : 
            var = tk.IntVar()
            check_box = tk.Checkbutton(root, text = str(pin), variable= var)
            check_box.place(x= 10, y=170 + i * 20)
            self.check_boxes.append(var)
            #print(self.check_boxes) # debug code, print out data
            a = 0
        
        
        
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
    pin_debug.make_pin_check(board_combo)
    
    #check_sum.check_(using_combo)


## kill shot button
def exitpress():
    exit()
def disconnect():
    pass
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
        
        if cmd == "btnpress"  : 
            self.btn_make_init.config(command= btnpress)
        if cmd == "exitpress" : # killshot switch
            self.btn_make_init.config(command=  exitpress)
        if cmd == "disconnect":
            self.btn_make_init.config(command= disconnect)
        
###################################################
###################################################
# END OF button class #############################
###################################################


"""
    그래프 보여지면, 해당핀-->data 까지 읽어올 수 있게 끔 만들고 싶음
    위의 콤보박스 class로 만들어서 관리할 필요 있음 
    아래의 matplotlib 관련된 내용도 반복문이나 클래스로 해야할 필요 있음 
    
"""

"""
MATPLOTLIB 
"""


class draw_graph(pin_check) :
    def __init__ (self) :
        self.data_recieve = []
        self.data_transmit = []
        self.data_x = []
        self.data_y = []
        self.figsize = ()
        
    def make_graph(self,figsize,dpi, subplot,x,y) :
        
        # 그래프 기본 속성 생성 
        # 값을 받아오면 pyserial 로 
        # 그값을 자동으로 받아와서 리스트에 
        # FIFO 구조로 리스트의 값을 그래프로 그리고싶다
        self.df = DataFrame(self.data_recieve, columns= ['time','t'])
        self.figsize = figsize
        self.dpi     = dpi
        self.subplot = subplot
        # 시간 정보는 어떻게 받아옴?
        # 그냥 데이터는 어떻게 리스트로 저장함?
        
        self.x_place = x
        self.y_place = y
        self.figure = plt.Figure(self.figsize, self.dpi)
        self.ax = self.figure.add_subplot(self.subplot)
        self.line = FigureCanvasTkAgg(self.figure, root)
        self.line.get_tk_widget().place(x= self.x_place,y= self.y_place)
        
        """
        

        self.df2 = self.df2[['time','Y']].groupby('time').sum()
        
        """

        
        


grid_figure = draw_graph()
grid_figure.make_graph((3,1), 100, 111,200,50)
        


        

board_combo = combo_make()
baud_combo  = combo_make()
dev_combo = combo_make()
using_combo = combo_make()

board_combo.make_combo("board",10,10)
baud_combo.make_combo("baud",10,40)
dev_combo.make_combo("dev",10,70)    
using_combo.make_combo("pin_",10,100) 

pin_debug = pin_check()

#check_sum = check_make()


btn_connect = btn_make()
btn_connect.make_btn("connect", "btnpress" , 5, 130, 10)

btn_disconnect = btn_make()
btn_disconnect.make_btn("disconnect","disconnect", 90, 130, 10)

btn_exit = btn_make()
btn_exit.make_btn("exit", "exitpress", 450, 0, 5)



lb = tk.Label(root)
lb.config(text = "normal_state")
lb.place(x= 5, y = 780)

root.mainloop()
 
