#Importando Bibliotecas
import tkinter

#Calculadora
def calcular():

    print('======CALCULATOR=======')
    print('OPERATIONS')
    print('1 - Add')
    print('2 - Subtraction')
    print('3 - Multiply')

    op = input('Choice a operation:')

    if op not in('1', '2', '3'):
        print('Try Again!')
        return

    n1 = float(input('Type a number:'))
    n2 = float(input('Type another number:'))

    if op == '1':
        r = n1 + n2
        op_txt = 'addition'
    elif op == '2':
        r = n1 - n2
        op_txt = 'subtraction'
    elif op == '3':
        r = n1 * n2
        op_txt = 'multiply'

    print(f'The result of the {op_txt} operation is: {r}')

#Par ou Impar
def verparouimp():
    nm = int(input('Type a number:'))
    if nm%2 == '0':
        print('Your number is even')
    else:
        print('Your number is odd')

#Conversor Metro e Milímetro
def conmetmil():
    print('===CONVERTER METER IN MILLIMETER & CENTIMETERS===')
    me = int(input('Meters:'))
    ce = me*100
    mi = me*1000
    print('Meters: {}, Centimeters: {} and Millimeters: {}'.format(me, ce, mi))

#Janela Popup // Importando Biblioteca
def janelapp():
    import tkinter as tk
    from tkinter import simpledialog

    #definindo variaveis, janelas e titulos
    root = tk.Tk()

    root.title('Popup maneiro')
    def sum():
        x = simpledialog.askinteger(title = 'Valor 1', prompt = 'Digite X:')
        y = simpledialog.askinteger(title = 'Valor 2', prompt = 'Digite Y:')
        label.configure(text = str(x+y))

    #Construindo a janela e botões
    label = tk.Label(root, width = 50, height = 5)
    button = tk.Button(root, width = 50, text = 'Adição', command = sum)

    label.grid(row = 0, column = 1)
    button.grid(row = 1, column = 1)

    root.mainloop()

#Manager Home
print('Hi, i am a script manager by: Leon')
print('This is my scripts:')
print('1 - Calculator \n2 - Even or Odd \n3 - Converter Meter in Millimeter\n4 - Popup Window')
scr = input('What script you want play?')

if scr not in('1', '2', '3', '4'):
    print('Try again!')

if scr in('1'):
    calcular()

elif scr in('2'):
    verparouimp()

elif scr in('3'):
    conmetmil()

elif scr in ('4'):
    janelapp()
