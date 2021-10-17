import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import requests
class Convertor(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.grid()
        self.text1=tk.Label(text="Multi-Convertor Tool",bg="#FF5500",fg="white",font=("Algerian",40),relief=tk.RAISED,bd=3)
        self.text1.grid(row=0,column=1,padx=50,pady=30)
        self.text2=tk.Button(text="MASS",font=("Comic Sans MS",20),bg="#87CEEB",command=self.Mass)
        self.text2.grid(row=2,column=0,padx=50,pady=30)
        self.text3=tk.Button(text="AREA",font=("Comic Sans MS",20),bg="#87CEEB",command=self.Area)
        self.text3.grid(row=2,column=1,padx=50,pady=30)
        self.text4=tk.Button(text="SPEED",font=("Comic Sans MS",20),bg="#87CEEB",command=self.Speed)
        self.text4.grid(row=2,column=2,padx=50,pady=30)
        self.text5=tk.Button(text="LENGTH",font=("Comic Sans MS",20),bg="#87CEEB",command=self.Length)
        self.text5.grid(row=4,column=0,padx=50,pady=30)
        self.text6=tk.Button(text="DENSITY",font=("Comic Sans MS",20),bg="#87CEEB",command=self.Density)
        self.text6.grid(row=4,column=1,padx=50,pady=30)
        self.text2=tk.Button(text="VOLUMN",font=("Comic Sans MS",20),bg="#87CEEB",command=self.Volumn)
        self.text2.grid(row=4,column=2,padx=50,pady=30)
        self.text4=tk.Button(text="CURRENCY",font=("Comic Sans MS",20),bg="#87CEEB",command=self.Currency)
        self.text4.grid(row=6,column=0,padx=50,pady=30)
        self.text5=tk.Button(text="TEMPERATURE",font=("Comic Sans MS",20),bg="#87CEEB",command=self.Temperature)
        self.text5.grid(row=6,column=1,padx=50,pady=30)
        self.text6=tk.Button(text="PLANE ANGLE",font=("Comic Sans MS",20),bg="#87CEEB",command=self.PlaneAngle)
        self.text6.grid(row=6,column=2,padx=50,pady=30)
        self.text6=tk.Button(text="TORQUE",font=("Comic Sans MS",20),bg="#87CEEB",command=self.Torque)
        self.text6.grid(row=8,column=1,padx=50,pady=30)
    def Length(self):
        self.w=tk.Toplevel(self)
        self.w.title("Length")
        self.w.geometry("619x350")
        self.load=Image.open("2.jpeg")
        self.render=ImageTk.PhotoImage(self.load)
        self.img=tk.Label(self.w,image=self.render)
        self.img.place(x=0,y=0)
        self.w.resizable(0,0)
        self.Wi=tk.Frame(self.w)
        #self.Wi.grid(row=0,column=1,padx=50,pady=30)
        self.Wi.grid(row=0,column=0,padx=50,pady=30)
        self.text3=tk.Label(self.Wi,
                            text='''Welcome to the Length Convertor''',bg='white',fg="black",font=("Berlin Sans FB Demi",26),borderwidth=3,relief=tk.RAISED)
        self.text3.grid()
        self.n1= tk.StringVar()
        self.n2= tk.StringVar()
        self.fromchoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n1,state='readonly',font=("Comic Sans MS",11))
        self.fromchoosen['values'] = ('Kilometer',  
                          'Meter', 
                          'Centimeter', 
                          'Millimeter', 
                          'Mile', 
                          'Yard', 
                          'Foot', 
                          'Inch'   
                                 )  
        #self.fromchoosen.grid(row=4,column=0,padx=50,pady=30)
        #self.fromchoosen.grid()
        self.fromchoosen.place(x = 65, y= 120)
        self.fromchoosen.current(0)
        self.tochoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n2,state='readonly',font=("Comic Sans MS",11))
        self.tochoosen['values'] = ('Kilometer',  
                          'Meter', 
                          'Centimeter', 
                          'Millimeter', 
                          'Mile', 
                          'Yard', 
                          'Foot', 
                          'Inch'
                                 )  
        #self.tochoosen.grid(row=4,column=1,padx=50,pady=30)
        #self.tochoosen.grid()
        self.tochoosen.place(x = 385, y= 120)
        self.tochoosen.current(1)
        self.n3=tk.StringVar()
        self.fromentry= tk.Entry(self.w,fg = 'black', bg = 'white',bd=3,width = 20,textvariable=self.n3,font=("",12))
        #self.fromentry.grid(row=6,column=1,padx=10,pady=10)
        #self.fromentry.grid()
        self.fromentry.place(x = 65, y = 180)
        #self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 25)
        self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 20,relief = tk.RIDGE, justify = tk.CENTER,  borderwidth = 3,font=("",12))
        #self.toentry.grid(row=6,column=3,padx=10,pady=10)
        #self.toentry.grid()
        self.toentry.place(x = 385, y = 180)
        self.convert1=tk.Button(self.w,text="  Convert  ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.check1)
        self.convert1.config(font=('Harlow Solid Italic', 10, 'bold'))
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.convert1.place(x = 320, y = 240)
        self.convert1.place(x = 245, y = 240)
        # this is the same thing
        self.back1=tk.Button(self.w,text="      Back      ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.w.destroy)
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.back1.place(x = 245, y = 240)
        self.back1.place(x = 320, y = 240)
    def check1(self):
        self.x3=self.n3.get()
        try:
            val = int(self.x3)
            self.calc1()
        except ValueError:
            try:
                val = float(self.x3)
                self.calc1()
            except ValueError:
                self.showmesg()
    def showmesg(self):
        messagebox.showerror("Error", message="Please enter the valid value")
    def calc1(self):
        self.x1=self.fromchoosen.get()
        self.x2=self.tochoosen.get()
        self.x3=self.n3.get()
        if(str(self.x1)=='Millimeter' and str(self.x2)=='Centimeter'):
            self.toentry.config(text = self.x1)
            c=float(self.x3)/10
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Millimeter' and str(self.x2)=='Meter'):
            c=float(self.x3)/1000
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Millimeter' and str(self.x2)=='Kilometer'):
            c=float(self.x3)*0.000001
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Millimeter' and str(self.x2)=='Inch'):
            c=float(self.x3)*0.03937
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Millimeter' and str(self.x2)=='Foot'):
            c=float(self.x3)*0.003281 
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Millimeter' and str(self.x2)=='Yard'):
            c=float(self.x3)*0.001094 
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Millimeter' and str(self.x2)=='Mile'):  
            c=float(self.x3)*0.000000621
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Centimeter' and str(self.x2)=='Meter'):
            c=float(self.x3)*0.01 
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Centimeter' and str(self.x2)=='Kilometer'):
            c=float(self.x3)*0.00001 
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Centimeter' and str(self.x2)=='Inch'):
            c=float(self.x3)*0.393701
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Centimeter' and str(self.x2)=='Foot'):
            c=float(self.x3)*0.032808
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Centimeter' and str(self.x2)=='Yard'):
            c=float(self.x3)*0.010936
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Centimeter' and str(self.x2)=='Mile'):
            c=float(self.x3)*0.000006
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Meter' and str(self.x2)=='Kilometer'):
            c=float(self.x3)*0.001
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Meter' and str(self.x2)=='Inch'):
            c=float(self.x3)*9.37008
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Meter' and str(self.x2)=='Foot'):
            c=float(self.x3)*3.28084
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Meter' and str(self.x2)=='Yard'):
            c=float(self.x3)*1.093613
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Meter' and str(self.x2)=='Mile'):
            c=float(self.x3)*0.000621
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Kilometer' and str(self.x2)=='Inch'):
            c=float(self.x3)*39370.08
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Kilometer' and str(self.x2)=='Foot'):
            c=float(self.x3)*3280.84
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Kilometer' and str(self.x2)=='Yard'):
            c=float(self.x3)*1093.613
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Kilometer' and str(self.x2)=='Mile'):
            c=float(self.x3)*0.621371
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Inch' and str(self.x2)=='Foot'):
            c=float(self.x3)*0.083333 
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Inch' and str(self.x2)=='Yard'):
            c=float(self.x3)*0.027778
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Inch' and str(self.x2)=='Mile'):
            c=float(self.x3)*0.000016
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Foot' and str(self.x2)=='Yard'):
            c=float(self.x3)*0.333333
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Foot' and str(self.x2)=='Mile'):
            c=float(self.x3)*0.000189
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Yard' and str(self.x2)=='Mile'):
            c=float(self.x3)*0.000568
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Mile' and str(self.x2)=='Yard'):
            c=float(self.x3)*1760
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Mile' and str(self.x2)=='Foot'):
            c=float(self.x3)*5280
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Mile' and str(self.x2)=='Inch'):
            c=float(self.x3)*63360
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Mile' and str(self.x2)=='Kilometer'):
            c=float(self.x3)*1.609344
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Mile' and str(self.x2)=='meter'):
            c=float(self.x3)*1609.344
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Mile' and str(self.x2)=='Centimeter'):
            c=float(self.x3)*160934.4
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Mile' and str(self.x2)=='Millimeter'):
            c=float(self.x3)*1609344
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Yard' and str(self.x2)=='Foot'):
            c=float(self.x3)*3
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Yard' and str(self.x2)=='Inch'):
            c=float(self.x3)*36
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Yard' and str(self.x2)=='Kilometer'):
            c=float(self.x3)*0.000914
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Yard' and str(self.x2)=='Meter'):
            c=float(self.x3)*0.9144
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Yard' and str(self.x2)=='Centimeter'):
            c=float(self.x3)*91.44
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Yard' and str(self.x2)=='Millimeter'):
            c=float(self.x3)*914.4
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Foot' and str(self.x2)=='Inch'):
            c=float(self.x3)*12 
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Foot' and str(self.x2)=='Kilometer'):
            c=float(self.x3)*0.000305
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Foot' and str(self.x2)=='Meter'):
            c=float(self.x3)*0.3048
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Foot' and str(self.x2)=='Centimeter'):
            c=float(self.x3)*30.48
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Foot' and str(self.x2)=='Millimeter'):
            c=float(self.x3)*304.8
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Inch' and str(self.x2)=='Kilometer'):
            c=float(self.x3)*0.000025
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Inch' and str(self.x2)=='Meter'):
            c=float(self.x3)*0.0254
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Inch' and str(self.x2)=='Centimeter'):
            c=float(self.x3)*2.54
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Inch' and str(self.x2)=='Millimeter'):
            c=float(self.x3)*25.4 
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Kilometer' and str(self.x2)=='Meter'):
            c=float(self.x3)*1000 
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Kilometer' and str(self.x2)=='Centimeter'):
            c=float(self.x3)*100000
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Kilometer' and str(self.x2)=='Millimeter'):
            c=float(self.x3)*1000000
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Meter' and str(self.x2)=='Centimeter'):
            c=float(self.x3)*100
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Meter' and str(self.x2)=='Millimeter'):
            c=float(self.x3)*1000
            ze=0
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Centimeter' and str(self.x2)=='Millimeter'):
            c=float(self.x3)*10
            ze=0
            self.toentry.config(text = str(c))
    def Area(self):
        self.w=tk.Toplevel(self)
        self.w.title("Area")
        self.w.geometry("619x350")
        self.load=Image.open("2.jpeg")
        self.render=ImageTk.PhotoImage(self.load)
        self.img=tk.Label(self.w,image=self.render)
        self.img.place(x=0,y=0)
        self.w.resizable(0,0)
        self.Wi=tk.Frame(self.w)
        #self.Wi.grid(row=0,column=1,padx=50,pady=30)
        self.Wi.grid(row=0,column=0,padx=50,pady=30)
        self.text3=tk.Label(self.Wi,
                            text='''Welcome to the Area Convertor''',bg='white',fg="black",font=("Berlin Sans FB Demi",26),borderwidth=3,relief=tk.RAISED)
        self.text3.grid()
        self.n1= tk.StringVar()
        self.n2= tk.StringVar()
        self.fromchoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n1,state='readonly',font=("Comic Sans MS",11))
        self.fromchoosen['values'] = ('Millimeter Square',  
                          'Meter Square', 
                          'Centimeter Square', 
                          'Yard Sqaure', 
                          'Foot Square', 
                          'Inch Square'   
                                 )  
        #self.fromchoosen.grid(row=4,column=0,padx=50,pady=30)
        #self.fromchoosen.grid()
        self.fromchoosen.place(x = 65, y= 120)
        self.fromchoosen.current(0)
        self.tochoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n2,state='readonly',font=("Comic Sans MS",11))
        self.tochoosen['values'] = ('Millimeter Square',  
                          'Meter Square', 
                          'Centimeter Square', 
                          'Yard Sqaure', 
                          'Foot Square', 
                          'Inch Square'
                                 )  
        #self.tochoosen.grid(row=4,column=1,padx=50,pady=30)
        #self.tochoosen.grid()
        self.tochoosen.place(x = 350, y= 120)
        self.tochoosen.current(1)
        self.n3=tk.StringVar()
        self.fromentry= tk.Entry(self.w,fg = 'black', bg = 'white',bd=3,width = 20,textvariable=self.n3,font=("",12))
        #self.fromentry.grid(row=6,column=1,padx=10,pady=10)
        #self.fromentry.grid()
        self.fromentry.place(x = 65, y = 180)
        #self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 25)
        self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 20,relief = tk.RIDGE, justify = tk.CENTER,  borderwidth = 3,font=("",12))
        #self.toentry.grid(row=6,column=3,padx=10,pady=10)
        #self.toentry.grid()
        self.toentry.place(x = 350, y = 180)
        self.convert1=tk.Button(self.w,text="  Convert  ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.check2)
        self.convert1.config(font=('Harlow Solid Italic', 10, 'bold'))
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.convert1.place(x = 405, y = 240)
        self.convert1.place(x = 225, y = 240)
        # this is the same thing
        self.back1=tk.Button(self.w,text="      Back      ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.w.destroy)
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.back1.place(x = 105, y = 240)
        self.back1.place(x = 300, y = 240)
    def check2(self):
        self.x3=self.n3.get()
        try:
            val = int(self.x3)
            self.calc2()
        except ValueError:
            try:
                val = float(self.x3)
                self.calc2()
            except ValueError:
                self.showmesg()
    def calc2(self):
        self.x1=self.fromchoosen.get()
        self.x2=self.tochoosen.get()
        self.x3=self.n3.get()
        if(str(self.x1)=='Millimeter Square' and str(self.x2)=='Centimeter Square'):
            c=float(self.x3)*0.01 
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Millimeter Square' and str(self.x2)=='Meter Square'):
            c=float(self.x3)*0.000001 
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Millimeter Square' and str(self.x2)=='Inch Square'):
            c=float(self.x3)*0.00155 
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Millimeter Square' and str(self.x2)=='Foot Square'):
            c=float(self.x3)*0.000011
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Millimeter Square' and str(self.x2)=='Yard Sqaure'):
            c=float(self.x3)*0.000001
            ze=0  
            self.toentry.config(text = str(c)) 
        elif(str(self.x1)=='Centimeter Square' and str(self.x2)=='Meter Square'):
            c=float(self.x3)*0.0001  
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Centimeter Square' and str(self.x2)=='Inch Square'):  
            c=float(self.x3)*0.155
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Centimeter Square' and str(self.x2)=='Foot Square'):
            c=float(self.x3)*0.001076 
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Centimeter Square' and str(self.x2)=='Yard Sqaure'):
            c=float(self.x3)*0.00012
            ze=0
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Meter Square' and str(self.x2)=='Inch Square'):
            c=float(self.x3)*1550.003
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Meter Square' and str(self.x2)=='Foot Square'):
            c=float(self.x3)*10.76391
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Meter Square' and str(self.x2)=='Yard Sqaure'):
            c=float(self.x3)*1.19599
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Inch Square' and str(self.x2)=='Foot Square'):
            c=float(self.x3)*0.006944 
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Inch Square' and str(self.x2)=='Yard Sqaure'):
            c=float(self.x3)*0.000772
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Foot Square' and str(self.x2)=='Yard Sqaure'):
            c=float(self.x3)*0.111111
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Yard Sqaure' and str(self.x2)=='Foot Square'):
            c=float(self.x3)*9
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Yard Sqaure' and str(self.x2)=='Inch Square'):
            c=float(self.x3)*1296 
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Yard Sqaure' and str(self.x2)=='Meter Square'):
            c=float(self.x3)*0.836127 
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Yard Sqaure' and str(self.x2)=='Centimeter Square'):
            c=float(self.x3)*8361.274 
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Yard Sqaure' and str(self.x2)=='Millimeter Square'):
            c=float(self.x3)*836127
            ze=0
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Foot Square' and str(self.x2)=='Inch Square'):
            c=float(self.x3)*144
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Foot Square' and str(self.x2)=='Meter Square'):
            c=float(self.x3)*0.092903
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Foot Square' and str(self.x2)=='Centimeter Square'):
            c=float(self.x3)*929.0304 
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Foot Square' and str(self.x2)=='Millimeter Square'):
            c=float(self.x3)*92903 
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Inch Square' and str(self.x2)=='Meter Square'):
            c=float(self.x3)*0.000645
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Inch Square' and str(self.x2)=='Centimeter Square'):
            c=float(self.x3)*6.4516
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Inch Square' and str(self.x2)=='Millimeter Square'):
            c=float(self.x3)*645.16
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Meter Square' and str(self.x2)=='Centimeter Square'):
            c=float(self.x3)*10000 
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Meter Square' and str(self.x2)=='Millimeter Square'):
            c=float(self.x3)*1000000 
            ze=0  
            self.toentry.config(text = str(c))
        elif(str(self.x1)=='Centimeter Square' and str(self.x2)=='Millimeter Square'):
            c=float(self.x3)*100
            ze=0  
            self.toentry.config(text = str(c))
    def Mass(self):
        self.w=tk.Toplevel(self)
        self.w.title("Mass")
        self.w.geometry("619x350")
        self.load=Image.open("2.jpeg")
        self.render=ImageTk.PhotoImage(self.load)
        self.img=tk.Label(self.w,image=self.render)
        self.img.place(x=0,y=0)
        self.w.resizable(0,0)
        self.Wi=tk.Frame(self.w)
        #self.Wi.grid(row=0,column=1,padx=50,pady=30)
        self.Wi.grid(row=0,column=0,padx=50,pady=30)
        self.text3=tk.Label(self.Wi,
                            text='''Welcome to the Mass Convertor''',bg='white',fg="black",font=("Berlin Sans FB Demi",26),borderwidth=3,relief=tk.RAISED)
        self.text3.grid()
        self.n1= tk.StringVar()
        self.n2= tk.StringVar()
        self.fromchoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n1,state='readonly',font=("Comic Sans MS",11))
        self.fromchoosen['values'] = ('Gram',  
                          'kilogram', 
                          'Metric', 
                          'Short Ton', 
                          'Long Ton', 
                          'Pound','Ounces'
                                 )  
        #self.fromchoosen.grid(row=4,column=0,padx=50,pady=30)
        #self.fromchoosen.grid()
        self.fromchoosen.place(x = 65, y= 120)
        self.fromchoosen.current(0)
        self.tochoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n2,state='readonly',font=("Comic Sans MS",11))
        self.tochoosen['values'] = ('Gram',  
                          'kilogram', 
                          'Metric', 
                          'Short Ton', 
                          'Long Ton', 
                          'Pound','Ounces'
                                 )  
        #self.tochoosen.grid(row=4,column=1,padx=50,pady=30)
        #self.tochoosen.grid()
        self.tochoosen.place(x = 350, y= 120)
        self.tochoosen.current(1)
        self.n3=tk.StringVar()
        self.fromentry= tk.Entry(self.w,fg = 'black', bg = 'white',bd=3,width = 20,textvariable=self.n3,font=("",12))
        #self.fromentry.grid(row=6,column=1,padx=10,pady=10)
        #self.fromentry.grid()
        self.fromentry.place(x = 65, y = 180)
        #self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 25)
        self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 20,relief = tk.RIDGE, justify = tk.CENTER,  borderwidth = 3,font=("",12))
        #self.toentry.grid(row=6,column=3,padx=10,pady=10)
        #self.toentry.grid()
        self.toentry.place(x = 350, y = 180)
        self.convert1=tk.Button(self.w,text="  Convert  ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.check3)
        self.convert1.config(font=('Harlow Solid Italic', 10, 'bold'))
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.convert1.place(x = 405, y = 240)
        self.convert1.place(x = 225, y = 240)
        # this is the same thing
        self.back1=tk.Button(self.w,text="      Back      ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.w.destroy)
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.back1.place(x = 105, y = 240)
        self.back1.place(x = 300, y = 240)
    def check3(self):
        self.x3=self.n3.get()
        try:
            val = int(self.x3)
            self.calc3()
        except ValueError:
            try:
                val = float(self.x3)
                self.calc3()
            except ValueError:
                self.showmesg()
    def calc3(self):
        self.x1=self.fromchoosen.get()
        self.x2=self.tochoosen.get()
        self.x3=self.n3.get()
        if(self.x1=='Gram'):
            a='g'
        elif(self.x1=='kilogram'):
            a='kg'
        elif(self.x1=='Metric'):
            a='mt'
        elif(self.x1=='Short Ton'):
            a='st'
        elif(self.x1=='Long Ton'):
            a='lt'
        elif(self.x1=='Pound'):
            a='lb'
        elif(self.x1=='Ounces'):
            a='Ounces'
        deep=0
        if(self.x2=='Gram'):
            b='g'
        elif(self.x2=='kilogram'):
            b='kg'
        elif(self.x2=='Metric'):
            b='mt'
        elif(self.x2=='Short Ton'):
            b='st'
        elif(self.x2=='Long Ton'):
            b='lt'
        elif(self.x2=='Pound'):
            b='lb'
        elif(self.x2=='Ounces'):
            b='Ounces'
        deep=0
        if(a=='g' and b=='kg'):
            c=float(self.x3)*0.001
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='g' and b=='mt'):
            c=float(self.x3)*0.000001 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='g' and b=='st'):
            c=float(self.x3)*0.000001
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='g' and b=='lt'):
            c=float(self.x3)*0.000000984
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='g' and b=='lb'):
            c=float(self.x3)*0.002205 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='g' and b=='oz'):
            c=float(self.x3)*0.035273 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='kg' and b=='mt'):  
            c=float(self.x3)*0.001 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='kg' and b=='st'):
            c=float(self.x3)*0.001102 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='kg' and b=='lt'):
            c=float(self.x3)*0.000984 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='kg' and b=='lb'):
            c=float(self.x3)*2.204586
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='kg' and b=='oz'):
            c=float(self.x3)*35.27337
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mt' and b=='st'):
            c=float(self.x3)*1.102293 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mt' and b=='lt'):
            c=float(self.x3)*0.984252 
            ze=0
            self.toentry.config(text = str(c))
        elif(a=='mt' and b=='lb'):
            c=float(self.x3)*2204.586 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mt' and b=='oz'):
            c=float(self.x3)*35273.37
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='st' and b=='lt'):
            c=float(self.x3)*0.892913
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='st' and b=='lt'):
            c=float(self.x3)*2000 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='st' and b=='lt'):
            c=float(self.x3)*32000
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='lt' and b=='lb'):
            c=float(self.x3)*2239.859
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='lt' and b=='oz'):
            c=float(self.x3)*35837.74
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='lb' and b=='oz'):
            c=float(self.x3)*16 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='oz' and b=='lb'):
            c=float(self.x3)*0.0625 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='oz' and b=='lt'):
            c=float(self.x3)*0.000028 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='oz' and b=='st'):
            c=float(self.x3)*0.000031
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='oz' and b=='mt'):
            c=float(self.x3)*0.000028
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='oz' and b=='kg'):
            c=float(self.x3)*0.02835 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='oz' and b=='g'):
            c=float(self.x3)*28
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='lb' and b=='lt'):
            c=float(self.x3)*0.000446
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='lb' and b=='st'):
            c=float(self.x3)*0.0005
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='lb' and b=='mt'):
            c=float(self.x3)*0.000454
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='lb' and b=='kg'):
            c=float(self.x3)*0.4536 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='lb' and b=='g'):
            c=float(self.x3)*453.6
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='lt' and b=='st'):
            c=float(self.x3)*1.119929
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='lt' and b=='mt'):
            c=float(self.x3)*1.016
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='lt' and b=='kg'):
            c=float(self.x3)*1016 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='lt' and b=='g'):
            c=float(self.x3)*1016000
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='st' and b=='mt'):
            c=float(self.x3)*0.9072
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='st' and b=='kg'):
            c=float(self.x3)*907.2
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='st' and b=='g'):
            c=float(self.x3)*907200
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mt' and b=='kg'):
            c=float(self.x3)*1000
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mt' and b=='g'):
            c=float(self.x3)*1000000
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='kg' and b=='g'):
            c=float(self.x3)*1000 
            ze=0  
            self.toentry.config(text = str(c))
    def Volumn(self):
        self.w=tk.Toplevel(self)
        self.w.title("Volumn")
        self.w.geometry("619x350")
        self.load=Image.open("2.jpeg")
        self.render=ImageTk.PhotoImage(self.load)
        self.img=tk.Label(self.w,image=self.render)
        self.img.place(x=0,y=0)
        self.w.resizable(0,0)
        self.Wi=tk.Frame(self.w)
        #self.Wi.grid(row=0,column=1,padx=50,pady=30)
        self.Wi.grid(row=0,column=0,padx=50,pady=30)
        self.text3=tk.Label(self.Wi,
                            text='''Welcome to the Volumn Convertor''',bg='white',fg="black",font=("Berlin Sans FB Demi",26),borderwidth=3,relief=tk.RAISED)
        self.text3.grid()
        self.n1= tk.StringVar()
        self.n2= tk.StringVar()
        self.fromchoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n1,state='readonly',font=("Comic Sans MS",11))
        self.fromchoosen['values'] = ('Centimeter Cube',  
                          'Meter Cube', 
                          'Liter', 
                          'Inch Cube', 
                          'Foot Cube', 
                          'Us Gallon','Imperial Gallon','us barrel'
                                 )  
        #self.fromchoosen.grid(row=4,column=0,padx=50,pady=30)
        #self.fromchoosen.grid()
        self.fromchoosen.place(x = 65, y= 120)
        self.fromchoosen.current(0)
        self.tochoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n2,state='readonly',font=("Comic Sans MS",11))
        self.tochoosen['values'] = ('Centimeter Cube',  
                          'Meter Cube', 
                          'Liter', 
                          'Inch Cube', 
                          'Foot Cube', 
                          'Us Gallon','Imperial Gallon','us barrel'
                                 )  
        #self.tochoosen.grid(row=4,column=1,padx=50,pady=30)
        #self.tochoosen.grid()
        self.tochoosen.place(x = 350, y= 120)
        self.tochoosen.current(1)
        self.n3=tk.StringVar()
        self.fromentry= tk.Entry(self.w,fg = 'black', bg = 'white',bd=3,width = 20,textvariable=self.n3,font=("",12))
        #self.fromentry.grid(row=6,column=1,padx=10,pady=10)
        #self.fromentry.grid()
        self.fromentry.place(x = 65, y = 180)
        #self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 25)
        self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 20,relief = tk.RIDGE, justify = tk.CENTER,  borderwidth = 3,font=("",12))
        #self.toentry.grid(row=6,column=3,padx=10,pady=10)
        #self.toentry.grid()
        self.toentry.place(x = 350, y = 180)
        self.convert1=tk.Button(self.w,text="  Convert  ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.check4)
        self.convert1.config(font=('Harlow Solid Italic', 10, 'bold'))
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.convert1.place(x = 405, y = 240)
        self.convert1.place(x = 225, y = 240)
        # this is the same thing
        self.back1=tk.Button(self.w,text="      Back      ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.w.destroy)
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.back1.place(x = 105, y = 240)
        self.back1.place(x = 300, y = 240)
    def check4(self):
        self.x3=self.n3.get()
        try:
            val = int(self.x3)
            self.calc4()
        except ValueError:
            try:
                val = float(self.x3)
                self.calc4()
            except ValueError:
                self.showmesg()
    def calc4(self):
        self.x1=self.fromchoosen.get()
        self.x2=self.tochoosen.get()
        self.x3=self.n3.get()
        if(self.x1=='Centimeter Cube'):
            a='cmc'
        elif(self.x1=='Meter Cube'):
            a='mc'
        elif(self.x1=='Liter'):
            a='ltr'
        elif(self.x1=='Inch Cube'):
            a='inc'
        elif(self.x1=='Foot Cube'):
            a='ftc'
        elif(self.x1=='Us Gallon'):
            a='usg'
        elif(self.x1=='Imperial Gallon'):
            a='ig'
        elif(self.x1=='us barrel'):
            a='usb'
        deep=0
        if(self.x2=='Centimeter Cube'):
            b='cmc'
        elif(self.x2=='Meter Cube'):
            b='mc'
        elif(self.x2=='Liter'):
            b='ltr'
        elif(self.x2=='Inch Cube'):
            b='inc'
        elif(self.x2=='Foot Cube'):
            b='ftc'
        elif(self.x2=='Us Gallon'):
            b='usg'
        elif(self.x2=='Imperial Gallon'):
            b='ig'
        elif(self.x2=='us barrel'):
            b='usb'
        deep=0
        if(a=='cmc' and b=='mc'):
            c=float(self.x3)*0.000001 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='cmc' and b=='ltr'):
            c=float(self.x3)*0.001 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='cmc' and b=='inc'):
            c=float(self.x3)*0.061024
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='cmc' and b=='ftc'):
            c=float(self.x3)*0.000035 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='cmc' and b=='usg'):
            c=float(self.x3)*0.000264 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='cmc' and b=='ig'):
            c=float(self.x3)*0.00022 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='cmc' and b=='usb'):  
            c=float(self.x3)*0.000006
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mc' and b=='ltr'):
            c=float(self.x3)*1000
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mc' and b=='inc'):
            c=float(self.x3)*61024 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mc' and b=='ftc'):
            c=float(self.x3)*35 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mc' and b=='usg'):
            c=float(self.x3)*264 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mc' and b=='ig'):
            c=float(self.x3)*220
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mc' and b=='usb'):
            c=float(self.x3)*6.29
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ltr' and b=='inc'):
            c=float(self.x3)/61
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ltr' and b=='ftc'):
            c=float(self.x3)/0.035
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ltr' and b=='usg'):
            c=float(self.x3)*0.264201
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ltr' and b=='ig'):
            c=float(self.x3)*0.22 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ltr' and b=='usb'):
            c=float(self.x3)*0.00629 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='inc' and b=='ftc'):
            c=float(self.x3)*0.000579  
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='inc' and b=='usg'):  
            c=float(self.x3)*0.004329 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='inc' and b=='ig'):
            c=float(self.x3)*0.003605 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='inc' and b=='usb'):
            c=float(self.x3)*0.000103 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftc' and b=='usg'):
            c=float(self.x3)*7.481333 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftc' and b=='ig'):
            c=float(self.x3)*6.229712
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftc' and b=='usg'):
            c=float(self.x3)*0.178127
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='usg' and b=='ig'):
            c=float(self.x3)*0.832701
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='usg' and b=='usb'):
            c=float(self.x3)*0.02381
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ig' and b=='usb'):
            c=float(self.x3)*0.028593
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='usb' and b=='ig'):
            c=float(self.x3)*35
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='usb' and b=='usg'):
            c=float(self.x3)*42
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='usb' and b=='ftc'):
            c=float(self.x3)*6
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='usb' and b=='inc'):
            c=float(self.x3)*9701
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='usb' and b=='ltr'):
            c=float(self.x3)*159
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='usb' and b=='mc'):
            c=float(self.x3)*0.15897 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='usb' and b=='cmc'):
            c=float(self.x3)*158970 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ig' and b=='usg'):
            c=float(self.x3)*1.20  
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ig' and b=='ftc'):
            c=float(self.x3)*0.16 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ig' and b=='inc'):
            c=float(self.x3)*277
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ig' and b=='ltr'):
            c=float(self.x3)*4.55 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ig' and b=='mc'):
            c=float(self.x3)*0.004545
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ig' and b=='cmc'):
            c=float(self.x3)*4545 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='usg' and b=='ftc'):
            c=float(self.x3)*0.13 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='usg' and b=='inc'):
            c=float(self.x3)*231 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='usg' and b=='ltr'):
            c=float(self.x3)*3.79 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='usg' and b=='mc'):
            c=float(self.x3)*0.003785 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='usg' and b=='cmc'):
            c=float(self.x3)*3785
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftc' and b=='inc'):
            c=float(self.x3)*1728 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftc' and b=='ltr'):
            c=float(self.x3)*28.31685 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftc' and b=='mc'):
            c=float(self.x3)*0.028317
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftc' and b=='cmc'):
            c=float(self.x3)*28317
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='inc' and b=='ltr'):
            c=float(self.x3)*0.016387
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='inc' and b=='mc'):
            c=float(self.x3)*0.000016 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='inc' and b=='cmc'):
            c=float(self.x3)*16.4
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ltr' and b=='mc'):
            c=float(self.x3)*0.001 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ltr' and b=='cmc'):
            c=float(self.x3)*1000
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mc' and b=='cmc'):
            c=float(self.x3)*1000000
            ze=0  
            self.toentry.config(text = str(c))
    def Density(self):
        self.w=tk.Toplevel(self)
        self.w.title("Density")
        self.w.geometry("619x350")
        self.load=Image.open("2.jpeg")
        self.render=ImageTk.PhotoImage(self.load)
        self.img=tk.Label(self.w,image=self.render)
        self.img.place(x=0,y=0)
        self.w.resizable(0,0)
        self.Wi=tk.Frame(self.w)
        #self.Wi.grid(row=0,column=1,padx=50,pady=30)
        self.Wi.grid(row=0,column=0,padx=50,pady=30)
        self.text3=tk.Label(self.Wi,
                            text='''Welcome to the Density Convertor''',bg='white',fg="black",font=("Berlin Sans FB Demi",26),borderwidth=3,relief=tk.RAISED)
        self.text3.grid()
        self.n1= tk.StringVar()
        self.n2= tk.StringVar()
        self.fromchoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n1,state='readonly',font=("Comic Sans MS",11))
        self.fromchoosen['values'] = ('Gram/Milli Liter',  
                          'Kilogram/Meter Cube', 
                          'Pound/Foot Cube', 
                          'Pound/Inch Cube' )  
        #self.fromchoosen.grid(row=4,column=0,padx=50,pady=30)
        #self.fromchoosen.grid()
        self.fromchoosen.place(x = 65, y= 120)
        self.fromchoosen.current(0)
        self.tochoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n2,state='readonly',font=("Comic Sans MS",11))
        self.tochoosen['values'] = ('Gram/Milli Liter',  
                          'Kilogram/Meter Cube', 
                          'Pound/Foot Cube', 
                          'Pound/Inch Cube' ) 
        #self.tochoosen.grid(row=4,column=1,padx=50,pady=30)
        #self.tochoosen.grid()
        self.tochoosen.place(x = 350, y= 120)
        self.tochoosen.current(1)
        self.n3=tk.StringVar()
        self.fromentry= tk.Entry(self.w,fg = 'black', bg = 'white',bd=3,width = 20,textvariable=self.n3,font=("",12))
        #self.fromentry.grid(row=6,column=1,padx=10,pady=10)
        #self.fromentry.grid()
        self.fromentry.place(x = 65, y = 180)
        #self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 25)
        self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 20,relief = tk.RIDGE, justify = tk.CENTER,  borderwidth = 3,font=("",12))
        #self.toentry.grid(row=6,column=3,padx=10,pady=10)
        #self.toentry.grid()
        self.toentry.place(x = 350, y = 180)
        self.convert1=tk.Button(self.w,text="  Convert  ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.check5)
        self.convert1.config(font=('Harlow Solid Italic', 10, 'bold'))
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.convert1.place(x = 405, y = 240)
        self.convert1.place(x = 225, y = 240)
        # this is the same thing
        self.back1=tk.Button(self.w,text="      Back      ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.w.destroy)
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.back1.place(x = 105, y = 240)
        self.back1.place(x = 300, y = 240)
    def check5(self):
        self.x3=self.n3.get()
        try:
            val = int(self.x3)
            self.calc5()
        except ValueError:
            try:
                val = float(self.x3)
                self.calc5()
            except ValueError:
                self.showmesg()
    def calc5(self):
        self.x1=self.fromchoosen.get()
        self.x2=self.tochoosen.get()
        self.x3=self.n3.get()
        if(self.x1=='Gram/Milli Liter'):
            a=1
        elif(self.x1=='Kilogram/Meter Cube'):
            a=2
        elif(self.x1=='Pound/Foot Cube'):
            a=3
        elif(self.x1=='Pound/Inch Cube'):
            a=4
        deep=0
        if(self.x1=='Gram/Milli Liter'):
            b=1
        elif(self.x1=='Kilogram/Meter Cube'):
            b=2
        elif(self.x1=='Pound/Foot Cube'):
            b=3
        elif(self.x1=='Pound/Inch Cube'):
            b=4
        deep=0
        if(a==1 and b==2):
            c=float(self.x3)*1000 
            ze=0 
            self.toentry.config(text = str(c))
        elif(a==1 and b==3):
            c=float(self.x3)*62.42197
            ze=0 
            self.toentry.config(text = str(c))
        elif(a==1 and b==4):
            c=float(self.x3)*0.036127
            ze=0 
            self.toentry.config(text = str(c))
        elif(a==2 and b==3):
            c=float(self.x3)*0.062422 
            ze=0 
            self.toentry.config(text = str(c))
        elif(a==2 and b==4):
            c=float(self.x3)*0.000036
            ze=0 
            self.toentry.config(text = str(c))
        elif(a==3 and b==4):
            c=float(self.x3)*0.000579
            ze=0 
            self.toentry.config(text = str(c))
        elif(a==4 and b==3):
            c=float(self.x3)*1727.84 
            ze=0 
            self.toentry.config(text = str(c))
        elif(a==4 and b==2):
            c=float(self.x3)*27680 
            ze=0 
            self.toentry.config(text = str(c))
        elif(a==4 and b==1):
            c=float(self.x3)*27.68
            ze=0 
            self.toentry.config(text = str(c))
        elif(a==3 and b==2):
            c=float(self.x3)*16.02
            ze=0 
            self.toentry.config(text = str(c))
        elif(a==3 and b==1):
            c=float(self.x3)*0.01602 
            ze=0 
            self.toentry.config(text = str(c))
        elif(a==2 and b==1):
            c=float(self.x3)*0.001
            ze=0 
            self.toentry.config(text = str(c))
    def Speed(self):
        self.w=tk.Toplevel(self)
        self.w.title("Speed")
        self.w.geometry("619x350")
        self.load=Image.open("2.jpeg")
        self.render=ImageTk.PhotoImage(self.load)
        self.img=tk.Label(self.w,image=self.render)
        self.img.place(x=0,y=0)
        self.w.resizable(0,0)
        self.Wi=tk.Frame(self.w)
        #self.Wi.grid(row=0,column=1,padx=50,pady=30)
        self.Wi.grid(row=0,column=0,padx=50,pady=30)
        self.text3=tk.Label(self.Wi,
                            text='''Welcome to the Speed Convertor''',bg='white',fg="black",font=("Berlin Sans FB Demi",26),borderwidth=3,relief=tk.RAISED)
        self.text3.grid()
        self.n1= tk.StringVar()
        self.n2= tk.StringVar()
        self.fromchoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n1,state='readonly',font=("Comic Sans MS",11))
        self.fromchoosen['values'] = ('Meter Per Second',  
                          'Meter Per Minute', 
                          'Kilometer Per Hour', 
                          'Foot Per Second','Miles Per Hour', 
                          'Foot Per Minute',
                                      )  
        #self.fromchoosen.grid(row=4,column=0,padx=50,pady=30)
        #self.fromchoosen.grid()
        self.fromchoosen.place(x = 65, y= 120)
        self.fromchoosen.current(0)
        self.tochoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n2,state='readonly',font=("Comic Sans MS",11))
        self.tochoosen['values'] = ('Meter Per Second',  
                          'Meter Per Minute', 
                          'Kilometer Per Hour', 
                          'Foot Per Second','Miles Per Hour', 
                          'Foot Per Minute',
                                      ) 
        #self.tochoosen.grid(row=4,column=1,padx=50,pady=30)
        #self.tochoosen.grid()
        self.tochoosen.place(x = 350, y= 120)
        self.tochoosen.current(1)
        self.n3=tk.StringVar()
        self.fromentry= tk.Entry(self.w,fg = 'black', bg = 'white',bd=3,width = 20,textvariable=self.n3,font=("",12))
        #self.fromentry.grid(row=6,column=1,padx=10,pady=10)
        #self.fromentry.grid()
        self.fromentry.place(x = 65, y = 180)
        #self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 25)
        self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 20,relief = tk.RIDGE, justify = tk.CENTER,  borderwidth = 3,font=("",12))
        #self.toentry.grid(row=6,column=3,padx=10,pady=10)
        #self.toentry.grid()
        self.toentry.place(x = 350, y = 180)
        self.convert1=tk.Button(self.w,text="  Convert  ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.check6)
        self.convert1.config(font=('Harlow Solid Italic', 10, 'bold'))
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.convert1.place(x = 405, y = 240)
        self.convert1.place(x = 225, y = 240)
        # this is the same thing
        self.back1=tk.Button(self.w,text="      Back      ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.w.destroy)
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.back1.place(x = 105, y = 240)
        self.back1.place(x = 300, y = 240)
    def check6(self):
        self.x3=self.n3.get()
        try:
            val = int(self.x3)
            self.calc6()
        except ValueError:
            try:
                val = float(self.x3)
                self.calc6()
            except ValueError:
                self.showmesg()
    def calc6(self):
        self.x1=self.fromchoosen.get()
        self.x2=self.tochoosen.get()
        self.x3=self.n3.get()
        if(self.x1=='Meter Per Second '):
            a='mps'
        elif(self.x1=='Meter Per Minute'):
            a='mpm'
        elif(self.x1=='Kilometer Per Hour'):
            a='kmph'
        elif(self.x1=='Foot Per Second'):
            a='ftps'
        elif(self.x1=='Foot Per Minute'):
            a='ftpm'
        elif(self.x1=='Miles Per Hour'):
            a='miph'
        deep=0
        if(self.x2=='Meter Per Second '):
            b='mps'
        elif(self.x2=='Meter Per Minute'):
            b='mpm'
        elif(self.x2=='Kilometer Per Hour'):
            b='kmph'
        elif(self.x2=='Foot Per Second'):
            b='ftps'
        elif(self.x2=='Foot Per Minute'):
            b='ftpm'
        elif(self.x2=='Miles Per Hour'):
            b='miph'
        deep=0
        if(a=='mps' and b=='mpm'):
            c=float(self.x3)*59.988
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mps' and b=='kmph'):
            c=float(self.x3)*3.599712  
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mps' and b=='ftps'):
            c=float(self.x3)*3.28084 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mps' and b=='ftpm'):
            c=float(self.x3)*196.8504  
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mps' and b=='miph'):
            c=float(self.x3)*2.237136 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mpm' and b=='kmph'):
            c=float(self.x3)*0.060007  
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mpm' and b=='ftps'):  
            c=float(self.x3)*0.054692
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mpm' and b=='ftpm'):
            c=float(self.x3)*3.281496
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mpm' and b=='miph'):
            c=float(self.x3)*0.037293 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='kmph' and b=='ftps'):
            c=float(self.x3)*0.911417 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='kmph' and b=='ftpm'):
            c=float(self.x3)*54.68504  
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='kmph' and b=='miph'):
            c=float(self.x3)*0.621477
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftps' and b=='ftpm'):
            c=float(self.x3)*60 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftps' and b=='miph'):
            c=float(self.x3)*0.681879
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftpm' and b=='miph'):
            c=float(self.x3)*0.011365
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='miph' and b=='ftpm'):
            c=float(self.x3)*87.99213 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='miph' and b=='ftps'):
            c=float(self.x3)*1.466535 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='miph' and b=='kmph'):
            c=float(self.x3)*1.609071  
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='miph' and b=='mpm'):
            c=float(self.x3)*26.81464   
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='miph' and b=='mps'):  
            c=float(self.x3)*0.447 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftpm' and b=='ftps'):
            c=float(self.x3)*0.016667  
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftpm' and b=='kmph'):
            c=float(self.x3)*0.018287 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftpm' and b=='mpm'):
            c=float(self.x3)*0.304739 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftpm' and b=='mps'):
            c=float(self.x3)*0.00508
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftps' and b=='kmph'):
            c=float(self.x3)*1.097192
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftps' and b=='mpm'):
            c=float(self.x3)*18.28434
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='ftps' and b=='mps'):
            c=float(self.x3)*0.3048 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='kmph' and b=='mpm'):
            c=float(self.x3)*16.66467
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='kmph' and b=='mps'):
            c=float(self.x3)*0.2778
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mpm' and b=='mps'):
            c=float(self.x3)*0.01667
            ze=0  
            self.toentry.config(text = str(c))
    def Temperature(self):
        self.w=tk.Toplevel(self)
        self.w.title("Temperature")
        self.w.geometry("800x350")
        self.load=Image.open("2.jpeg")
        self.render=ImageTk.PhotoImage(self.load)
        self.img=tk.Label(self.w,image=self.render)
        self.img.place(x=0,y=0)
        self.w.resizable(0,0)
        self.Wi=tk.Frame(self.w)
        #self.Wi.grid(row=0,column=1,padx=50,pady=30)
        self.Wi.grid(row=0,column=0,padx=50,pady=30)
        self.text3=tk.Label(self.Wi,
                            text='''Welcome to the Temperature Convertor''',bg='white',fg="black",font=("Berlin Sans FB Demi",26),borderwidth=3,relief=tk.RAISED)
        self.text3.grid()
        self.n1= tk.StringVar()
        self.n2= tk.StringVar()
        self.fromchoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n1,state='readonly',font=("Comic Sans MS",11))
        self.fromchoosen['values'] = ('Degree Celsius',  
                          'Degree Kelvin', 
                          'Degree Fahrenheit'
                                      )  
        #self.fromchoosen.grid(row=4,column=0,padx=50,pady=30)
        #self.fromchoosen.grid()
        self.fromchoosen.place(x = 65, y= 120)
        self.fromchoosen.current(0)
        self.tochoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n2,state='readonly',font=("Comic Sans MS",11))
        self.tochoosen['values'] = ('Degree Celsius',  
                          'Degree Kelvin', 
                          'Degree Fahrenheit'
                                      )
        #self.tochoosen.grid(row=4,column=1,padx=50,pady=30)
        #self.tochoosen.grid()
        self.tochoosen.place(x = 350, y= 120)
        self.tochoosen.current(1)
        self.n3=tk.StringVar()
        self.fromentry= tk.Entry(self.w,fg = 'black', bg = 'white',bd=3,width = 20,textvariable=self.n3,font=("",12))
        #self.fromentry.grid(row=6,column=1,padx=10,pady=10)
        #self.fromentry.grid()
        self.fromentry.place(x = 65, y = 180)
        #self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 25)
        self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 20,relief = tk.RIDGE, justify = tk.CENTER,  borderwidth = 3,font=("",12))
        #self.toentry.grid(row=6,column=3,padx=10,pady=10)
        #self.toentry.grid()
        self.toentry.place(x = 350, y = 180)
        self.convert1=tk.Button(self.w,text="  Convert  ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.check7)
        self.convert1.config(font=('Harlow Solid Italic', 10, 'bold'))
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.convert1.place(x = 405, y = 240)
        self.convert1.place(x = 225, y = 240)
        # this is the same thing
        self.back1=tk.Button(self.w,text="      Back      ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.w.destroy)
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.back1.place(x = 105, y = 240)
        self.back1.place(x = 300, y = 240)
    def check7(self):
        self.x3=self.n3.get()
        try:
            val = int(self.x3)
            self.calc7()
        except ValueError:
            try:
                val = float(self.x3)
                self.calc7()
            except ValueError:
                self.showmesg()
    def calc7(self):
        self.x1=self.fromchoosen.get()
        self.x2=self.tochoosen.get()
        self.x3=self.n3.get()
        if(self.x1=='Degree Celsius'):
            a='c'
        elif(self.x1=='Degree Kelvin'):
            a='k'
        elif(self.x1=='Degree Fahrenheit'):
            a='f'
        deep=0
        if(self.x2=='Degree Celsius'):
            b='c'
        elif(self.x2=='Degree Kelvin'):
            b='k'
        elif(self.x2=='Degree Fahrenheit'):
            b='f'
        deep=0
        if(a=='c' and b=='f'):
            c=(float(self.x3)*9/5)+32 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='k' and b=='f'):
            c=(float(self.x3)-273.15)*9/5+32 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='f' and b=='c'):
            c=(float(self.x3)-32)*5/9
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='k' and b=='c'):
            c=float(self.x3)-273.15 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='c' and b=='k'):
            c=float(self.x3)+273.15
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='f' and b=='k'):
            c=(float(self.x3)-32)*5/9+273.15
            ze=0  
            self.toentry.config(text = str(c))
    def PlaneAngle(self):
        self.w=tk.Toplevel(self)
        self.w.title("PlaneAngle")
        self.w.geometry("712x350")
        self.load=Image.open("2.jpeg")
        self.render=ImageTk.PhotoImage(self.load)
        self.img=tk.Label(self.w,image=self.render)
        self.img.place(x=0,y=0)
        self.w.resizable(0,0)
        self.Wi=tk.Frame(self.w)
        #self.Wi.grid(row=0,column=1,padx=50,pady=30)
        self.Wi.grid(row=0,column=0,padx=50,pady=30)
        self.text3=tk.Label(self.Wi,
                            text='''Welcome to the Plane Angle Convertor''',bg='white',fg="black",font=("Berlin Sans FB Demi",26),borderwidth=3,relief=tk.RAISED)
        self.text3.grid()
        self.n1= tk.StringVar()
        self.n2= tk.StringVar()
        self.fromchoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n1,state='readonly',font=("Comic Sans MS",11))
        self.fromchoosen['values'] = ('Degree',  
                          'Gradian', 
                          'Radian', 
                          'Milliradian', 
                          'Second Of Arce','Minute Of Arc'
                                      )  
        #self.fromchoosen.grid(row=4,column=0,padx=50,pady=30)
        #self.fromchoosen.grid()
        self.fromchoosen.place(x = 125, y= 120)
        self.fromchoosen.current(0)
        self.tochoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n2,state='readonly',font=("Comic Sans MS",11))
        self.tochoosen['values'] = ('Degree',  
                          'Gradian', 
                          'Radian', 
                          'Milliradian', 
                          'Second Of Arce','Minute Of Arc'
                                      ) 
        #self.tochoosen.grid(row=4,column=1,padx=50,pady=30)
        #self.tochoosen.grid()
        self.tochoosen.place(x = 410, y= 120)
        self.tochoosen.current(1)
        self.n3=tk.StringVar()
        self.fromentry= tk.Entry(self.w,fg = 'black', bg = 'white',bd=3,width = 20,textvariable=self.n3,font=("",12))
        #self.fromentry.grid(row=6,column=1,padx=10,pady=10)
        #self.fromentry.grid()
        self.fromentry.place(x = 125, y = 180)
        #self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 25)
        self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 20,relief = tk.RIDGE, justify = tk.CENTER,  borderwidth = 3,font=("",12))
        #self.toentry.grid(row=6,column=3,padx=10,pady=10)
        #self.toentry.grid()
        self.toentry.place(x = 410, y = 180)
        self.convert1=tk.Button(self.w,text="  Convert  ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.check8)
        self.convert1.config(font=('Harlow Solid Italic', 10, 'bold'))
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.convert1.place(x = 405, y = 240)
        self.convert1.place(x = 285, y = 240)
        # this is the same thing
        self.back1=tk.Button(self.w,text="      Back      ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.w.destroy)
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.back1.place(x = 105, y = 240)
        self.back1.place(x = 360, y = 240)
    def check8(self):
        self.x3=self.n3.get()
        try:
            val = int(self.x3)
            self.calc8()
        except ValueError:
            try:
                val = float(self.x3)
                self.calc8()
            except ValueError:
                self.showmesg()
    def calc8(self):
        self.x1=self.fromchoosen.get()
        self.x2=self.tochoosen.get()
        self.x3=self.n3.get()
        if(self.x1=='Degree'):
            a='d'
        elif(self.x1=='Gradian'):
            a='g'
        elif(self.x1=='Milliradian'):
            a='mr'
        elif(self.x1=='Minute Of Arc'):
            a='moa'
        elif(self.x1=='Radian'):
            a='r'
        elif(self.x1=='Second Of Arc'):
            a='soa'
        deep=0
        if(self.x2=='Degree'):
            b='d'
        elif(self.x2=='Gradian'):
            b='g'
        elif(self.x2=='Milliradian'):
            b='mr'
        elif(self.x2=='Minute Of Arc'):
            b='moa'
        elif(self.x2=='Radian'):
            b='r'
        elif(self.x2=='Second Of Arc'):
            b='soa'
        deep=0
        if(a=='d' and b=='g'):
            c=float(self.x3)*200/180 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='d' and b=='mr'):
            c=float(self.x3)*(1000*3.14)/180 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='d' and b=='moa'):
            c=float(self.x3)*60
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='d' and b=='r'):
            c=float(self.x3)*3.14/180 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='d' and b=='soa'):
            c=float(self.x3)*3600
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='g' and b=='mr'):
            c=float(self.x3)*(1000*3.14)/200
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='g' and b=='moa'):  
            c=float(self.x3)*54
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='g' and b=='r'):
            c=float(self.x3)*3.14/200
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='g' and b=='soa'):
            c=float(self.x3)*3240 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mr' and b=='moa'):
            c=float(self.x3)*(60*180)/(1000*3.14) 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mr' and b=='r'):
            c=float(self.x3)/1000 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mr' and b=='soa'):
            c=float(self.x3)*(3600*180)/(1000*3.14)
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='moa' and b=='r'):
            c=float(self.x3)*3.14/(60*180)
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='moa' and b=='soa'):
            c=float(self.x3)*60
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='r' and b=='soa'):
            c=float(self.x3)*(3600*180)*3.14
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='soa' and b=='r'):
            c=float(self.x3)*3.14/(180/3600)
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='soa' and b=='moa'):
            c=float(self.x3)/60 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='soa' and b=='mr'):
            c=float(self.x3)*100*3.14/(180*3600)
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='soa' and b=='g'):
            c=float(self.x3)/3240  
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='soa' and b=='d'):  
            c=float(self.x3)/3600
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='r' and b=='moa'):
            c=float(self.x3)*(60*180)/3.14 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='r' and b=='mr'):
            c=float(self.x3)*1000
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='r' and b=='g'):
            c=float(self.x3)*200/3.14 
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='r' and b=='d'):
            c=float(self.x3)*180/3.14
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='moa' and b=='mr'):
            c=float(self.x3)*1000*3.14/(60*180)
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='moa' and b=='g'):
            c=float(self.x3)/54
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='moa' and b=='d'):
            c=float(self.x3)/60
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mr' and b=='g'):
            c=float(self.x3)*200/(1000*3.14)
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='mr' and b=='d'):
            c=float(self.x3)*180/(1000*3.14)
            ze=0  
            self.toentry.config(text = str(c))
        elif(a=='g' and b=='d'):
            c=float(self.x3)*180/200
            ze=0  
            self.toentry.config(text = str(c))
    def Torque(self):
        self.w=tk.Toplevel(self)
        self.w.title("Torque")
        self.w.geometry("619x350")
        self.load=Image.open("2.jpeg")
        self.render=ImageTk.PhotoImage(self.load)
        self.img=tk.Label(self.w,image=self.render)
        self.img.place(x=0,y=0)
        self.w.resizable(0,0)
        self.Wi=tk.Frame(self.w)
        #self.Wi.grid(row=0,column=1,padx=50,pady=30)
        self.Wi.grid(row=0,column=0,padx=50,pady=30)
        self.text3=tk.Label(self.Wi,
                            text='''Welcome to the Torque Convertor''',bg='white',fg="black",font=("Berlin Sans FB Demi",26),borderwidth=3,relief=tk.RAISED)
        self.text3.grid()
        self.n1= tk.StringVar()
        self.n2= tk.StringVar()
        self.fromchoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n1,state='readonly',font=("Comic Sans MS",11))
        self.fromchoosen['values'] = ('Newton Meter',  
                          'Kilogram Force Meter', 
                          'Foot Pound', 
                          'Inch Pound'
                                      )  
        #self.fromchoosen.grid(row=4,column=0,padx=50,pady=30)
        #self.fromchoosen.grid()
        self.fromchoosen.place(x = 65, y= 120)
        self.fromchoosen.current(0)
        self.tochoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n2,state='readonly',font=("Comic Sans MS",11))
        self.tochoosen['values'] = ('Newton Meter',  
                          'Kilogram Force Meter', 
                          'Foot Pound', 
                          'Inch Pound'
                                      ) 
        #self.tochoosen.grid(row=4,column=1,padx=50,pady=30)
        #self.tochoosen.grid()
        self.tochoosen.place(x = 350, y= 120)
        self.tochoosen.current(1)
        self.n3=tk.StringVar()
        self.fromentry= tk.Entry(self.w,fg = 'black', bg = 'white',bd=3,width = 20,textvariable=self.n3,font=("",12))
        #self.fromentry.grid(row=6,column=1,padx=10,pady=10)
        #self.fromentry.grid()
        self.fromentry.place(x = 65, y = 180)
        #self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 25)
        self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 20,relief = tk.RIDGE, justify = tk.CENTER,  borderwidth = 3,font=("",12))
        #self.toentry.grid(row=6,column=3,padx=10,pady=10)
        #self.toentry.grid()
        self.toentry.place(x = 350, y = 180)
        self.convert1=tk.Button(self.w,text="  Convert  ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.check9)
        self.convert1.config(font=('Harlow Solid Italic', 10, 'bold'))
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.convert1.place(x = 405, y = 240)
        self.convert1.place(x = 225, y = 240)
        # this is the same thing
        self.back1=tk.Button(self.w,text="      Back      ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.w.destroy)
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.back1.place(x = 105, y = 240)
        self.back1.place(x = 300, y = 240)
    def check9(self):
        self.x3=self.n3.get()
        try:
            val = int(self.x3)
            self.calc9()
        except ValueError:
            try:
                val = float(self.x3)
                self.calc9()
            except ValueError:
                self.showmesg()
    def calc9(self):
        self.x1=self.fromchoosen.get()
        self.x2=self.tochoosen.get()
        self.x3=self.n3.get()
        if(self.x1=='Newton Meter'):
            a='nm'
        elif(self.x1=='Kilogram Force Meter'):
            a='kgfm'
        elif(self.x1=='Foot Pound'):
            a='ftlb'
        elif(self.x1=='Inch Pound'):
            a='inlb'
        deep=0
        if(self.x2=='Newton Meter'):
            b='nm'
        elif(self.x2=='Kilogram Force Meter'):
            b='kgfm'
        elif(self.x2=='Foot Pound'):
            b='ftlb'
        elif(self.x2=='Inch Pound'):
            b='inlb'
    def Currency(self):
        self.w=tk.Toplevel(self)
        self.w.title("Currency")
        self.w.geometry("800x350")
        self.load=Image.open("2.jpeg")
        self.render=ImageTk.PhotoImage(self.load)
        self.img=tk.Label(self.w,image=self.render)
        self.img.place(x=0,y=0)
        self.w.resizable(0,0)
        self.Wi=tk.Frame(self.w)
        #self.Wi.grid(row=0,column=1,padx=50,pady=30)
        self.Wi.grid(row=0,column=0,padx=50,pady=30)
        self.text3=tk.Label(self.Wi,
                            text='''Welcome to the Real Time Currency Convertor''',bg='white',fg="black",font=("Berlin Sans FB Demi",26),borderwidth=3,relief=tk.RAISED)
        self.text3.grid()
        self.n1= tk.StringVar()
        self.n2= tk.StringVar()
        self.fromchoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n1,state='readonly',font=("Comic Sans MS",11))
        self.fromchoosen['values'] = ('Indian Rupee','US Dollar','UAE Dirham','Argentine Peso'
                                        ,'Australian Dollar','Bulgarian Lev','Brazilian Real',
                                         'Bahamian Dollar','Canadian Dollar','Swiss Franc',
                                         'Chilean Peso','Chinese Yuan','Colombian Peso','Czech Koruna',
                                         'Danish Krone','Dominican Peso','Egyptian Pound','Euro','Fiji Dollar',
                                         'Pound Sterling','Quetzal','Hong Kong Dollar','Croatian Kuna','Hungarian Forint'
                                         ,'Indonesian Rupiah','New Israeli Shekel','Iceland Krona','Japanese Yen','South Korean Won'
                                         ,'Kazakhstani Tenge','Maldivian Rufiyaa','Mexican Peso','Malaysian Ringgit','Norwegian Krone'
                                         ,'New Zealand Dollar','Panamanian Balboa','Peru Nuevo Sol','Philippine Peso','Poland zloty'
                                         ,'Paraguayan Guarani','Romanian Leu','Russian Ruble','Saudi Riyal','Swedish Krona','Singapore Dollar'
                                         ,'Thai Baht','Turkish Lira','Taiwan Dollar','Ukrainian hryvnia','Peso Uruguayo','South African Rand')  
        #self.fromchoosen.grid(row=4,column=0,padx=50,pady=30)
        #self.fromchoosen.grid()
        self.fromchoosen.place(x = 65, y= 120)
        self.fromchoosen.current(0)
        self.tochoosen = ttk.Combobox(self.w,width = 18,textvariable=self.n2,state='readonly',font=("Comic Sans MS",11))
        self.tochoosen['values'] = ('Indian Rupee','US Dollar','UAE Dirham','Argentine Peso'
                                    ,'Australian Dollar','Bulgarian Lev','Brazilian Real',
                                     'Bahamian Dollar','Canadian Dollar','Swiss Franc',
                                     'Chilean Peso','Chinese Yuan','Colombian Peso','Czech Koruna',
                                     'Danish Krone','Dominican Peso','Egyptian Pound','Euro','Fiji Dollar',
                                     'Pound Sterling','Quetzal','Hong Kong Dollar','Croatian Kuna','Hungarian Forint'
                                     ,'Indonesian Rupiah','New Israeli Shekel','Iceland Krona','Japanese Yen','South Korean Won'
                                     ,'Kazakhstani Tenge','Maldivian Rufiyaa','Mexican Peso','Malaysian Ringgit','Norwegian Krone'
                                     ,'New Zealand Dollar','Panamanian Balboa','Peru Nuevo Sol','Philippine Peso','Poland zloty'
                                     ,'Paraguayan Guarani','Romanian Leu','Russian Ruble','Saudi Riyal','Swedish Krona','Singapore Dollar'
                                     ,'Thai Baht','Turkish Lira','Taiwan Dollar','Ukrainian hryvnia','Peso Uruguayo','South African Rand') 
        #self.tochoosen.grid(row=4,column=1,padx=50,pady=30)
        #self.tochoosen.grid()
        self.tochoosen.place(x = 350, y= 120)
        self.tochoosen.current(1)
        self.n3=tk.StringVar()
        self.fromentry= tk.Entry(self.w,fg = 'black', bg = 'white',bd=3,width = 20,textvariable=self.n3,font=("",12))
        #self.fromentry.grid(row=6,column=1,padx=10,pady=10)
        #self.fromentry.grid()
        self.fromentry.place(x = 65, y = 180)
        #self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 25)
        self.toentry= tk.Label(self.w, text = '',fg = 'black', bg = 'white',width = 20,relief = tk.RIDGE, justify = tk.CENTER,  borderwidth = 3,font=("",12))
        #self.toentry.grid(row=6,column=3,padx=10,pady=10)
        #self.toentry.grid()
        self.toentry.place(x = 350, y = 180)
        self.convert1=tk.Button(self.w,text="  Convert  ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.check10)
        self.convert1.config(font=('Harlow Solid Italic', 10, 'bold'))
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.convert1.place(x = 405, y = 240)
        self.convert1.place(x = 225, y = 240)
        # this is the same thing
        self.back1=tk.Button(self.w,text="      Back      ",font=("Harlow Solid Italic",10),fg = 'white', bg = 'blue',command=self.w.destroy)
        #self.convert1.grid(row=16,column=2,padx=10,pady=10)
        #self.back1.place(x = 105, y = 240)
        self.back1.place(x = 300, y = 240)
    def check10(self):
        self.x3=self.n3.get()
        try:
            val = int(self.x3)
            self.calc10()
        except ValueError:
            try:
                val = float(self.x3)
                self.calc10()
            except ValueError:
                self.showmesg()
    def calc10(self):
        self.x1=self.fromchoosen.get()
        self.x2=self.tochoosen.get()
        self.x3=self.n3.get()
        p= ('Indian Rupee','US Dollar','UAE Dirham','Argentine Peso'
                ,'Australian Dollar','Bulgarian Lev','Brazilian Real',
                 'Bahamian Dollar','Canadian Dollar','Swiss Franc',
                 'Chilean Peso','Chinese Yuan','Colombian Peso','Czech Koruna',
                 'Danish Krone','Dominican Peso','Egyptian Pound','Euro','Fiji Dollar',
                 'Pound Sterling','Quetzal','Hong Kong Dollar','Croatian Kuna','Hungarian Forint'
                 ,'Indonesian Rupiah','New Israeli Shekel','Iceland Krona','Japanese Yen','South Korean Won'
                 ,'Kazakhstani Tenge','Maldivian Rufiyaa','Mexican Peso','Malaysian Ringgit','Norwegian Krone'
                 ,'New Zealand Dollar','Panamanian Balboa','Peru Nuevo Sol','Philippine Peso','Poland zloty'
                 ,'Paraguayan Guarani','Romanian Leu','Russian Ruble','Saudi Riyal','Swedish Krona','Singapore Dollar'
                 ,'Thai Baht','Turkish Lira','Taiwan Dollar','Ukrainian hryvnia','Peso Uruguayo','South African Rand')
        if(self.x1==p[0]):
            a='INR'
        elif(self.x1==p[1]):
            a='USD'
        elif(self.x1==p[2]):
            a='AED'
        elif(self.x1==p[3]):
            a='ARS'
        elif(self.x1==p[4]):
            a='AUD'
        elif(self.x1==p[5]):
            a='BGN'
        elif(self.x1==p[6]):
            a='BRL'
        elif(self.x1==p[7]):
            a='BSD'
        elif(self.x1==p[8]):
            a='CAD'
        elif(self.x1==p[9]):
            a='CHF'
        elif(self.x1==p[10]):
            a='CLP'
        elif(self.x1==p[11]):
            a='CNY'
        elif(self.x1==p[12]):
            a='COP'
        elif(self.x1==p[13]):
            a='CZK'
        elif(self.x1==p[14]):
            a='DKK'
        elif(self.x1==p[15]):
            a='DOP'
        elif(self.x1==p[16]):
            a='EGP'
        elif(self.x1==p[17]):
            a='EUR'
        elif(self.x1==p[18]):
            a='FJD'
        elif(self.x1==p[19]):
            a='GBP'
        elif(self.x1==p[20]):
            a='GTQ'
        elif(self.x1==p[21]):
            a='HKD'
        elif(self.x1==p[22]):
            a='HRK'
        elif(self.x1==p[23]):
            a='HUF'
        elif(self.x1==p[24]):
            a='IDR'
        elif(self.x1==p[25]):
            a='ILS'
        elif(self.x1==p[26]):
            a='ISK'
        elif(self.x1==p[27]):
            a='JPY'
        elif(self.x1==p[28]):
            a='KRW'
        elif(self.x1==p[29]):
            a='KZT'
        elif(self.x1==p[30]):
            a='MVR'
        elif(self.x1==p[31]):
            a='MXN'
        elif(self.x1==p[32]):
            a='MYR'
        elif(self.x1==p[33]):
            a='NOK'
        elif(self.x1==p[34]):
            a='NZD'
        elif(self.x1==p[35]):
            a='PAB'
        elif(self.x1==p[36]):
            a='PEN'
        elif(self.x1==p[37]):
            a='PHP'
        elif(self.x1==p[38]):
            a='PLN'
        elif(self.x1==p[39]):
            a='PYG'
        elif(self.x1==p[40]):
            a='RON'
        elif(self.x1==p[41]):
            a='RUB'
        elif(self.x1==p[42]):
            a='SAR'
        elif(self.x1==p[43]):
            a='SEK'
        elif(self.x1==p[44]):
            a='SGD'
        elif(self.x1==p[45]):
            a='THB'
        elif(self.x1==p[46]):
            a='TRY'
        elif(self.x1==p[47]):
            a='TWD'
        elif(self.x1==p[48]):
            a='UAH'
        elif(self.x1==p[49]):
            a='UYU'
        elif(self.x1==p[50]):
            a='ZAR'
        deep=0
        if(self.x2==p[0]):
            b='INR'
        elif(self.x2==p[1]):
            b='USD'
        elif(self.x2==p[2]):
            b='AED'
        elif(self.x2==p[3]):
            b='ARS'
        elif(self.x2==p[4]):
            b='AUD'
        elif(self.x2==p[5]):
            b='BGN'
        elif(self.x2==p[6]):
            b='BRL'
        elif(self.x2==p[7]):
            b='BSD'
        elif(self.x2==p[8]):
            b='CAD'
        elif(self.x2==p[9]):
            b='CHF'
        elif(self.x2==p[10]):
            b='CLP'
        elif(self.x2==p[11]):
            b='CNY'
        elif(self.x2==p[12]):
            b='COP'
        elif(self.x2==p[13]):
            b='CZK'
        elif(self.x2==p[14]):
            b='DKK'
        elif(self.x2==p[15]):
            b='DOP'
        elif(self.x2==p[16]):
            b='EGP'
        elif(self.x2==p[17]):
            b='EUR'
        elif(self.x2==p[18]):
            b='FJD'
        elif(self.x2==p[19]):
            b='GBP'
        elif(self.x2==p[20]):
            b='GTQ'
        elif(self.x2==p[21]):
            b='HKD'
        elif(self.x2==p[22]):
            b='HRK'
        elif(self.x2==p[23]):
            b='HUF'
        elif(self.x2==p[24]):
            b='IDR'
        elif(self.x2==p[25]):
            b='ILS'
        elif(self.x2==p[26]):
            b='ISK'
        elif(self.x2==p[27]):
            b='JPY'
        elif(self.x2==p[28]):
            b='KRW'
        elif(self.x2==p[29]):
            b='KZT'
        elif(self.x2==p[30]):
            b='MVR'
        elif(self.x2==p[31]):
            b='MXN'
        elif(self.x2==p[32]):
            b='MYR'
        elif(self.x2==p[33]):
            b='NOK'
        elif(self.x2==p[34]):
            b='NZD'
        elif(self.x2==p[35]):
            b='PAB'
        elif(self.x2==p[36]):
            b='PEN'
        elif(self.x2==p[37]):
            b='PHP'
        elif(self.x2==p[38]):
            b='PLN'
        elif(self.x2==p[39]):
            b='PYG'
        elif(self.x2==p[40]):
            b='RON'
        elif(self.x2==p[41]):
            b='RUB'
        elif(self.x2==p[42]):
            b='SAR'
        elif(self.x2==p[43]):
            b='SEK'
        elif(self.x2==p[44]):
            b='SGD'
        elif(self.x2==p[45]):
            b='THB'
        elif(self.x2==p[46]):
            b='TRY'
        elif(self.x2==p[47]):
            b='TWD'
        elif(self.x2==p[48]):
            b='UAH'
        elif(self.x2==p[49]):
            b='UYU'
        elif(self.x2==p[50]):
            b='ZAR'
        deep=0
        if(a=='INR'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/INR'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='USD'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/USD'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='AED'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/AED'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='ARS'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/ARS'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='AUD'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/AUD'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='BGN'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/BGN'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='BRL'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/BRL'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='BSD'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/BSD'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='CHF'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/CHF'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='CLP'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/CLP'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='CNY'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/CNY'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='COP'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/COP'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='CZK'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/CZK'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='DKK'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/DKK'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='DOP'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/DOP'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='EGP'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/EGP'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='EUR'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/EUR'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='FJD'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/FJD'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='GBP'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/GBP'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='GTQ'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/GTQ'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='HKD'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/HKD'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='HRK'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/HRK'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='HUF'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/HUF'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='IDR'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/IDR'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='ILS'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/ILS'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='ISK'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/ISK'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='JPY'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/JPY'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='KRW'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/KRW'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='KZT'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/KZT'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='MVR'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/MVR'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='MXN'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/MXN'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='MYR'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/MYR'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='NOK'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/NOK'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='NZD'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/NZD'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='PAB'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/PAB'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='PEN'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/PEN'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='PHP'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/PHP'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='PLN'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/PLN'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='PYG'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/PYG'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='RON'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/RON'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='RUB'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/RUB'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='SAR'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/SAR'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='SEK'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/SEK'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='SGD'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/SGD'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='THB'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/THB'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='TRY'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/TRY'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='TWD'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/TWD'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='UAH'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/UAH'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='UYU'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/UYU'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='ZAR'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/ZAR'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))

        elif(a=='CAD'):
            deep=0
            URL = 'https://api.exchangerate-api.com/v4/latest/CAD'
            currency = requests.get(URL)
            data = currency.json()
            x=float(data['rates'][b])
            c=float(self.x3)*x
            ze=0 
            self.toentry.config(text = str(c))



root=tk.Tk()
root.title("Convertor")
#root.minsize(width=400,height=400)
root.geometry("1250x650")
root.resizable(0,0)

load=Image.open("13.jpg")
render=ImageTk.PhotoImage(load)
img= Label(root,image= render)
img.place(x=0,y=0)
app=Convertor(master=root)
app.mainloop()
root.destroy()
