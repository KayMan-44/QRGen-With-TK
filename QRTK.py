import tkinter as tk
from QR import Generate_QR


class WindowWidget:
    def __init__(self, win):
        self.lbl1 = tk.Label(win, text="QR Generator")
        self.lbl2 = tk.Label(win, text="Enter a link:")
        self.lbl3 = tk.Label(win, text="Enter a name:")
        self.lbl4 = tk.Label(win, text="QR Code Generated!")
        self.lbl5 = tk.Label(win, text="Both link and name are required")

        # Link
        self.entry_Var = tk.StringVar()
        self.LinkEntry = tk.Entry(win, textvariable=self.entry_Var)

        # Name
        self.entry_Var2 = tk.StringVar()
        self.nameEntry = tk.Entry(win, textvariable=self.entry_Var2)

        # Button
        self.QRButton = tk.Button(
            win, text="Generate QR image", command=self.generate_QR_pressed
        )

        # Placement
        self.lbl1.pack()
        self.lbl2.pack()
        self.LinkEntry.pack()
        self.lbl3.pack()
        self.nameEntry.pack()
        self.QRButton.pack()
        self.lbl4.pack_forget()
        self.lbl5.pack_forget()

    def generate_QR_pressed(self):
        link = self.entry_Var.get()
        name = self.entry_Var2.get()
        if link and name:
            filename = name + ".png"
            Generate_QR(link, filename)
            self.lbl4.pack()
            self.lbl5.pack_forget()
        else:
            print("Both link and name are required.")
            self.lbl5.pack()
            self.lbl4.pack_forget()


window = tk.Tk()
window.title("QRGen")
window.geometry("800x600+10+10")
Widget_Win = WindowWidget(window)

window.mainloop()
