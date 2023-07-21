import tkinter as tk
from tkinter import ttk

#teste pra fazer um interface com tabelas

#window_configs__
window = tk.Tk()
window.title("DEDO NO CU E GUITAR HERO")
window.geometry('600x400')

#notebook widget__
label1 = ttk.Label(window, text= 'Label 1', background='green')
label2 = ttk.Label(window, text= 'Label 2', background='purple')
label3 = ttk.Label(window, text= 'Label 3', background='red')
label4 = ttk.Label(window, text= 'Label 4', background='blue')
label5 = ttk.Label(window, text= 'Label 5', background='white')

#escolhe as colunas__
window.columnconfigure(0, weight= 1)
window.columnconfigure(1, weight= 1)
window.columnconfigure(2, weight= 1)

#escolhe as linhas
window.rowconfigure(0, weight= 1)
window.rowconfigure(1, weight= 1)
window.rowconfigure(2, weight= 1 )

#escolhe os lugar onde vao ta as label
label1.grid(row= 0, column= 1, sticky= 'nsew')
label2.grid(row= 1, column= 1, columnspan= 2, sticky= 'nsew')
label3.grid(row= 0 , column= 0, rowspan= 3, sticky= 'nsew')
label4.grid(row= 2, column= 2, sticky='nsew')

label5.place(relx= 0.5, rely= 0.5, relwidth= 1)

window.mainloop()