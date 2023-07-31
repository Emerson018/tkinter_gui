import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

def button_func():
    entry_text = entry.get()

    label['text'] = entry_text

    #desativa a palavra
    label['state'] = 'disable'

#window_configs__
window = tk.Tk()
window.title("DEDO NO CU E GUITAR HERO")
window.geometry('600x400')
window.minsize(200,100)
window.resizable(True,True)
#x,y = escala do window

#screen attributes__
print(window.winfo_screenwidth())
print(window.winfo_screenheight())
#window.overrideredirect(True) = tira a barra de menu
grip = ttk.Sizegrip(window)
grip.place(relx= 1.0, rely= 1.0, anchor= 'se')


#sobreescreve algo. entry e label estao usando os mesmos dados
string_var = tk.StringVar()
#pra n deixar marcado a 'box' e transformar ela em int, str ou bool
check_var = tk.StringVar()

radio_var = tk.StringVar()

#menu__
menu = tk.Menu(window)
#submenu__ tearoff tira as linha do menu
file_menu = tk.Menu(menu, tearoff= False)
file_menu.add_command(label= 'New', command= lambda: print('New file'))
file_menu.add_separator()
file_menu.add_command(label= 'Open', command= lambda: print('Open file'))
menu.add_cascade(label= 'File', menu= file_menu)

#another_sub_menu__
help_check_string = tk.StringVar()

help_menu = tk.Menu(menu, tearoff= False)
help_menu.add_checkbutton(label= 'putinha?',
                onvalue= 'on', 
                offvalue= 'off', variable= help_check_string)
help_menu.add_separator()
menu.add_cascade(label= 'Help', menu= help_menu)

window.configure(menu= menu)

menu_button = ttk.Menubutton(window, text = 'Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff= False)
button_sub_menu.add_command(label='cachorra', command= lambda: print('safada'))
button_sub_menu.add_checkbutton(label= 'seleciona ai troxa')
menu_button.configure(menu= button_sub_menu)




#notebook widget__
notebook = ttk.Notebook(window)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text= 'Tab 1')
notebook.add(tab2, text= 'Tab 2')
notebook.pack()
# pra rodar em otra tab: ex => label = ttk.Label(tab2,.........)

#parei em 4:15:52

label = ttk.Label(
        master=window,
        text='texto inicial',
        background= 'pink', #cor
        textvariable=string_var)
label.pack(side= 'bottom', fill='both') #escolhe lado e preenche

#pra poder dar entrada no que tu escrever
entry = ttk.Entry(
        master=window,
        textvariable=string_var)
entry.pack()

button = ttk.Button(
        master=window,
        text='botao do lá ele',
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
combo = ttk.Combobox(window,
        textvariable= nome_string)
combo.configure(value = items)
combo.pack()

#events__
#combobosSelected é padrao|tentar usar sempre lambda|
combo.bind(
        '<<ComboboxSelected>>',
        lambda event: combo_label.config
        (text = f'Valor selecionado: {nome_string.get()}'))
combo_label = ttk.Label(
        window,
        text= 'Lista de Itens')
combo_label.pack()

#spinbox__
spin = ttk.Spinbox(
        window,
        from_= 0, to = 20)
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down')) 
spin.pack()

#slider
scale_int = tk.IntVar(value= 0)
scale = ttk.Scale(
        window,
        command= lambda value: print(scale_int.get()),
        from_ = 0,
        to = 100,
        length= 150,
        orient= 'horizontal',
        variable = scale_int)
scale.pack()

#scroll_text__

#progress_bar_
progress = ttk.Progressbar(
        window,
        variable= scale_int,
        maximum= 100,
        orient= 'horizontal',
        mode= 'determinate',
        length= 50)
progress.pack()

#canvas__
canvas = tk.Canvas(window,
        bg = 'blue')
canvas.pack()

#left,top,right, bottom
canvas.create_rectangle(
        (259,25,50,100),
        fill= 'purple', 
        width= 3, 
        outline='white')




window.mainloop()

#LABEL = traducao é tipo pra legenda, ou rótulo
#dá pra escrever só a variavel, pq dai ele automaticamente vai pra MASTER
#'radio buttons' precisam de um VALUE
#tkinter-event-binding
#site :https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html