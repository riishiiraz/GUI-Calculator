# This Code Was Written on [Aug-10-2019] by @riishiiraz

from tkinter import *
from math import factorial

root=Tk()
root.title("Calculator")

root.resizable(0,0)

var=StringVar(root)
var.set('0')

scr=Frame(root)
scr.pack()

btn=Frame(root)
btn.pack()

fnt="Times", 35


ht,wt=1,4
bd=1
pdy=pdx=2
bg="#bfafff"
fc='#bfdfff'  # focus Color
pbg='#00ff00' # press Bg

class Stack:
    def __init__(self):
        self.list = []
        self.c_ind = 0
        self.len = 0
    def add(self , expr):
        self.list.append(expr)
        self.len = self.list.__len__()
        self.c_ind = self.len-1
    def next(self):
        if(self.len==0):    return
        if(self.c_ind < (self.len-1)):
            self.c_ind+=1
        else:
            root.bell()
            return
        var.set(self.list[self.c_ind])
    def prev(self):
        if(self.len==0):    return
        if(self.c_ind>0):
            self.c_ind-=1
        else:
            root.bell()
            return
        var.set(self.list[self.c_ind])
    
stack = Stack()        
        

def equate():
    try:
        result=eval(var.get().replace('÷','/').replace('×','*'))
        stack.add(var.get())
        var.set(result)
        stack.add(result)
    except SyntaxError:
        var.set("Syntax Error")


def click(key):
    if key=='/':    key='÷'
    if key=='*':    key='×'
    
    if key=='=':
        equate()
        return
    if var.get()[0].isalpha():
        var.set('0')
        
    while var.get().startswith('0') :
        var.set(var.get()[1:])

    content = var.get()
    if((key in ["÷","×"] and content!="") and var.get()!=""):
        last = var.get()[-1]
        if(key==last):
            return

    if(key=="."):
        for x in content[::-1]:
            if(x in ["÷","×","+","-"]):
                var.set(var.get()+str(key))
                return
            elif(x=="."):
                return
    

    if(key in ["÷","×","+","-"] and var.get()!=""):
        last = var.get()[-1]
        if (last in ["÷","×","+","-"]):
            var.set(var.get()[:-1]+key)
            return
        
        
    var.set(var.get()+str(key))

def math(typ):
    if var.get().replace(' ','').isalpha(): var.set('0')
    
    try:
        if typ=='sq':
            if len(var.get())>=20:
                var.set("Memoey Error")
                return
            var.set(eval(var.get())**2)
            
        elif typ=='sqrt':   var.set(eval(var.get())**.5)
        elif typ=='fa':   var.set(factorial(eval(var.get())))
        
    except ValueError as err:
        
        var.set("Syntax Error")
    except OverflowError as ovr:
        var.set("Memoey Error")


b_9=Button(btn,text='9',font=fnt , bd=bd , width=wt ,bg=bg)
b_9.config(height=ht , cursor='hand2',command=lambda :click(9))
b_9.grid(row=0,column=0,pady=pdy,padx=pdx)

b_8=Button(btn,text='8',font=fnt , bd=bd , width=wt,bg=bg)
b_8.config(height=ht , cursor='hand2',command=lambda :click(8))
b_8.grid(row=0,column=1,pady=pdy,padx=pdx)

b_7=Button(btn,text='7',font=fnt , bd=bd , width=wt,bg=bg)
b_7.config(height=ht , cursor='hand2',command=lambda :click(7))
b_7.grid(row=0,column=2,pady=pdy,padx=pdx)

b_6=Button(btn,text='6',font=fnt , bd=bd , width=wt,bg=bg)
b_6.config(height=ht , cursor='hand2',command=lambda :click(6))
b_6.grid(row=1,column=0,pady=pdy,padx=pdx)

b_5=Button(btn,text='5',font=fnt , bd=bd , width=wt,bg=bg)
b_5.config(height=ht , cursor='hand2',command=lambda :click(5))
b_5.grid(row=1,column=1,pady=pdy,padx=pdx)

b_4=Button(btn,text='4',font=fnt , bd=bd , width=wt,bg=bg)
b_4.config(height=ht , cursor='hand2',command=lambda :click(4))
b_4.grid(row=1,column=2,pady=pdy,padx=pdx)


b_3=Button(btn,text='3',font=fnt , bd=bd , width=wt,bg=bg)
b_3.config(height=ht , cursor='hand2',command=lambda :click(3))
b_3.grid(row=2,column=0,pady=pdy,padx=pdx)

b_2=Button(btn,text='2',font=fnt , bd=bd , width=wt,bg=bg)
b_2.config(height=ht , cursor='hand2',command=lambda :click(2))
b_2.grid(row=2,column=1,pady=pdy,padx=pdx)

b_1=Button(btn,text='1',font=fnt , bd=bd , width=wt,bg=bg)
b_1.config(height=ht , cursor='hand2',command=lambda :click(1))
b_1.grid(row=2,column=2,pady=pdy,padx=pdx)

b_0=Button(btn,text='0',font=fnt , bd=bd , width=wt,bg=bg)
b_0.config(height=ht , cursor='hand2',command=lambda :click(0))
b_0.grid(row=3,column=0,pady=pdy,padx=pdx)

b_p=Button(btn,text='+',font=fnt+("bold",) , bd=bd , width=wt,bg=bg)
b_p.config(height=ht , cursor='hand2',command=lambda :click('+'))
b_p.grid(row=0,column=3,pady=pdy,padx=pdx)

b_mi=Button(btn,text='‒',font=fnt+("bold",) , bd=bd , width=wt,bg=bg)
b_mi.config(height=ht , cursor='hand2',command=lambda :click('-'))
b_mi.grid(row=1,column=3,pady=pdy,padx=pdx)

b_mu=Button(btn,text='×',font=fnt+("bold",) , bd=bd , width=wt,bg=bg)
b_mu.config(height=ht , cursor='hand2',command=lambda :click('*'))
b_mu.grid(row=2,column=3,pady=pdy,padx=pdx)

b_d=Button(btn,text='÷',font=fnt+("bold",) , bd=bd , width=wt,bg=bg)
b_d.config(height=ht , cursor='hand2',command=lambda :click('/'))
b_d.grid(row=3,column=3,pady=pdy,padx=pdx)

b_pt=Button(btn,text='.',font=fnt , bd=bd , width=wt,bg=bg)
b_pt.config(height=ht , cursor='hand2',command=lambda :click('.'))
b_pt.grid(row=3,column=2,pady=pdy,padx=pdx)

b_eq=Button(btn,text='=',font=fnt+("bold",) , bd=bd , width=wt,bg=bg)
b_eq.config(height=ht , cursor='hand2',command=equate)
b_eq.grid(row=4,column=3,pady=pdy,padx=pdx)

b_cl=Button(btn,text='C',font=fnt , bd=bd , width=wt,bg=bg)
b_cl.config(height=ht , cursor='hand2',command=lambda:var.set('0'))
b_cl.grid(row=3,column=1,pady=pdy,padx=pdx)


#  functions
# ϰ!  χ

b_sq= Button(btn,text='ϰ²',font=fnt , bd=bd , width=wt,bg=bg)
b_sq.config(height=ht , cursor='hand2',command=lambda:math('sq'))
b_sq.grid(row=4,column=0,pady=pdy,padx=pdx)

b_fa= Button(btn,text='ϰ!',font=fnt , bd=bd , width=wt,bg=bg)
b_fa.config(height=ht , cursor='hand2',command=lambda:math('fa'))
b_fa.grid(row=4,column=1,pady=pdy,padx=pdx)


b_sqrt= Button(btn,text='√',font=fnt , bd=bd , width=wt,bg=bg)
b_sqrt.config(height=ht , cursor='hand2',command=lambda:math('sqrt'))
b_sqrt.grid(row=4,column=2,pady=pdy,padx=pdx)


# ====================================== Screen ====================================

ent=Entry(scr,textvariable=var,font='Times 45',width=15,state='readonly', highlightthickness = 1, justify = 'left')
ent.pack()
ent.focus()

# =================================== Bindings ==================================================
def clr_one():
    if len(var.get())==1 or var.get()[0].isalpha():
        var.set('0')
    else:
        var.set(var.get()[:-1])

keylist=['b_'+str(x) for x in list(range(10))+['p','mi','mu','d','pt','eq','cl','sq','sqrt','fa'] ]



# for Focus In and Out =======================================================

for k in keylist:
    
    exec(   "%s.bind('<Enter>',lambda event :%s.config(bg='%s'))"% (k,k,fc)   )

for k in keylist:
    
    exec(   "%s.bind('<Leave>',lambda event :%s.config(bg=bg))"% (k,k)   )
# =============================================================================

# For Key Click on Focus ==========================================================
z=zip(keylist[:16],list(range(10))+['+','-','*','/','.','='])

for btn,k in z:
    exec(   "root.bind('%s',lambda event : %s.config(bg=pbg) or click('%s'))"% (k,btn,k)   )

root.bind("<KeyRelease>",lambda e:[eval(b).config(bg=bg) for b in keylist])
# ==============================================================================


root.bind("<Return>",lambda e:equate() or b_eq.config(bg=pbg) )
root.bind("<BackSpace>",lambda e:clr_one())
root.bind("(",lambda e:click("("))
root.bind(")",lambda e:click(")"))

root.bind("<Up>", lambda e:stack.prev())
root.bind("<Down>", lambda e:stack.next())

ent.bind('<Enter>',lambda e:ent.config(fg='green'))
ent.bind('<Leave>',lambda e:ent.config(fg='black'))


root.mainloop()

