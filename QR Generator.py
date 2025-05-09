"""
QR code generator using Python
-> Run this command in CMD: pip install qrcode pillow
"""

import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Define functions
def createQR(*args):
    data = text_entry.get()
    if data:
        img = qrcode.make(data)  # Generate QR Code
        resized_img = img.resize((280, 250))
        tkimage = ImageTk.PhotoImage(resized_img)
        qr_canvas.delete("all")
        qr_canvas.create_image(0, 0, anchor=tk.NW, image=tkimage)
        qr_canvas.image = tkimage  # Keep a reference to avoid garbage collection
    else:
        messagebox.showwarning("Error", "Enter some data first")

def saveQR(*args):
    data = text_entry.get()
    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280, 250))
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG files", "*.png")])
        if path:
            resized_img.save(path)
            messagebox.showinfo("Success", "QR Code is saved")
    else:
        messagebox.showwarning("Error", "Enter some data first")


# GUI code
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("300x380")
root.config(bg="white")
root.resizable(False, False)

# First frame (QR display)
frame1 = tk.Frame(root, bd=2, relief=tk.RAISED)
frame1.place(x=10, y=0, width=280, height=250)

# Try to load default image or show blank

cover_img = tk.PhotoImage(file="image.gif")


qr_canvas = tk.Canvas(frame1, width=280, height=250)
if cover_img:
    qr_canvas.create_image(0, 0, anchor=tk.NW, image=cover_img)
    qr_canvas.image = cover_img
qr_canvas.bind("<Double-1>", saveQR)
qr_canvas.pack(fill=tk.BOTH)

# Second frame (Entry and Buttons)
frame2 = tk.Frame(root, bd=2, relief=tk.RAISED)
frame2.place(x=10, y=260, width=280, height=100)

text_entry = ttk.Entry(frame2, width=26, font=("Sitka Small", 11), justify=tk.CENTER)
text_entry.bind("<Return>", createQR)
text_entry.place(x=5, y=5)

btn_1 = ttk.Button(frame2, text="Create", width=10, command=createQR)
btn_1.place(x=25, y=50)

btn_2 = ttk.Button(frame2, text="Save", width=10, command=saveQR)
btn_2.place(x=100, y=50)

btn_3 = ttk.Button(frame2, text="Exit", width=10, command=root.quit)
btn_3.place(x=175, y=50)

root.mainloop()
