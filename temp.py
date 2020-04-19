# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
import math

def add(list, size): 
   if (size == 0): 
     return 0
   else: 
     return list[size - 1] + add(list, size - 1)

def sub(list, size):
    diff=0
    for ele in range(0, size-1): 
        diff = list[ele] - list[ele+1]
    return diff

def mul(list,size):
    mul=1
    for i in range(0,size):
        mul=mul * list[i]
    return mul    
    
def div(list, size):
    list2=[]
    quo=1
    quo1=list[0]/list[1]
    list2.append(quo1)
    for ele in range(2,len(list),2):
        quo1=list[ele]/list[ele+1]
        list2.append(quo1)
    return list2    


def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
    return x 
def gcd(list, size):
    num1=list[0] 
    num2=list[1] 
    gcd=find_gcd(num1,num2) 
    for i in range(2,len(list)): 
        gcd=find_gcd(gcd,list[i]) 
    return gcd

def find_lcm(num1, num2): 
    if(num1>num2): 
        num = num1 
        den = num2 
    else: 
        num = num2 
        den = num1 
    rem = num % den 
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den 
    gcd = den 
    lcm1 = int(int(num1 * num2)/int(gcd)) 
    return lcm1 
def lcm(list, size):
    num1 = list[0] 
    num2 = list[1] 
    lcm = find_lcm(num1, num2) 
    for i in range(2, len(list)): 
        lcm = find_lcm(lcm, list[i]) 
    return lcm

def mod(list,size):
    l1=[]
    num1=list[0]
    num2=list[1]
    mod=num1 % num2
    l1.append(mod)
    mod1=1
    for i in range(2,len(list),2):
        mod1 = list[i] % list [i+1] 
        l1.append(mod1)
    return l1  

def fact(list,size):
    l3=[]
    fact=1
    for i in range(0,size):
        fact=math.factorial(list[i])
        l3.append(fact)
    return l3    
def extraxt_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def remove(string): 
    return string.replace(",", " ")

def Reverse(lst): 
    return [ele for ele in reversed(lst)] 

def calculate():
    text = textin.get()
    text1 = remove(text)
    for word in text1.split(' '):
        if word.upper() in operations.keys():
            try: 
                list1 = extraxt_from_text(text1)
                if(text.upper().__contains__('SUBTRACT') or text.upper().__contains__('SUBTRACTION') or text.upper().__contains__('DIVIDES')):
                    list1=Reverse(list1)      
                r = operations[word.upper()](list1, len(list1))
                list.delete(0,END)
                list.insert(END,r) 
                
            except Exception as e:
                list.delete(0,END)
                list.insert(END,Exception) 
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'The following operation is not supported')
            

operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,'SUBTRACTION':sub,
               '+':add,'-':sub,'/':div,'MULTIPLY':mul,'MULTIPLICATION':mul,'*':mul,'PRODUCT':mul,
                'FACT':fact,'FACTORIAL':fact,
                  'DIVISION':div, 'DIV':div,'DIVIDE':div,'DIVIDES':div,'DIVIDED':div,
                  'GCD':gcd,'HCF':gcd,'LCM':lcm,'MOD':mod,'MODULUS':mod,'REMAINDER':mod}
win = Tk()
win.geometry('500x400')
win.title('Smart Calcy')
win.configure(bg='lightskyblue')
l4 = Label(win, text=' ',bg='lightskyblue')
l4.config(anchor=CENTER)
l4.pack()
l1 = Label(win , text='Hello,I am a smart calculator',fg='lightskyblue',font='Courier',bg='black',width=30 , padx=3)
l1.config(anchor=CENTER)
l1.pack()
l5 = Label(win, text=' ',bg='lightskyblue')
l5.config(anchor=CENTER)
l5.pack()
l2 = Label(win , text='My name is Calcy' ,fg='lightskyblue',font='Courier',bg='black', padx=3)
l2.config(anchor=CENTER)
l2.pack()
l6 = Label(win, text=' ',bg='lightskyblue')
l6.config(anchor=CENTER)
l6.pack()
l3 = Label(win , text='How may i help you??',fg='lightskyblue',font='Courier',bg='black', padx=3)
l3.config(anchor=CENTER)
l3.pack()
l7 = Label(win, text=' ',bg='lightskyblue',height=2)
l7.config(anchor=CENTER)
l7.pack()
textin = StringVar()
e1 = Entry(win , width=30 , textvariable = textin,font=('Helvetica', 10),relief='solid',justify='center')
e1.pack(anchor="center")
l8 = Label(win, text=' ',bg='lightskyblue',height=1)
l8.config(anchor=CENTER)
l8.pack()
b1 = Button(win , text='Just this' ,fg='lightskyblue',bg='black',font='Helvetica',activebackground='green',activeforeground='black',justify='center',command=calculate)
b1.pack(anchor="center")
l9 = Label(win, text=' ',bg='lightskyblue',height=1)
l9.config(anchor=CENTER)
l9.pack()
list = Listbox(win,width=50,height=3,font=('Helvetica', 10),relief='solid',justify='center')
list.pack(anchor="center")

win.mainloop()
