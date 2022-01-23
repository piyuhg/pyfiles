#!/usr/bin/python3
from tkinter import*

def Clicked(inp):
	global operator
	operator = operator + str(inp)
	text_Input.set(operator)

def Exit():
	calc.destroy()
	exit()

def Clr():
	global operator
	operator = operator[0:-1]
	text_Input.set(operator)

def AC():
	global operator
	operator = ""
	text_Input.set(0)

def EVAL():
	global operator
	result = str(eval(operator))
	text_Input.set(result)

calc = Tk()
calc.title("GUI Calculator")
operator = ""

text_Input = StringVar()

Display = Entry(calc, bg = "powder blue", fg = "black", font = "calibri 18 bold", textvariable = text_Input, bd = 25, insertwidth = 4, justify = 'right').grid(columnspan = 4, row = 0)

button_off = Button(calc, padx = 16, pady = 8, bd = 8, fg = "black", font = "calibri 12 bold", text = "OFF", command = Exit, bg = "orange").grid(row = 1, columnspan = 1, column = 0)

button_Clr = Button(calc, padx = 16, pady = 8, bd = 8, fg = "black", font = "calibri 12 bold", text = "CLR", command = Clr, bg = "powder blue").grid(row = 1, column = 2)

button_AC = Button(calc, padx = 16, pady = 8, bd = 8, fg = "white", font = "calibri 12 bold", text = "AC", command = AC, bg = "dark grey").grid(row = 1, column = 3)

button_7 = Button(calc, padx = 16, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text = "7", command = lambda:Clicked(7), bg = "powder blue").grid(row = 2, column = 0)

button_8 = Button(calc, padx = 16, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text = "8", command = lambda:Clicked(8), bg = "powder blue").grid(row = 2, column = 1)

button_9 = Button(calc, padx = 16, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text = "9", command = lambda:Clicked(9), bg = "powder blue").grid(row = 2, column = 2)

button_divide = Button(calc, padx = 20, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text = "/", command = lambda:Clicked("/"), bg = "powder blue").grid(row = 2, column = 3)

button_4 = Button(calc, padx = 16, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text = "4", command = lambda:Clicked(4), bg = "powder blue").grid(row = 3, column = 0)

button_5 = Button(calc, padx = 16, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text = "5", command = lambda:Clicked(5), bg = "powder blue").grid(row = 3, column = 1)

button_6 = Button(calc, padx = 16, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text = "6", command = lambda:Clicked(6), bg = "powder blue").grid(row = 3, column = 2)

button_multiply = Button(calc, padx = 16, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text = "x", command = lambda:Clicked("*"), bg = "powder blue").grid(row = 3, column = 3)

button_1 = Button(calc, padx = 16, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text = "1", command = lambda:Clicked(1), bg = "powder blue").grid(row = 4, column = 0)

button_2 = Button(calc, padx = 16, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text = "2", command = lambda:Clicked(2), bg = "powder blue").grid(row = 4, column = 1)

button_3 = Button(calc, padx = 16, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text = "3", command = lambda:Clicked(3), bg = "powder blue").grid(row = 4, column = 2)

button_subtract = Button(calc, padx = 20, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text = "-", command = lambda:Clicked("-"), bg = "powder blue").grid(row = 4, column = 3)

button_dot = Button(calc, padx = 20, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text = ".", command = lambda:Clicked("."), bg = "powder blue").grid(row = 5, column = 0)

button_0 = Button(calc, padx = 16, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text = "0", command = lambda:Clicked(0), bg = "powder blue").grid(row = 5, column = 1)

button_add = Button(calc, padx = 16, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text = "+", command = lambda:Clicked("+"), bg = "powder blue").grid(row = 5, column = 2)

button_equal = Button(calc, padx = 16, pady = 8, bd = 8, fg = "black", font = "calibri 18 bold", text ="=", command = EVAL, bg = "powder blue").grid(row = 5, column = 3)

calc.mainloop()
