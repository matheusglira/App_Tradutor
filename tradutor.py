import tkinter as tk
from googletrans import Translator

win = tk.Tk()
win.title("Tradutor")
win.geometry("320x80")

def traducao():
	palavra = entry.get()
	tradutor = Translator(service_urls=['translate.google.com'])
	traducao1 = tradutor.translate(palavra, dest="pt")
	label1 = tk.Label(win, text=f"Traduzido em português: {traducao1.text}", bg="yellow")
	label1.grid(row=2, column=0)

label = tk.Label(win, text="Digite a palavra: ")
label.grid(row=0, column=0, sticky="W")

entry = tk.Entry(win)
entry.grid(row=1, column=0)

button = tk.Button(win, text="Tradutor", command=traducao)
button.grid(row=1, column=2)

win.mainloop()
