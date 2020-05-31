import tkinter as tk
import json

class MessageWindow:
    def __init__(self,level_one):
        self.level_one = level_one
        level_one.geometry("500x625")
        level_one.title("RoboMail - Messaggio")
        level_one.resizable(False,False)

        tk.Label().pack()

        tk.Label(level_one,text="Oggetto del messaggio").pack()
        self.subject_entry = tk.Entry(level_one,width=50)
        self.subject_entry.pack()

        tk.Label(level_one,text="Corpo del messaggio").pack()
        self.message_entry = tk.Text(level_one,)
        self.message_entry.pack()

        tk.Label(level_one).pack()
        tk.Button(level_one,text="Invia",bg="red",width=15).pack(pady=2)

        def save_button ():
            with open("./bin/saved_message.json","w") as f:
                printer = {
                    "Subject" : self.subject_entry.get(),
                    "Message" : self.message_entry.get(1.0,"end-1c")
                }
                json.dump(printer,f,indent=4)
                level_one.destroy()
        tk.Button(level_one,text="Salva ed esci",width=15,command=save_button).pack(pady=2)

        tk.Button(level_one,text="Esci senza salvare",width=15,command=level_one.destroy).pack(pady=2)

