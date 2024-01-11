import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import tkinter.ttk as ttk
import serial
import numpy as np


def btnpress() :
    a = []
    a.append(board_combo.getU("board"))
    a.append(baud_combo.getU("baud"))
    a.append(dev_combo.getU("dev"))
    lb.config(text = a )
    print("Initiating Arudino Serial")
    py_serial = serial.Serial(port=dev_combo.getU("dev"), baudrate = baud_combo.getU("baud"))

    
btn1 = tk.Button(root)
btn1.config(text = "connect")
btn1.config(width = 15)
btn1.config(command = btnpress)
btn1.place(x = 5, y = 110)

class combo_make() :
    def __init__ (self) :
        self.box_data_board = ["Arduino","STM32","Atmega128","Atmega328P"]
        self.box_data_baud = [4800, 9600, 19200, 31250, 38400, 57600, 115200]
        self.box_data_dev = ["/dev/ttyUSB0","/dev/ttyUSB1","/dev/ttyUSB2"]
        self.x = 0
        self.y = 0
        self.box_name_init = 0
        self.selection = 0
        
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
        elif name == "baud" :
            self.box_name_init = ttk.Combobox(root)
            self.box_name_init.config(height = 5)
            self.box_name_init.config(value = self.box_data_baud)
            self.box_name_init.place(x = self.x, y = self.y)
            self.box_name_init.config(state = "readonly")
            self.box_name_init.set(name)
        elif name == "dev" :
            self.box_name_init = ttk.Combobox(root)
            self.box_name_init.config(height = 5)
            self.box_name_init.config(value = self.box_data_dev)
            self.box_name_init.place(x = self.x, y = self.y)
            self.box_name_init.config(state = "readonly")
            self.box_name_init.set(name)
            
    def getU(self,name : str):
        if name == "board":
            return self.box_name_init.get()
        if name == "baud":
            return self.box_name_init.get()
        if name == "dev":
            return self.box_name_init.get()

class btn_make() :
    def __init__(self) :
        self.btn_make_init = 0
        self.btn_msg = 0
        self.x = 0 # location data
        self.y = 0
    def make_btn(self,cmd :str, x, y):
        self.btn_make_init = tk.Button(root)
        self.btn_make_init.config(width=15)


root = tk.Tk()
root.title("liquid frameworks")
root.geometry("1200x800")
root.resizable(False,False)



"""
figure1 = plt.figure(figsize=(4,3), dpi = 100)
ax1 = figure1.add_subplot(111)
canvas = FigureCanvasTkAgg(figure1, master = root)
canvas.draw()
canvas.get_tk_widget().place(x=250,y=50)


figure2 = plt.figure(figsize=(4,3), dpi = 100)
ax2 = figure2.add_subplot(111)
canvas = FigureCanvasTkAgg(figure2, master = root)
canvas.draw()
canvas.get_tk_widget().place(x=700,y=50)



figure3 = plt.figure(figsize=(4,3), dpi = 100)
ax3 = figure3.add_subplot(111)
canvas = FigureCanvasTkAgg(figure3, master = root)
canvas.draw()
canvas.get_tk_widget().place(x=250,y=400)

figure4 = plt.figure(figsize=(4,3), dpi = 100)
ax4 = figure4.add_subplot(111)
canvas = FigureCanvasTkAgg(figure4, master = root)
canvas.draw()
canvas.get_tk_widget().place(x=700,y=400)


    그래프 보여지면, 해당핀-->data 까지 읽어올 수 있게 끔 만들고 싶음
    위의 콤보박스 class로 만들어서 관리할 필요 있음 
    아래의 matplotlib 관련된 내용도 반복문이나 클래스로 해야할 필요 있음 
    
"""


board_combo = combo_make()
baud_combo  = combo_make()
dev_combo = combo_make()
board_combo.make_combo("board",10,10)
baud_combo.make_combo("baud",10,40)
dev_combo.make_combo("dev",10,70)     




lb = tk.Label(root)
lb.config(text = "done")
lb.place(x= 5, y = 780)

root.mainloop()