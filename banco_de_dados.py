import tkinter as tk
from tkinter import ttk
from random import choice

#window__
window = tk.Tk()
window.geometry('500x400')
window.title('banco de dados')

#data__
first_names = ['Emerson','Matheus','Carlos','Eduardo','Maria','Iino','Zero','Saulo']
last_names = ['Cano','Bob','Sayrix','teve','caneta','Robson','Teclado','Serioman']

#treeview__
table = ttk.Treeview(window, columns= ('first', 'last', 'email'), show= 'headings')
table.heading('first', text= 'First Name') 
table.heading('last', text= 'Last Name') 
table.heading('email', text= 'Email')
table.pack(fill= 'both', expand= True)

#Inser Values into a table__
for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first[0]}{last}@gmail.com'
    data = (first, last, email)
    table.insert(parent= '', index= 0, values= data)

#events__
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])

def delete_itens(_):
    print(f'Data has been deleted!')
    for i in table.selection():
        table.delete(i)

table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_itens)

window.mainloop()

