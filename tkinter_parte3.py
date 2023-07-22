import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('pack')
window.geometry('600x400')

#widgets__
label1 = ttk.Label(window, text= 'First Label', background= 'red')
label2 = ttk.Label(window, text= 'First Label', background= 'blue')
label3 = ttk.Label(window, text= 'First Label', background= 'green')

#layout__
label1.pack(side= 'top', expand= 'True', fill= 'both',pady= 50, padx= 70)
label2.pack(side= 'top', fill= 'x')
label3.pack(side= 'top', expand= 'True', fill= 'y')


# side = escolhe o lado
#expand = expandir o negocio
#fill = completar pra x, y ou os dois
#padX e Y = distancia das laterais até o centro do layout
window.mainloop()