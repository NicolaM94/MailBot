import tkinter as tk

class Message:
    
    def __init__(self,level_one):
        self.level_one = level_one
        self.level_one.resizable(False,False)
        self.level_one.geometry("600x600")
        self.level_one.title ("Nuovo messaggio - MailBot")


        tk.Label(level_one,text="Oggetto").pack(pady=5)
        self.subject = tk.Entry(level_one,width=70)
        self.subject.pack(pady=5)

        tk.Label(level_one,text="Messaggio").pack(pady=5)
        self.message = tk.Text(level_one)
        self.message.pack(padx=5,pady=5)