import tkinter as tk
from tkinter import simpledialog

word = str(tk.simpledialog.askstring("What is you word", "Word: "))

print("Orginal String is ", word)
print("Printing only even index chars")

word_length = len(word)

for arrangement in range(word_length):
    if arrangement%2 == 0:
        print(word[arrangement])