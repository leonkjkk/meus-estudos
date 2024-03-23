#importando as bibliotecas
import tkinter as tk
from tkinter import simpledialog

def janelapp():
#definindo variaveis, janelas e titulos
    root = tk.Tk()

    root.iconbitmap(r'C:\Users\victor\Downloads\pylogo.ico')

    root.title('Conversor Temperatura')
    def fahtocel():
        x = simpledialog.askinteger(title = 'Fahrenheit', prompt = 'Digite a Temperatura:')
        label.configure(text = str((x-32)/1.8))

    def celtofah():
        y = simpledialog.askinteger(title = 'Celsius', prompt = 'Digite a Temperatura:')
        label.configure(text = str(y*1.8+32))

    #Construindo a janela e botões
    label = tk.Label(root, width = 30, height = 5)
    button = tk.Button(root, width = 30, text = 'Fahrenheit to Celsius', command = fahtocel)
    button2 = tk.Button(root, width = 30, text = 'Celsius to Fahrenheit', command = celtofah)

    label.grid(row = 0, column = 1)
    button.grid(row = 1, column = 1)
    button2.grid(row = 1, column = 0)

    root.mainloop()
janelapp()
