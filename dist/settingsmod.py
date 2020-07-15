import tkinter as tk

class Settings:

    def __init__(self,level_one):

        self.level_one = level_one
        self.level_one.title("Impostazioni - MailBot")
        self.level_one.resizable(False,False)
        self.level_one.geometry("300x400")
        self.level_one.config(bg="grey")
        
        tk.Label (level_one,text="Indirizzo mail").pack()
        self.address = tk.Entry(level_one,width=50)
        self.address.pack(pady=15)
        
        tk.Label(level_one,text="Password").pack()
        self.password = tk.Entry(level_one,width=50,show="*")
        self.password.pack()