# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 19:48:38 2021

@author: ASPrajna
"""

from tkinter import *
from tkinter import messagebox

fc=1
t1,t2,t3,t4,t5,t6,t7,t8,t9=" "," "," "," "," "," "," "," "," "
w=0


def restart():
    global t1,t2,t3,t4,t5,t6,t7,t8,t9,fc,w
    w=0
    fc=1
    t1,t2,t3,t4,t5,t6,t7,t8,t9=" "," "," "," "," "," "," "," "," "
    bu1.set(" *")
    bu2.set(" *")
    bu3.set(" *")
    bu4.set(" *")
    bu5.set(" *")
    bu6.set(" *")
    bu7.set(" *")
    bu8.set(" *")
    bu9.set(" *")
    return

def verify():
    global w
    print(t1+"-"+t2+"-"+t3+"-"+t4+"-"+t5+"-"+t6+"-"+t7+"-"+t8+"-"+t9+"-")
    if t1==t2  and  t3==t2  and  t3=="X":
         messagebox.showinfo("WINNER","WINNER IS X")
         w=1
         return
    if t1==t2 and t3==t2 and t3=="0":
         messagebox.showinfo("WINNER","WINNER IS 0")
         w=1
         return
    if t4==t5 and t5==t6 and t6=="X":
         messagebox.showinfo("WINNER","WINNER IS X")
         w=1
         return
    if t4==t5 and t5==t6 and t6=="0":
         messagebox.showinfo("WINNER","WINNER IS 0")
         w=1
         return
    if t7==t8 and t9==t8 and t8=="X":
         messagebox.showinfo("WINNER","WINNER IS X")
         w=1
         return
    if t7==t8 and t9==t7 and t7=="0":
         messagebox.showinfo("WINNER","WINNER IS 0")
         w=1
         return
    if t1==t4 and t7==t4 and t1=="X":
         messagebox.showinfo("WINNER","WINNER IS X")
         w=1
         return
    if t1==t4 and t4==t7 and t1=="0":
         messagebox.showinfo("WINNER","WINNER IS 0")
         w=1
         return
    if t2==t5 and t8==t5 and t2=="X":
         messagebox.showinfo("WINNER","WINNER IS X")
         w=1
         return
    if t5==t2 and t8==t2 and t2=="0":
         messagebox.showinfo("WINNER","WINNER IS 0")
         w=1
         return
    if t3==t9 and t6==t9 and t3=="X":
         messagebox.showinfo("WINNER","WINNER IS X")
         w=1
         return
    if t3==t9 and t6==t9 and t3=="0":
         messagebox.showinfo("WINNER","WINNER IS 0")
         w=1
         return
    if t1==t5 and t9==t5 and t5=="X":
         messagebox.showinfo("WINNER","WINNER IS X")
         w=1
         return
    if t5==t1 and t9==t5 and t5=="0":
         messagebox.showinfo("WINNER","WINNER IS 0")
         w=1
         return
    if t3==t5 and t5==t7 and t3=="X":
         messagebox.showinfo("WINNER","WINNER IS X")
         w=1
         return
    if t3==t5 and t5==t7 and t3=="0":
         messagebox.showinfo("WINNER","WINNER IS 0")
         w=1
         return

def check1():
  global fc ,t1
  if w==0:
      if fc==1:
          bu1.set("X")
          t1="X"
          fc=0
      else:
          bu1.set("0")
          fc=1
          t1="0"
  else:
      messagebox.showerror("Warning","Winner is declared")
  verify()
  return
     
def check2():
  global fc ,t2
  if w==0:
      if fc==1:
          bu2.set("X")
          fc=0
          t2="X"
      else:
          bu2.set("0")
          fc=1
          t2="0"
  else:
      messagebox.showerror("Warning","Winner is declared")
  verify()
  return
      
def check3():
  global fc ,t3
  if w==0:
      if fc==1:
          bu3.set("X")
          fc=0
          t3="X"
      else:
          bu3.set("0")
          fc=1
          t3="0"
  else:
      messagebox.showerror("Warning","Winner is declared")
  verify()
  return
     
def check4():
  global fc ,t4
  if w==0:
      if fc==1:
          bu4.set("X")
          fc=0
          t4="X"
      else:
          bu4.set("0")
          fc=1
          t4="0"
  else:
      messagebox.showerror("Warning","Winner is declared")
  verify()
  return

def check5():
  global fc ,t5
  if w==0:
      if fc==1:
          bu5.set("X")
          fc=0
          t5="X"
      else:
          bu5.set("0")
          fc=1 
          t5="0"
  else:
      messagebox.showerror("Warning","Winner is declared")
  verify()
  return

def check6():
  global fc ,t6
  if w==0:
      if fc==1:
          bu6.set("X")
          fc=0
          t6="X"
      else:
          bu6.set("0")
          fc=1
          t6="0"
  else:
      messagebox.showerror("Warning","Winner is declared")
  verify()
  return

def check7():
  global fc ,t7
  if w==0:
      if fc==1:
          bu7.set("X")
          fc=0
          t7="X"
      else:
          bu7.set("0")
          fc=1
          t7="0"
  else:
      messagebox.showerror("Warning","Winner is declared")
  verify()
  return

def check8():
  global fc ,t8
  if w==0:
      if fc==1:
          bu8.set("X")
          fc=0
          t8="X"
      else:
          bu8.set("0")
          fc=1
          t8="0"
  else:
      messagebox.showerror("Warning","Winner is declared")
  verify()
  return

def check9():
  global fc ,t9
  if w==0:
      if fc==1:
          bu9.set("X")
          fc=0
          t9="X"
      else:
          bu9.set("0")
          fc=1
          t9="0"
  else:
      messagebox.showerror("Warning","Winner is declared")
  verify()
  return


root=Tk()
bu1=StringVar()
bu2=StringVar()
bu3=StringVar()
bu4=StringVar()
bu5=StringVar()
bu6=StringVar()
bu7=StringVar()
bu8=StringVar()
bu9=StringVar()
bu1.set(" *")
bu2.set(" *")
bu3.set(" *")
bu4.set(" *")
bu5.set(" *")
bu6.set(" *")
bu7.set(" *")
bu8.set(" *")
bu9.set(" *")
b1=Button(root,padx=25 , pady=25,command=check1,textvariable=bu1,font = ('Helvetica',20,'bold','italic'))
b2=Button(root,padx=25 , pady=25,command=check2,textvariable=bu2,font = ('Helvetica',20,'bold','italic'))
b3=Button(root,padx=25 , pady=25,command=check3,textvariable=bu3,font = ('Helvetica',20,'bold','italic'))
b4=Button(root,padx=25 , pady=25,command=check4,textvariable=bu4,font = ('Helvetica',20,'bold','italic'))
b5=Button(root,padx=25 , pady=25,command=check5,textvariable=bu5,font = ('Helvetica',20,'bold','italic'))
b6=Button(root,padx=25 , pady=25,command=check6,textvariable=bu6,font = ('Helvetica',20,'bold','italic'))
b7=Button(root,padx=25 , pady=25,command=check7,textvariable=bu7,font = ('Helvetica',20,'bold','italic'))
b8=Button(root,padx=25 , pady=25,command=check8,textvariable=bu8,font = ('Helvetica',20,'bold','italic'))
b9=Button(root,padx=25 , pady=25,command=check9,textvariable=bu9,font = ('Helvetica',20,'bold','italic'))
label =Label(root,text=" ",font = ('Helvetica',10,'bold','italic'))
restart=Button(root,text="RESTART" ,padx=25, pady=25,command=restart,font = ('Helvetica',20,'bold','italic'),bg="red")

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
label.grid(row=3,columnspan=3)
restart.grid(row=4,columnspan=3)
root.mainloop()