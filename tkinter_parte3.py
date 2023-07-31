import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('pack')
window.geometry('600x400')

'''
#widgets__
label1 = ttk.Label(window, text= 'First Label', background= 'red')
label2 = ttk.Label(window, text= 'First Label', background= 'blue')
label3 = ttk.Label(window, text= 'First Label', background= 'green')

#layout__
label1.pack(side= 'top', expand= 'True', fill= 'both',pady= 50, padx= 70)
label2.pack(side= 'top', fill= 'x')
label3.pack(side= 'top', expand= 'True', fill= 'y')
'''


#top_frame__
top_frame = ttk.Frame(window) #faz isso pra ter só uma direcao dos layout
label1 = ttk.Label(top_frame, text= '1 Label', background= 'red')
label2 = ttk.Label(top_frame, text= '2 Label', background= 'blue')

#middle_widget__

label3 = ttk.Button(window, text= '3 Label')

#bottom_frame__
bot_frame = ttk.Frame(window)
label4 = ttk.Label(bot_frame, text= '6 Label', background= 'pink')
label5 = ttk.Label(bot_frame, text= '5 Label', background= 'yellow')

#top_layout__
label1.pack(side= 'left', fill= 'both', expand= 'True')
label2.pack(side= 'left', fill= 'both', expand= 'True')
top_frame.pack(fill= 'both', expand= 'True')

#middle_layout__
label3.pack(expand= 'True')

#bottom_layout__
label4.pack(side= 'left', expand= 'True', fill= 'both' )
label5.pack(side= 'left', expand= 'True', fill= 'both')
bot_frame.pack(fill= 'both', expand= 'True', padx= 20, pady= 20)

# side = escolhe o lado
#expand = expandir True ou False, pra expandir até o final
#fill = completar pra x, y ou os dois
#padX e Y = distancia das laterais até o centro do layout
window.mainloop()