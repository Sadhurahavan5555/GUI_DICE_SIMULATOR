from tkinter import *
import random

window = Tk()

label = Label(window,font=('bold',300))
def roll():
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.config(text=f'{random.choice(number)}')
    label.pack()
    
window.minsize(600,600)  
window.maxsize(600,600)   
window.title('ROLL THE DICE')  

heading = Label(window,text='ROLL THE DICE',font=('bold',55),bg='blue')
heading.pack(fill=X)


button = Button(window,text='Roll',font=('normal',45),bg='white',command=lambda:roll())
button.pack()

window.mainloop()
