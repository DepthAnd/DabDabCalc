import tkinter
from math import sqrt
from tkinter import *

window = Tk()
window.title('DabDabCalc')
window.geometry("625x650")
window['bg'] = '#494b52'

calc = tkinter.Entry(window, justify='right', font=('TimesNewRoman', 38,), width=15,)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=5, stick='we',  padx=5, pady='5px', ipady=30)


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[:0]
    calc.delete(0, tkinter.END)
    calc.insert(0, value + digit)


def add_parentheses(parentheses):
     value = calc.get()
     if value[0] == '0' and len(value) == 1:
         value = value[:0]
     calc.delete(0, tkinter.END)
     calc.insert(0, value + parentheses)


def make_digit_button(digit):
   return tkinter.Button(text=digit, bd=5, font=('TimesNewRoman', 32,), command=lambda: add_digit(digit))


def make_operation_button(operation):
   return tkinter.Button(text=operation, bd=5, font=('TimesNewRoman', 32,), command=lambda: add_operation(operation))


def make_parentheses_button(operation):
   return tkinter.Button(text=operation, bd=5, font=('TimesNewRoman', 32,), command=lambda: add_parentheses(operation))


def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-*/.':
        value = value[:-1]
    calc.delete(0, tkinter.END)
    calc.insert(0, value+operation)


def make_operation(operation):
    return tkinter.Button(text=operation, bd=5, font=('TimesNewRoman', 32,), command=calculate)


def make_clear(ac):
    return tkinter.Button(text=ac, bd=5, font=('TimesNewRoman', 32,), command=clear)


def make_radical():
    try:
        value = float(calc.get())
        result = sqrt(value)
        calc.delete(0, tkinter.END)
        calc.insert(0, str(result))
    except ValueError:
        calc.delete(0, tkinter.END)
        calc.insert(0, "Error")


def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        operation = value[-1]
        value = value[:-1] + operation + value[:-1]
    calc.delete(0, tkinter.END)
    calc.insert(0, eval(value))


def clear():
    calc.delete(0, tkinter.END)
    calc.insert(0, '0')


make_digit_button('1').grid(row=1, column=0, stick='wens', padx='5px', pady='5px')
make_digit_button('2').grid(row=1, column=1, stick='wens', padx='5px', pady='5px')
make_digit_button('3').grid(row=1, column=2, stick='wens', padx='5px', pady='5px')
make_digit_button('4').grid(row=2, column=0, stick='wens', padx='5px', pady='5px')
make_digit_button('5').grid(row=2, column=1, stick='wens', padx='5px', pady='5px')
make_digit_button('6').grid(row=2, column=2, stick='wens', padx='5px', pady='5px')
make_digit_button('7').grid(row=3, column=0, stick='wens', padx='5px', pady='5px')
make_digit_button('8').grid(row=3, column=1, stick='wens', padx='5px', pady='5px')
make_digit_button('9').grid(row=3, column=2, stick='wens', padx='5px', pady='5px')
make_digit_button('0').grid(row=4, column=1, stick='wens', padx='5px', pady='5px')
make_operation_button('+').grid(row=3, column=3, stick='wens', padx='5px', pady='5px')
make_operation_button('.').grid(row=4, column=4, stick='wens', padx='5px', pady='5px')
make_operation_button('-').grid(row=4, column=3, stick='wens', padx='5px', pady='5px')
make_operation_button('*').grid(row=1, column=3, stick='wens', padx='5px', pady='5px')
make_operation_button('/').grid(row=2, column=3, stick='wens', padx='5px', pady='5px')
make_parentheses_button('(').grid(row=2, column=4, stick='wens', padx='5px', pady='5px')
make_parentheses_button(')').grid(row=3, column=4, stick='wens', padx='5px', pady='5px')
tkinter.Button(text='√', bd=5, font=('TimesNewRoman', 32,), command=lambda: make_radical()).grid(row=1, column=4, stick='wens', padx='5px', pady='5px')
make_clear('AC').grid(row=4, column=0, stick='wens', padx='5px', pady='5px')
make_operation('=').grid(row=4, column=2, stick='wens', padx='5px', pady='5px')

window.grid_columnconfigure(0, minsize=125)
window.grid_columnconfigure(1, minsize=125)
window.grid_columnconfigure(2, minsize=125)
window.grid_columnconfigure(3, minsize=125)
window.grid_columnconfigure(4, minsize=125)

window.grid_rowconfigure(1, minsize=125)
window.grid_rowconfigure(2, minsize=125)
window.grid_rowconfigure(3, minsize=125)
window.grid_rowconfigure(4, minsize=125)

window.mainloop()

