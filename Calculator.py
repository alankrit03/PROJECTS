from tkinter import *

def click(event):
    global current_screen
    new_val = event.widget.cget("text")
    print(type(display_value.get()))
    print(new_val,type(new_val))
    if new_val == "Del":
        try:
            current_screen.pop(-1)
            display_value.set(''.join(current_screen))
        except :
            display_value.set('Error')


    elif new_val == 'C':
        current_screen=[]
        display_value.set('')

    elif new_val == '=':
        try:
            result=str(eval((display_value.get())))
            current_screen=list(result)
            display_value.set(result)
        except Exception as e:
            display_value.set('Error')
            current_screen=[]

    else:
        display_value.set(display_value.get()+new_val)
        current_screen.append(new_val)
    print('bind succesful')
    screen.update()

current_screen=[]
root = Tk()
# WIDTH X HEIGHT
root.geometry('500x580')
root.resizable(width=False,height=False)
root.title('Calculator')
root.configure(background='black')
root.wm_iconbitmap("calci.ico")


display_value = StringVar()
display_value.set('')
screen = Entry(root, bg='black', font='helvetica 45 bold', textvar=display_value, fg='yellow')
screen.pack(padx=10)



#colors_options: #39ff14,#FF69B4
mainframe = Frame(bg='#FF69B4')
mainframe.pack(fill=BOTH, expand=1)

frame_1 = Frame(mainframe, bg='cyan')
frame_1.pack( fill=X)
b1 = Button(frame_1, text='1', font='lucida 30 bold', bg='black', fg='white',
        activebackground='black', activeforeground='cyan')
b1.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
b1.bind("<Button-1>",click)

b2 = Button(frame_1, text='2', font='lucida 30 bold', bg='black', fg='white',
        activebackground='black', activeforeground='cyan')
b2.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
b2.bind("<Button-1>",click)

b3 = Button(frame_1, text='3', font='lucida 30 bold', bg='black', fg='white',
        activebackground='black', activeforeground='cyan')
b3.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
b3.bind("<Button-1>",click)

button_add = Button(frame_1, text='+', font='lucida 30 bold', bg='black', fg='white',
              activebackground='black', activeforeground='cyan')
button_add.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
button_add.bind("<Button-1>",click)


frame_2 = Frame(mainframe, bg='cyan')
frame_2.pack( fill=X)
b4 = Button(frame_2, text='4', font='lucida 30 bold', bg='black', fg='white',
        activebackground='black', activeforeground='cyan')
b4.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
b4.bind("<Button-1>",click)

b5 = Button(frame_2, text='5', font='lucida 30 bold', bg='black', fg='white',
        activebackground='black', activeforeground='cyan')
b5.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
b5.bind("<Button-1>",click)

b6 = Button(frame_2, text='6', font='lucida 30 bold', bg='black', fg='white',
        activebackground='black', activeforeground='cyan')
b6.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
b6.bind("<Button-1>",click)

button_mutiply = Button(frame_2, text='*', font='lucida 30 bold', bg='black', fg='white',
        activebackground='black', activeforeground='cyan')
button_mutiply.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
button_mutiply.bind("<Button-1>",click)



frame_3 = Frame(mainframe, bg='cyan')
frame_3.pack( fill=X)

b7 = Button(frame_3, text='7', font='lucida 30 bold', bg='black', fg='white',
        activebackground='black', activeforeground='cyan')
b7.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
b7.bind("<Button-1>",click)

b8 = Button(frame_3, text='8', font='lucida 30 bold', bg='black', fg='white',
        activebackground='black', activeforeground='cyan')
b8.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
b8.bind("<Button-1>",click)

b9 = Button(frame_3, text='9', font='lucida 30 bold', bg='black', fg='white',
        activebackground='black', activeforeground='cyan')
b9.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
b9.bind("<Button-1>",click)

button_subtract = Button(frame_3, text='-', font='lucida 30 bold', bg='black', fg='white',
        activebackground='black', activeforeground='cyan')
button_subtract.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
button_subtract.bind("<Button-1>",click)



frame_4 = Frame(mainframe, bg='cyan')
frame_4.pack( fill=X)

button_point = Button(frame_4, text='.', font='lucida 30 bold', bg='black', fg='white',
        activebackground='black', activeforeground='cyan')
button_point.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
button_point.bind("<Button-1>",click)

b0 = Button(frame_4, text='0', font='lucida 30 bold', bg='black', fg='white',
        activebackground='black', activeforeground='cyan')
b0.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
b0.bind("<Button-1>",click)

button_00 = Button(frame_4, text='00', font='lucida 25 bold', bg='black', fg='white',
        activebackground='black', activeforeground='cyan')
button_00.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
button_00.bind("<Button-1>",click)

button_divide = Button(frame_4, text='/', font='lucida 30 bold', bg='black', fg='white',
              activebackground='black', activeforeground='cyan')
button_divide.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
button_divide.bind("<Button-1>",click)


frame_5 = Frame(mainframe, bg='cyan')
frame_5.pack( fill=X)

button_c = Button(frame_5, text='C', font='lucida 30 bold', bg='black', fg='white',
              activebackground='black', activeforeground='cyan')
button_c.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
button_c.bind("<Button-1>",click)


button_del = Button(frame_5, text='Del', font='lucida 30 bold', bg='black', fg='white',
              activebackground='black', activeforeground='cyan')
button_del.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
button_del.bind("<Button-1>",click)

button_equal = Button(frame_5, text='=', font='lucida 30 bold', bg='black', fg='white',
        activebackground='black', activeforeground='cyan')
button_equal.pack(expand=1, fill=BOTH, padx=10, pady=10, side='left')
button_equal.bind("<Button-1>",click)

root.mainloop()

#Code Written By ALANKRIT AGARWAL