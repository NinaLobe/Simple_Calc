import Tkinter
from  Tkinter import *
import tkMessageBox
result = ""

def add():
    a=float(firstNumber.get())
    b=float(secondNumber.get())
    result = str(a+b) + "\n"
    resultText.insert("0.0", result)
def substract():
    a=float(firstNumber.get())
    b=float(secondNumber.get())
    result = str(a - b) + "\n"
    resultText.insert("0.0", result)
def multiply():
    a=float(firstNumber.get())
    b=float(secondNumber.get())
    result = str(a * b) + "\n"
    resultText.insert("0.0", result)
def divide():
    a=float(firstNumber.get())
    b=float(secondNumber.get())
    result = str(a/b) + "\n"
    resultText.insert("0.0", result)
def reset():
    resultText.delete("0.0", END)


window = Tkinter.Tk()
window.geometry("300x250")

#naslov
appName = Tkinter.Label(window,text = "Calculate",font=("Arial", 22))
appName.grid(row=0, column=2)

firstNumberText = Tkinter.Label(window,text = "First number:")
firstNumberText.grid(row=1, column=1)
firstNumber =Tkinter.Entry(window)
firstNumber.grid(row=1, column=2)

secondNumberText = Tkinter.Label(window,text = "Second number:")
secondNumberText.grid(row=2, column=1)
secondNumber =Tkinter.Entry(window)
secondNumber.grid(row=2, column=2)

#Gumbi
addButton = Tkinter.Button(window,text="+",command = add, bg = "blue",width = 8, font=("Ariel", 13))
addButton.grid(row=5,column=2,sticky=E)
substractButton = Tkinter.Button(window,text="  -  ",command = substract,width = 8,font=("Ariel", 13),bg = "red")
substractButton.grid(row=5,column=2,sticky=W)
multiplyButton = Tkinter.Button(window,text="  *  ",command = multiply, bg = "yellow",width = 8,font=("Ariel", 13))
multiplyButton.grid(row=6, column=2,sticky=E)
divideButton = Tkinter.Button(window,text="  :  ",command = divide,width = 8,font=("Ariel", 13),bg = "green")
divideButton.grid(row=6, column=2,sticky=W)

#Result
resultLabel = Tkinter.Label(window,text = "Result: ")
resultLabel.grid(row=8, column=1)
resultText = Tkinter.Text(window,height=4, width=20)
resultText.grid(row=8, column=2)

#Gumb, ki pobrise parametre ali vsaj rezultat
resetButton = Tkinter.Button(window,text= "Reset",command = reset)
resetButton.grid(row=10,column=2)


#resultText.delete("0.1", END)
#resultText.insert("0.0", result)


window.mainloop()