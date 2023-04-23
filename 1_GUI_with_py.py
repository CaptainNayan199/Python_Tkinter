from tkinter import *
import tkinter as nayan

root = Tk()
root.title("Day_1 Tkinter")
root.geometry("400x600")

myLabel = Label(root, text="Hello Nayan")
myLabel2 = Label(root, text="Nayan in the house")
frame = nayan.Frame(root)
button = nayan.Button(frame, text="Click me", command=None)
button.pack(side="top")
frame.pack()
myLabel.pack()
myLabel2.pack()