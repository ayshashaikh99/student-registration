from tkinter import *


main_window = Tk()

#label
my_name=Label(main_window,text = "What is your name").grid(row = 0 , column = 0)

my_age=Label(main_window,text = "What is your age").grid(row = 1 , column = 0)

#text input
Entry(main_window, width=50,borderwidth = 5 ).grid(row = 0, column = 1)

Entry(main_window, width=50,borderwidth = 5 ).grid(row = 1, column = 1)

def on_click():
    print(f"my name is {my_name}, and my age is {my_age}" )
 # button
Button(main_window,text = "click here",command =on_click).grid(row = 2 , column=1)


main_window.mainloop()