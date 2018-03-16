import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import matplotlib.animation as animation
from matplotlib import style

from tkinter import *


matplotlib.use("TkAgg")
readings = []


HEADER1 = ("Verdana", 40)
HEADER2 = ("Courier", 12)
style.use("ggplot")

#dictionary key = gesture name , value = readings in millivolt
gestures={}

gestures['fist'] = [1,2,3,4,5,6,7,8]
gestures['release'] = [1,2,3,4,5,6,7,8]

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(421)
b = f.add_subplot(422)
c = f.add_subplot(423)
d = f.add_subplot(424)
e = f.add_subplot(425)
ff = f.add_subplot(426)
g = f.add_subplot(427)
h = f.add_subplot(428)


def animate(i):
    pullData = open("readings", "r").read()
    dataList = pullData.split('\n')
    xList=[]
    yList=[]

    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))

    global readings
    readings = yList

    a.clear()
    b.clear()
    c.clear()
    d.clear()
    e.clear()
    ff.clear()
    g.clear()
    h.clear()
    a.plot(xList,yList)
    b.plot(xList,yList)
    c.plot(xList,yList)
    d.plot(xList,yList)
    e.plot(xList,yList)
    ff.plot(xList,yList)
    g.plot(xList,yList)
    h.plot(xList,yList)
    


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

        canvas = FigureCanvasTkAgg(f, LeftFrame)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        RightFrame = tk.Frame(self)
        RightFrame.configure(background='black')
        RightFrame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1, anchor=tk.N)

        heading = tk.Label(RightFrame, text='Readings : ', font=HEADER2,background='black',foreground='#42f4e2')
        heading.pack()

        v = StringVar(RightFrame, value='No Connection')


        entry_1 = tk.Entry(RightFrame, width=10,textvariable=v,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_2 = tk.Entry(RightFrame, width=10,textvariable=v,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_3 = tk.Entry(RightFrame, width=10,textvariable=v,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_4 = tk.Entry(RightFrame, width=10,textvariable=v,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_5 = tk.Entry(RightFrame, width=10,textvariable=v,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_6 = tk.Entry(RightFrame, width=10,textvariable=v,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_7 = tk.Entry(RightFrame, width=10,textvariable=v,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)
        entry_8 = tk.Entry(RightFrame, width=10,textvariable=v,background='black',foreground='#42f4e2',relief=FLAT,highlightthickness=0,bd=15)

        entry_1.pack()
        entry_2.pack()
        entry_3.pack()
        entry_4.pack()
        entry_5.pack()
        entry_6.pack()
        entry_7.pack()
        entry_8.pack()




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
