import tkinter
from tkinter import *
from tkinter import messagebox

#```````````````````````````````````````````````````````````````````
root=tkinter.Tk()
root.geometry('290x250')
root.title("calculater")
root.resizable(False,False)
root.configure(bd=3,relief=GROOVE,borderwidth=3)

#``````````````````````````````````````````````````````````````````````````````
var1=StringVar()
var2=StringVar()
var3=StringVar()
expression=''
expression1=''
selected1=0
selected2=0

def sum1():
   s=int(entry1.get())+int(entry2.get())
   var3.set(s)
   
def sub():
   s=int(entry1.get())-int(entry2.get())
   var3.set(s)
   
def div():
   s=int(entry1.get())/int(entry2.get())
   var3.set(s)
   
def multi():
   s=int(entry1.get())*int(entry2.get())
   var3.set(s)
   
def input_num(number):
   global expression
   global expression1
   global selected1
   global selected2
  
   if(selected1==1):
      expression=expression+str(number)
      var1.set(expression)
   elif(selected2==1):
     
      expression1=expression1+str(number)
      var2.set(expression1)
      
def select_iout1():
   global selected1
   global selected2
   selected2=0
   selected1=1

def select_iout2():
   global selected2
   global selected1
   selected1=0
   selected2=1  
   
def clear_all():
   global expression
   global expression1
   entry1.delete(first=0,last=10)
   entry2.delete(first=0,last=10)
   entry3.delete(first=0,last=10)
   expression=""
   expression1=""
   
   
#````````````````````````````````````````````````````````````````````````````````
entry1=Entry(root,textvariable=var1,bd=5,relief=GROOVE,exportselection=0)
entry1.place(x=10,y=10)
entry2=Entry(root,textvariable=var2,bd=5,relief=GROOVE,exportselection=0)
entry2.place(x=150,y=10)
entry3=Entry(root,bd=5,relief=GROOVE,width=40,textvariable=var3,exportselection=0)
entry3.place(x=14,y=40)

 
#`````````````````````````````````````````````````````````````````````````````````  

button1=Button(root,text=1,width=5,height=3,bd=3,relief=GROOVE,command= lambda:input_num(1))
button1.place(x=5,y=65)
button2=Button(root,text=2,width=5,height=3,bd=3,relief=GROOVE,command=lambda:input_num(2))
button2.place(x=50,y=65)
button3=Button(root,text=3,width=5,height=3,bd=3,relief=GROOVE,command=lambda:input_num(3))
button3.place(x=95,y=65)
button4=Button(root,text=4,width=5,height=3,bd=3,relief=GROOVE,command=lambda:input_num(4))
button4.place(x=140,y=65)
button5=Button(root,text=5,width=5,height=3,bd=3,relief=GROOVE,command=lambda:input_num(5))
button5.place(x=185,y=65)
button6=Button(root,text=6,width=5,height=3,bd=3,relief=GROOVE,command=lambda:input_num(6))
button6.place(x=5,y=120)
button7=Button(root,text=7,width=5,height=3,bd=3,relief=GROOVE,command=lambda:input_num(7))
button7.place(x=50,y=120)
button8=Button(root,text=8,width=5,height=3,bd=3,relief=GROOVE,command=lambda:input_num(8))
button8.place(x=95,y=120)
button9=Button(root,text=9,width=5,height=3,bd=3,relief=GROOVE,command=lambda:input_num(9))
button9.place(x=140,y=120)
button9=Button(root,text=0,width=5,height=3,bd=3,relief=GROOVE,command=lambda:input_num(0))
button9.place(x=185,y=120)
field1=Button(root,text="field1",width=5,height=3,bd=3,relief=GROOVE,command=select_iout1)
field1.place(x=230,y=65)
field2=Button(root,text="field2",width=5,height=3,bd=3,relief=GROOVE,command=select_iout2)
field2.place(x=230,y=120)

#``````````````````````````````````````````````````````````````````````````````````````
sum=Button(root,text="+",width=5,height=3,bd=3,relief=GROOVE,command=sum1)
sum.place(x=5,y=177)
sub=Button(root,text="-",width=5,height=3,bd=3,relief=GROOVE,command=sub)
sub.place(x=50,y=177)
div=Button(root,text="/",width=5,height=3,bd=3,relief=GROOVE,command=div)
div.place(x=95,y=177)
mul=Button(root,text="*",width=5,height=3,bd=3,relief=GROOVE,command=multi)
mul.place(x=140,y=177)
percent=Button(root,text="%",width=5,height=3,bd=3,relief=GROOVE)
percent.place(x=185,y=177)
AC=Button(root,text="AC",width=5,height=3,bd=3,relief=GROOVE,command=clear_all)
AC.place(x=230,y=177)

root.mainloop()
