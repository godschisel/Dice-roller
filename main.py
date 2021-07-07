import random, tkinter

master = tkinter.Tk()
result = 0
c_width = 400
c_height = 50

def calculate(eq):
    global result
    new_eq = eq.replace("(", "").replace(")", "")
    a = 0
    for i in new_eq.split("+"):
        if '-' in i:
           new_i = i.split('-')
           print(new_i)
           a += int(new_i[0]) - int(new_i[1])
        else:
           a += int(i)

    result = f'{eq} = {a}'
    

dice_count_label = tkinter.Label(text='How many?').grid(row=0,column=0)
how_many = tkinter.StringVar(master)
how_many.set(" ") 
dice_count = tkinter.OptionMenu(master, how_many, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10').grid(row=0,column=1)

dice_type_label = tkinter.Label(text='Dice type?').grid(row=0,column=2)
dice_type = tkinter.StringVar(master)
dice_type.set("  ")
w = tkinter.OptionMenu(master, dice_type, "d4", "d6", "d8", "d10", "d12", "d20", "d100").grid(row=0,column=3)

mod_label = tkinter.Label(text='Modifier:').grid(row=0,column=4)
modifier = tkinter.Entry(width=4)
modifier.grid(row=0,column=5)


def activate():
    global canvas
    canvas.delete("all")
    mod = modifier.get()
    if len(mod) == 0:
        mod = 0
    try:
        mod = int(mod)
        c = []
        if how_many.get() == " ":
            a = 1
        else:
            a = int(how_many.get())
        if dice_type.get() == "  ":
            b = 4
        else:
            b = int(dice_type.get()[1:])
        for i in range(a):
            dice_roll = random.randrange(1,b+1)
            c.append(str(dice_roll))
        if mod >= 0:
            eq = "(" + " + ".join(c) + ") + " + str(mod)
        else:    
            eq = "(" + " + ".join(c) + ") " + str(mod)
        calculate(eq)
        canvas.create_text(c_width // 2, c_height // 2, text = result)
    except ValueError:
        canvas.create_text(c_width // 2, c_height // 2, text = 'Error', fill="red")
        


button = tkinter.Button(text="Go!", command=activate).grid(row=0,column=6)


canvas = tkinter.Canvas(bg="white", height=c_height, width=c_width)
canvas.grid(row=1,column=0, columnspan=7)


tkinter.mainloop()