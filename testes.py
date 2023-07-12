import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text = entry.get()

    label['text'] = entry_text

    #desativa a palavra
    label['state'] = 'disable'


window = tk.Tk()
window.title("Lugar dos testes")
window.geometry('600x400')

#sobreescreve algo. entry e label estao usando os mesmos dados
string_var = tk.StringVar()
#pra n deixar marcado a 'box' e transformar ela em int, str ou bool
check_var = tk.StringVar()
#
radio_var = tk.StringVar()

label = ttk.Label(
        master=window,
        text='texto inicial',
        textvariable=string_var)
label.pack()

#pra poder dar entrada no que tu escrever
entry = ttk.Entry(
        master=window,
        textvariable=string_var)
entry.pack()

button = ttk.Button(
        master=window,
        text='botao de teste',
        command= button_func)
button.pack()

#checkbox__
check = ttk.Checkbutton(
        window,
        text='clica se tu é arrombado',
        command = lambda:print(check_var.get()),
        variable= check_var,
        onvalue= 'marcado',
        offvalue= 'desmarcado')
check.pack()

#radio(bolinhas de seleção)__
radio = ttk.Radiobutton(
        window,
        text='Resposta errada',
        value= 1,
        variable=radio_var,
        command= lambda: print(radio_var.get()))
radio.pack()

radio2 = ttk.Radiobutton(
        window,
        text='Resposta certa',
        value= 2,
        variable=radio_var,
        command= lambda: print(radio_var.get()))
radio2.pack()

#combox__
items = ('Sayrix', 'Emerson', 'relampago')

nome_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window,textvariable= nome_string)
combo.configure(value = items)
combo.pack()

#events__
#combobosSelected é padrao|tentar usar sempre lambda|
combo.bind(
        '<<ComboboxSelected>>',
        lambda event: combo_label.config
        (text = f'Valor selecionado: {nome_string.get()}'))
combo_label = ttk.Label(window, text= 'Lista de Itens')
combo_label.pack()

#spinbox__
spin = ttk.Spinbox(
        window,
        from_= 0, to = 20)
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down')) 
spin.pack()

#canvas__
canvas = tk.Canvas(window, bg = 'green')
canvas.pack()

#left,top,right, bottom
canvas.create_rectangle((80,20,100,200), fill= 'red', width= 10)

window.mainloop()

#LABEL = traducao é tipo pra legenda, ou rótulo
#dá pra escrever só a variavel, pq dai ele automaticamente vai pra MASTER
#'radio buttons' precisam de um VALUE
#tkinter-event-binding
#site :https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html