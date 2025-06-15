from tkinter import *
from tkinter import filedialog, messagebox, font, colorchooser
from PIL import Image, ImageTk

messagebox.showwarning("Mario", "5 More Days Until Mario Steals Your Liver")
messagebox.showwarning("Mario", "4 More Days Until Mario Steals Your Liver")
messagebox.showwarning("Mario", "3 More Days Until Mario Steals Your Liver")
messagebox.showwarning("Mario", "2 More Days Until Mario Steals Your Liver")
messagebox.showwarning("Mario", "1 More Day Until Mario Steals Your Liver")

root = Tk()
root.title("")
root.resizable(False, False)
root.attributes("-fullscreen", True)
root.config(bg="#000000")

img = Image.open("pic.png")
img = img.resize((1920, 1080))
img = ImageTk.PhotoImage(img)

Label(root, image=img, bg="black").grid(row=1, sticky="E")

root.mainloop()