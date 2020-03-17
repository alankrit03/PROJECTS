from tkinter import *

if __name__ == "__main__":

    root = Tk()
    root.geometry('500x400')
    root.title('Movie_Journal')

    Label(text="Welcome", bg='black', fg='red').pack()
    Label(text="Welcome to Movie_Journal by Alankrit",bg='black',fg='yellow').place(x=200,y=50)
    root.config(background='black')

    a=Frame(root,bg='cyan',width=100,height=200)
    a.place(x=0,y=100)
    Label(a,text="Welcome",bg='cyan', fg='red').pack()


    root.mainloop()