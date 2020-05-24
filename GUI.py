#!/usr/bin/env python
# coding: utf-8

# In[2]:


from SysSim import *
from tkinter import *


# In[3]:


root=Tk()
root.title("System simulator")
root.geometry("780x200")
#root.configure(background="black")

global inp_type1
global inp_type2
inp_var1=StringVar()
inp_var2=StringVar()

#interactive fn
def click():
    
    n=int(n_e.get())
    m=int(m_e.get())
    t=float(t_e.get())
    a=str(a_e.get()).split(',')
    b=str(b_e.get()).split(',')

    inp_type1=inp_var1.get()
    inp_type2=inp_var2.get()
    for i in range(len(a)):
        a[i] = float(a[i])
    for i in range(len(b)):
        b[i] = float(b[i])   

    if n!=m:
        temp=[]
        for i in range(n-m):
            temp.append(0)
        b=temp+b

    
    if inp_type1=="unit step" and inp_type2=="0":
        sys=System(n,m,a,b,inp_type1,t)
        A,B,C,D=sys.computeStateSpace()
        t,Xs,inp= sys.computeStateEqautions()
        y= sys.computeOutput()
        
    elif inp_type1=="0" and inp_type2=="impulse":
        sys=System(n,m,a,b,inp_type2,t)        
        A,B,C,D=sys.computeStateSpace()
        t,Xs,inp= sys.computeStateEqautions()
        y= sys.computeOutput()    
    elif inp_type1=="unit step" and inp_type2=="impulse":
        sys1=System(n,m,a,b,inp_type1,t)
        sys2=System(n,m,a,b,inp_type2,t)
        A,B,C,D=sys1.computeStateSpace()
        t,Xs,inp= sys1.computeStateEqautions()
        y= sys1.computeOutput()
        A2,B2,C2,D2=sys2.computeStateSpace()
        t2,Xs2,inp2= sys2.computeStateEqautions()
        y2= sys2.computeOutput()
    def plotOutputs():
        sys1.plotOutput()
        sys2.plotOutput()
        
    def plotStates():
        sys1.plotStates()
        sys2.plotStates()        
    #frame 3
    if inp_type1=="unit step" and inp_type2=="0":
        button_1=Button(frame_3,text="System Response",command = sys.plotOutput,padx=100)
        button_1.grid(row=0,column=0)
        button_2=Button(frame_3,text="Plot States    ",command = sys.plotStates,padx=100)
        button_2.grid(row=0,column=1)
    elif inp_type1=="0" and inp_type2=="impulse":
        button_1=Button(frame_3,text="System Response",command = sys.plotOutput,padx=100)
        button_1.grid(row=0,column=0)
        button_2=Button(frame_3,text="Plot States    ",command = sys.plotStates,padx=100)
        button_2.grid(row=0,column=1)
    elif inp_type1=="unit step" and inp_type2=="impulse":
        button_1=Button(frame_3,text="System Response",command = plotOutputs,padx=100)
        button_1.grid(row=0,column=0)
        button_2=Button(frame_3,text="Plot States    ",command = plotStates,padx=100)
        button_2.grid(row=0,column=1)
    

    
#root

frame_1 = LabelFrame(root, text="Input parameters",padx=5,pady=5)
frame_1.grid(row=0,column=0)

frame_2 = LabelFrame(root, text="Response type",padx=60,pady=20)
frame_2.grid(row=0,column=1)

frame_3 = LabelFrame(root, text="Visualizing",padx=5,pady=5)
frame_3.grid(row=1,column=0,columnspan=2)

#frame 1

lbl_1=Label(frame_1,text="Output's order :           ")
lbl_1.grid(row=0,column=0)
n_e=Entry(frame_1,width=50)
n_e.grid(row=0,column=1)

lbl_2=Label(frame_1,text="Inputs's order :             ")
lbl_2.grid(row=1,column=0)
m_e=Entry(frame_1,width=50)
m_e.grid(row=1,column=1)

lbl_3=Label(frame_1,text="Output's coefficients : ")
lbl_3.grid(row=2,column=0)
a_e=Entry(frame_1,width=50)
a_e.grid(row=2,column=1)

lbl_4=Label(frame_1,text="Inputs's coefficients : ")
lbl_4.grid(row=3,column=0)
b_e=Entry(frame_1,width=50)
b_e.grid(row=3,column=1)

lbl_5=Label(frame_1,text="Maximum time :        ")
lbl_5.grid(row=4,column=0)
t_e=Entry(frame_1,width=50)
t_e.grid(row=4,column=1)

#frame 2

check_1=Checkbutton(frame_2,text="Unit step      ",variable=inp_var1,onvalue="unit step",offvalue="0")
check_1.grid(row=0,column=0)
check_1.deselect()


check_2=Checkbutton(frame_2,text="Unit impulse",variable=inp_var2,onvalue="impulse",offvalue="0")
check_2.grid(row=1,column=0)
check_2.deselect()

button_3=Button(frame_2,text="Enter Parameters",command=click)
button_3.grid(row=2,column=1,rowspan=2)



mainloop()


# In[ ]:




