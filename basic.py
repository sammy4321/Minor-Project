import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
from tkinter import *
import threading
import time
import random
import numpy as np
import collections

matplotlib.use("TkAgg")
readings = []


HEADER1 = ("Verdana", 40)
HEADER2 = ("Courier", 12)
style.use("ggplot")

#dictionary key = gesture name , value = readings in millivolt
gestures={}

gestures['fist'] = [1,2,3,4,5,6,7,8]
gestures['release'] = [1,2,3,4,5,6,7,8]

class demo_thread(threading.Thread):
    def __init__(self,e1,e2,e3,e4,e5,e6,e7,e8,ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,canvas):
        threading.Thread.__init__(self)
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
        self.e4 = e4
        self.e5 = e5
        self.e6 = e6
        self.e7 = e7
        self.e8 = e8
        self.ax1=ax1
        self.ax2=ax2
        self.ax3=ax3
        self.ax4=ax4
        self.ax5=ax5
        self.ax6=ax6
        self.ax7=ax7
        self.ax8=ax8
        self.id = id
        self.canvas = canvas
    def run(self):
        #print('hey')
        flag = True
        m=100
        n=100
        i=2
        x1 = collections.deque(100*[0],100)
        x2 = collections.deque(100*[0],100)
        x3 = collections.deque(100*[0],100)
        x4 = collections.deque(100*[0],100)
        x5 = collections.deque(100*[0],100)
        x6 = collections.deque(100*[0],100)
        x7 = collections.deque(100*[0],100)
        x8 = collections.deque(100*[0],100)
        while flag:
            
            random_number1 = random.randint(-3,3)
            random_number2 = random.randint(-3,3)
            random_number3 = random.randint(-3,3)
            random_number4 = random.randint(-3,3)
            random_number5 = random.randint(-3,3)
            random_number6 = random.randint(-3,3)
            random_number7 = random.randint(-3,3)
            random_number8 = random.randint(-3,3)
            x1.appendleft(random_number1)
            x2.appendleft(random_number2)
            x3.appendleft(random_number3)
            x4.appendleft(random_number4)
            x5.appendleft(random_number5)
            x6.appendleft(random_number6)
            x7.appendleft(random_number7)
            x8.appendleft(random_number8)
            matrix1 = np.random.normal(0,1,m*n).reshape(m,n)
            matrix2 = np.random.normal(0,1,m*n).reshape(m,n)
            matrix3 = np.random.normal(0,1,m*n).reshape(m,n)
            matrix4 = np.random.normal(0,1,m*n).reshape(m,n)
            matrix5 = np.random.normal(0,1,m*n).reshape(m,n)
            matrix6 = np.random.normal(0,1,m*n).reshape(m,n)
            matrix7 = np.random.normal(0,1,m*n).reshape(m,n)
            matrix8 = np.random.normal(0,1,m*n).reshape(m,n)

            #print(random_number)
            #time.sleep(1)
            try:
                self.ax1.clear()
                self.ax2.clear()
                self.ax3.clear()
                self.ax4.clear()
                self.ax5.clear()
                self.ax6.clear()
                self.ax7.clear()
                self.ax8.clear()
                self.ax1.axis([0, 100, -4, 4])
                self.ax2.axis([0, 100, -4, 4])
                self.ax3.axis([0, 100, -4, 4])
                self.ax4.axis([0, 100, -4, 4])
                self.ax5.axis([0, 100, -4, 4])
                self.ax6.axis([0, 100, -4, 4])
                self.ax7.axis([0, 100, -4, 4])
                self.ax8.axis([0, 100, -4, 4])
                self.ax1.plot(np.array(x1))
                self.ax2.plot(np.array(x2))
                self.ax3.plot(np.array(x3))
                self.ax4.plot(np.array(x4))
                self.ax5.plot(np.array(x5))
                self.ax6.plot(np.array(x6))
                self.ax7.plot(np.array(x7))
                self.ax8.plot(np.array(x8))
                self.canvas.draw()
                self.e1.delete(0,tk.END)
                self.e1.insert(0,str(random_number1))
                self.e2.delete(0,tk.END)
                self.e2.insert(0,str(random_number2))
                self.e3.delete(0,tk.END)
                self.e3.insert(0,str(random_number3))
                self.e4.delete(0,tk.END)
                self.e4.insert(0,str(random_number4))
                self.e5.delete(0,tk.END)
                self.e5.insert(0,str(random_number5))
                self.e6.delete(0,tk.END)
                self.e6.insert(0,str(random_number6))
                self.e7.delete(0,tk.END)
                self.e7.insert(0,str(random_number7))
                self.e8.delete(0,tk.END)
                self.e8.insert(0,str(random_number8))
                #time.sleep(1)
            except Exception :
                #print(Exception)
                flag = False

class save_thread(threading.Thread):
    def __init__(self,e1,e2,e3,e4,e5,e6,e7,e8):
        threading.Thread.__init__(self)
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
        self.e4 = e4
        self.e5 = e5
        self.e6 = e6
        self.e7 = e7
        self.e8 = e8
        self.id = id
    def run(self):
        #print('hey')
        flag = True
        while flag:
            random_number1 = random.randint(0,100)
            random_number2 = random.randint(0,100)
            random_number3 = random.randint(0,100)
            random_number4 = random.randint(0,100)
            random_number5 = random.randint(0,100)
            random_number6 = random.randint(0,100)
            random_number7 = random.randint(0,100)
            random_number8 = random.randint(0,100)
            #print(random_number)
            #time.sleep(1)
            try:
                self.e1.delete(0,tk.END)
                self.e1.insert(0,str(random_number1))
                self.e2.delete(0,tk.END)
                self.e2.insert(0,str(random_number2))
                self.e3.delete(0,tk.END)
                self.e3.insert(0,str(random_number3))
                self.e4.delete(0,tk.END)
                self.e4.insert(0,str(random_number4))
                self.e5.delete(0,tk.END)
                self.e5.insert(0,str(random_number5))
                self.e6.delete(0,tk.END)
                self.e6.insert(0,str(random_number6))
                self.e7.delete(0,tk.END)
                self.e7.insert(0,str(random_number7))
                self.e8.delete(0,tk.END)
                self.e8.insert(0,str(random_number8))
                time.sleep(1)
            except:
                flag = False
class MyoArm(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.wm_title(self , "Myo Arm")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, DemoPage, AddGesturePage):
            frame = F(container , self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self , cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='black')
        label = tk.Label(self, text="Myo Arm", font=HEADER1,background ='black',foreground='#c5d0e2')
        label.pack(pady=10, padx=10)

        TEXT = "Detect and predict hand gestures using Myo Armband"

        text = tk.Label(self, text=TEXT, font=HEADER2,background = 'black',foreground = '#42f4e2')
        text.pack()

        photo1 = tk.PhotoImage(file = 'letsgetstarted(1).png')

        button1 = tk.Button(self, compound = tk.TOP,width = 163,height = 49,
                            command=lambda : controller.show_frame(PageOne),image=photo1,relief = FLAT,bd = 0,highlightthickness=0,bg = 'black',activebackground='black',padx=0,pady=0)
        button1.pack()
        button1.image = photo1
        button1.place(x = 220,y=400)
        



class DemoPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='black')
        label = tk.Label(self, text="Demo Page", font=HEADER1,background='black',foreground='#c5d0e2')
        label.pack(pady=10, padx=10)

        photo1 = tk.PhotoImage(file = 'backk.png')

        button1 = tk.Button(self, compound=tk.TOP,width = 143,height = 48,
                            command=lambda : controller.show_frame(PageOne),image=photo1,relief = FLAT,bd = 0,highlightthickness=0,bg = 'black',activebackground='black',padx=0,pady=0)
        button1.pack()
        #button1.pack()
        button1.image = photo1


        LeftFrame = tk.Frame(self)
        LeftFrame.configure(background='black')
        LeftFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor=tk.N)

        f = Figure(figsize=(5, 5), dpi=100)
        ax1 = f.add_subplot(421)
        ax2 = f.add_subplot(422)
        ax3 = f.add_subplot(423)
        ax4 = f.add_subplot(424)
        ax5 = f.add_subplot(425)
        ax6 = f.add_subplot(426)
        ax7 = f.add_subplot(427)
        ax8 = f.add_subplot(428)

        #ax1 = fig.add_pyplot()
        canvas = FigureCanvasTkAgg(f, LeftFrame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        RightFrame = tk.Frame(self)
        RightFrame.configure(background='black')
        RightFrame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1, anchor=tk.N)

        heading = tk.Label(RightFrame, text='Readings : ', font=HEADER2,background='black',foreground='#42f4e2')
        heading.pack()

        v = StringVar(RightFrame, value='No Connection')


        entry_1 = tk.Entry(RightFrame, width=10,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_2 = tk.Entry(RightFrame, width=10,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_3 = tk.Entry(RightFrame, width=10,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_4 = tk.Entry(RightFrame, width=10,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_5 = tk.Entry(RightFrame, width=10,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_6 = tk.Entry(RightFrame, width=10,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_7 = tk.Entry(RightFrame, width=10,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_8 = tk.Entry(RightFrame, width=10,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)

        entry_1.pack()
        entry_2.pack()
        entry_3.pack()
        entry_4.pack()
        entry_5.pack()
        entry_6.pack()
        entry_7.pack()
        entry_8.pack()

        demo_thread_controller = demo_thread(entry_1,entry_2,entry_3,entry_4,entry_5,entry_6,entry_7,entry_8,ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,canvas)
        demo_thread_controller.start()




class AddGesturePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='black')
        label = tk.Label(self, text="Save Gestures", font=HEADER1,background='black',foreground='#c5d0e2')
        label.pack(pady=10, padx=10)

        v1 = StringVar(self, value='No Connection')
        v2 = StringVar(self, value='No Connection')
        v3 = StringVar(self, value='No Connection')
        v4 = StringVar(self, value='No Connection')
        v5 = StringVar(self, value='No Connection')
        v6 = StringVar(self, value='No Connection')
        v7 = StringVar(self, value='No Connection')
        v8 = StringVar(self, value='No Connection')

        entry_1 = tk.Entry(self, width=10,textvariable=v1,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_2 = tk.Entry(self, width=10,textvariable=v2,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_3 = tk.Entry(self, width=10,textvariable=v3,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_4 = tk.Entry(self, width=10,textvariable=v4,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_5 = tk.Entry(self, width=10,textvariable=v5,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_6 = tk.Entry(self, width=10,textvariable=v6,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_7 = tk.Entry(self, width=10,textvariable=v7,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_8 = tk.Entry(self, width=10,textvariable=v8,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)

        entry_1.pack()
        entry_2.pack()
        entry_3.pack()
        entry_4.pack()
        entry_5.pack()
        entry_6.pack()
        entry_7.pack()
        entry_8.pack()

        save_thread_controller = save_thread(entry_1,entry_2,entry_3,entry_4,entry_5,entry_6,entry_7,entry_8)
        save_thread_controller.start()





        #tag = tk.Label(self, text="Current Gestures", font=HEADER2)
        #tag.grid(row=1)

        #for i , name in enumerate(gestures):
            #name_label = tk.Label(self, text=name, font=HEADER2)
            #name_label.grid(row=i+2)


        vn = StringVar(self,value='Enter Name of Gesture Here')
        entry_n = tk.Entry(self,textvariable=vn,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_n.pack()

        def saveValues():
        	e1 = entry_1.get()
        	e2 = entry_2.get()
        	e3 = entry_3.get()
        	e4 = entry_4.get()
        	e5 = entry_5.get()
        	e6 = entry_6.get()
        	e7 = entry_7.get()
        	e8 = entry_8.get()
        	en = entry_n.get()

        	text_to_save = en+'-'+e1+','+e2+','+e3+','+e4+','+e5+','+e6+','+e7+','+e8+'\n'

        	f= open('gestures','a')
        	ff = open('activate_functions.py','a')
        	ff.write('def '+en+'():\n')
        	ff.write('\tprint("Inside Function '+en+'")\n\n')
        	ff.close()
        	f.write(text_to_save)

        	f.close()
        	bc = StringVar(self,value='Saved Successfully')
        	entry_n.config(textvariable=bc)

        photo0 = tk.PhotoImage(file = 'save.png')
        button0 = tk.Button(self,compound=tk.TOP,width=143,height=48,command=saveValues,image=photo0,relief = FLAT,bd = 0,highlightthickness=0,bg = 'black',activebackground='black',padx=0,pady=0)
        button0.pack()
        button0.image = photo0

        photo1 = tk.PhotoImage(file = 'backk.png')
        button1 = tk.Button(self, compound=tk.TOP,width = 143,height = 48,
                            command=lambda : controller.show_frame(PageOne),image=photo1,relief = FLAT,bd = 0,highlightthickness=0,bg = 'black',activebackground='black',padx=0,pady=0)
        button1.pack()
        button1.image = photo1


class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='black')
        label = tk.Label(self, text="Welcome to Myo Arm", font=HEADER1,background='black',foreground='#c5d0e2')
        label.pack(pady=10, padx=10)
        photo1 = tk.PhotoImage(file = 'readgesture(1).png')

        button1 = tk.Button(self, compound = tk.TOP,width=145,height=145,image=photo1,
                            command=lambda : controller.show_frame(DemoPage),relief = FLAT,bd = 0,highlightthickness = 0,bg = 'black',activebackground='black',padx=0,pady=0)
        button1.pack()
        button1.image = photo1
        button1.place(x=100,y=200)

        photo2 = tk.PhotoImage(file = 'savegesture(1).png')

        button2 = tk.Button(self,compound = tk.TOP,width=145,height=145,image=photo2,
                            command=lambda : controller.show_frame(AddGesturePage),relief = FLAT,bd = 0,highlightthickness = 0,bg = 'black',activebackground='black',padx=0,pady=0)

        button2.pack()
        button2.image = photo2

        button2.place(x=350,y=200)
        photo3 = tk.PhotoImage(file = 'back(1).png')



        button3 = tk.Button(self, compound = tk.TOP,width=145,height=145,image=photo3,
                            command=lambda : controller.show_frame(StartPage),relief = FLAT,bd = 0,highlightthickness = 0,bg = 'black',activebackground='black',padx=0,pady=0)
        button3.pack()
        button3.image = photo3
        button3.place(x=225,y=350)

        # testButton = ttk.Button(self, text="test",
        #                     command=lambda : controller.show_frame(TestPage))
        # testButton.pack()



myapp = MyoArm()
myapp.mainloop()
