import tkinter as tk
from tkinter import ttk

window =  tk.Tk()
window.title('colocando layout em cima do otro')
window.geometry('600x400')

def mostra_label():
    global label_visible

    if label_visible:
        label1.place_forget()
        label_visible = False
    else:
        label_visible = True
        label1.place(x= 50, y= 100, width= 200, height= 150)

label_visible = True

#widgets__
label1 = ttk.Label(window, text= 'Label 1', background= 'green')
label2 = ttk.Label(window, text= 'Label 1', background= 'blue')
label3 = ttk.Label(window, text= 'Label 1', background= 'red')

button1 =ttk.Button(window, text= 'mostra label 1', command= lambda: label1.tkraise())
button2 = ttk.Button(window, text= 'mostra label 2', command= lambda: label2.tkraise())
button3 = ttk.Button(window, text= 'mostra label 3', command= lambda: label3.tkraise())
button4 = ttk.Button(window, text= 'Hide/show label 1', command= mostra_label)

#layout__
label1.place(x= 50, y= 100, width= 200, height= 150)
label2.place(x= 60, y= 100, width= 200, height= 150)
label3.place(x= 70, y= 100, width= 200, height= 150)

button1.place(rely= 1, relx= 0.8, anchor= 'se')
button2.place(rely= 1, relx= 1, anchor= 'se')
button3.place(rely= 1, relx= 0.6, anchor= 'se')
button4.place(rely= 1, relx= 0.4, anchor= 'se')



window.mainloop()