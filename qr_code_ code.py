#QR CODE GRNERATOR
import qrcode
from PIL import Image
import tkinter as tk
from tkinter import PhotoImage
class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x800")
        self.label=tk.Label(self.root, text="QR CODE GENERATOR",font=('Arial',18,))
        self.label.pack(pady=50)
        
        self.label1=tk.Label(self.root, text="Enter the URL",font=('Arial',18))
        self.label1.pack(padx=50,pady=0)


        self.url= tk.Entry(self.root,font=('Arial',18))
        self.url.pack(padx=50,pady=0)
        
        
        self.button=tk.Button(self.root,text="CONVERT",font=("Arial",15),command=self.value)
        self.button.pack(padx=10,pady=10)
        
        
        self.Image1 = PhotoImage(file="QR_CODE_IMAGE.png")
        self.image_label = tk.Label(self.root,image=self.Image1)
        
        self.root.mainloop()
    def value(self):
        self.URL=str(self.url.get())
        self.qr = qrcode.QRCode(
                 version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,
                 border=4,
            )
        self.qr.add_data(self.URL)
        self.qr.make(fit=True)
        self.img = self.qr.make_image(fill_color="black", back_color="white")
        self.img.save("QR_CODE_IMAGE.png")
                
        self.Image1 = PhotoImage(file="QR_CODE_IMAGE.png")
        self.image_label = tk.Label(self.root,image=self.Image1)
        
        self.image_label.pack()
        
      
MyGUI()

