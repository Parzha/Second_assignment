import tkinter
import math

my_cal = tkinter.Tk()
my_cal.title("Calculator")

expression = ""


# Create functions
def add(value):
    global expression
    expression += value
    label_result.config(text=expression)



def clear():
    global expression
    expression = ""
    label_result.config(text=expression)

def tan():
    global expression
    tan_degree=float(expression)
    tan_result=math.tan(tan_degree)
    label_result.config(text=tan_result)
def sin():
    global expression
    sin_degree=float(expression)
    sin_result=math.sin(sin_degree)
    label_result.config(text=sin_result)
def cos():
    global expression
    cos_degree=int(expression)
    cos_result=math.cos(cos_degree)
    label_result.config(text=cos_result)
def cot():
    global expression
    cot_degree=int(expression)
    cot_result=math.cot(cot_degree)
    label_result.config(text=cot_result)

def calculate():
    global expression
    result = ""


    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "error"
            expression = ""
    label_result.config(text=result)


label_result = tkinter.Label(my_cal, text="welcome")
label_result.grid(row=0,column=0,columnspan=5)

button_1 = tkinter.Button(my_cal,text=' 1 ',command=lambda: add("1"))
button_1.grid(row=1,column=0)

button_2 = tkinter.Button(my_cal,text=' 2 ',command=lambda:add("2"))
button_2.grid(row=1,column=1)

button_3 = tkinter.Button(my_cal,text=' 3 ',command=lambda:add("3"))
button_3.grid(row=1,column=2)

button_4 = tkinter.Button(my_cal,text=' 4 ',command=lambda:add("4"))
button_4.grid(row=2,column=0)

button_5 = tkinter.Button(my_cal,text=' 5 ',command=lambda:add("5"))
button_5.grid(row=2,column=1)

button_6 = tkinter.Button(my_cal,text=' 6 ',command=lambda:add("6"))
button_6.grid(row=2,column=2)

button_7 = tkinter.Button(my_cal,text=' 7 ',command=lambda:add("7"))
button_7.grid(row=3,column=0)

button_8 = tkinter.Button(my_cal,text=' 8 ',command=lambda:add("8"))
button_8.grid(row=3,column=1)

button_9 = tkinter.Button(my_cal,text=' 9 ',command=lambda:add("9"))
button_9.grid(row=3,column=2)

button_0 = tkinter.Button(my_cal,text=' 0 ',command=lambda:add("0"))
button_0.grid(row=4,column=0)

button_plus = tkinter.Button(my_cal,text='+',command=lambda:add("+"))
button_plus.grid(row=1,column=4)

button_sub = tkinter.Button(my_cal,text=' -',command=lambda:add("-"))
button_sub.grid(row=2,column=4)

button_multi = tkinter.Button(my_cal,text=' *',command=lambda:add("*"))
button_multi.grid(row=3,column=4)

button_div = tkinter.Button(my_cal,text=' /',command=lambda:add("/"))
button_div.grid(row=4,column=4)

button_tan = tkinter.Button(my_cal,text='tan ',command=lambda:tan())
button_tan.grid(row=1,column=5)
button_sin = tkinter.Button(my_cal,text='sin ',command=lambda:sin())
button_sin.grid(row=2,column=5)
button_cos = tkinter.Button(my_cal,text='cos ',command=lambda:cos())
button_cos.grid(row=3,column=5)
button_cot = tkinter.Button(my_cal,text='cot ',command=lambda:cot())
button_cot.grid(row=4,column=5)



button_clear = tkinter.Button(my_cal,text='CE',command=lambda: clear())
button_clear.grid(row=4,column=2)

button_equals = tkinter.Button(my_cal, text="=", width=2, command=lambda: calculate())
button_equals.grid(row=4, column=1 )









my_cal.mainloop()


