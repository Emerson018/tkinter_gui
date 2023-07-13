#criar um fazedor de qrcode
import customtkinter
import qrcode
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
#import ttkbootstrap as ttk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('dark-blue')

window = customtkinter.CTk()
window.title('Projetin')
window.geometry('800x500')

def gerar_codigo():
    link = entry1.get()

    label2['text'] = 'some text'
    #output_strig.set('Código gerado!!')
    gera_codigo = qrcode.make(link)
    gera_codigo.save('qrcode_teste.png')
    exibir_qrcode()

def exibir_qrcode():
    image = Image.open('qrcode_teste.png')
    image = image.resize((200,200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label_qrcode.configure(image=photo)
    label_qrcode.image = photo

def fecha_programa():
    window.destroy()

frame = customtkinter.CTkFrame(master=window)
frame.pack(pady=20, padx=60, fill= 'both', expand=True)

#edita_fonte__
font_label = customtkinter.CTkFont(family='Calibri', size=24, weight='bold')

#titulo__
label = ttk.Label(master=frame, text='criador de QRCODE', font=font_label)
label.pack(pady=12, padx=10)

#gera_link__
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Link para gerar')
entry1.pack(pady=12, padx=10)

#botao_login__
button = customtkinter.CTkButton(master=frame, text='Gerar código', command=gerar_codigo)
button.pack(pady=12, padx=10)

#botao_exit__
button_exit = customtkinter.CTkButton(master=window, text ='Fechar programa', command=fecha_programa)
button_exit.pack(side='bottom',padx=10,pady=10, anchor='se')

#botao_checkbox__
checkbox = customtkinter.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)

#mostra_qrcode__
label_qrcode = customtkinter.CTkLabel(master=frame)
label_qrcode.pack(pady=12, padx=10)

#texto_depois_de_gerar__
output_strig = tk.StringVar()
output_label = ttk.Label(master=frame,
                         text='Output',
                         font = font_label,
                         textvariable=output_strig)
output_label.pack(pady=5)

label2 = ttk.Label(master=frame, text = 'Testando')
label2.pack()

window.mainloop()