from tkinter import *
class View:    
    raiz = Tk()
    miFrame = Frame(raiz, width=600, height=400)
    miFrame.pack()

    num1Label = Label(miFrame, text="Num1").place(x=200, y=100)
    num1Input = Entry(miFrame)
    num1Input.place(x=270, y=100)

    num2Label = Label(miFrame, text="Num2").place(x=200, y=150)
    num2Input = Entry(miFrame)
    num2Input.place(x=270, y=150)
    resultLabel = Label(miFrame, text="Resultado").place(x=200, y=200)

    opcion = IntVar()
    
    operRadio1 = Radiobutton(miFrame, text="add", variable=opcion, value=1).place(x=150, y=250)
    operRadio2 = Radiobutton(miFrame, text="substract", variable=opcion, value=2).place(x=220, y=250)
    operRadio3 = Radiobutton(miFrame, variable=opcion, text="multiply", value=3).place(x=310, y=250)
    operRadio4 = Radiobutton(miFrame, variable=opcion, text="divide", value=4).place(x=400, y=250)

    def __init__(self):
        print("Enter the option: \n" 
                "1. Add \n"
                "2. Substract \n" 
                "3. Multiply \n"
                "4. Divide \n")
        self.option = input()
        print("Enter the number 1: ")
        self.num1 = input()
        print("Enter the number 2: ")
        self.num2 = input()

