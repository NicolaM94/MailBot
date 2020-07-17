import tkinter as tk
from json import dump,load

class Settings:

    def __init__(self,level_one):

        self.level_one = level_one
        self.level_one.title("Impostazioni - MailBot")
        self.level_one.resizable(False,False)
        self.level_one.geometry("300x400")
        
        
        def settingssaver ():
            with open("saved_cache/settings.json","w") as file:
                to_dump = {
                    "Indirizzo" : self.address.get(),
                    "Password" : self.password.get(),
                    "Server SMTP" : self.smtpserver.get(),
                    "Porta SMTP" : self.port.get()
                }
                dump(to_dump,file,indent=4)
                level_one.destroy()

        try:
            with open("saved_cache/settings.json","r") as file:
                reader = load(file)
                for k in reader:
                    if k != "Password":
                        text_to_show = k + ": " + reader[k]
                        tk.Label(level_one,text=text_to_show).pack()
                tk.Label(level_one).pack(pady=10)
        except:
            tk.Label(level_one,text="Non hai ancora impostazioni salvate")
            tk.Label(level_one).pack(pady=10)


        tk.Label (level_one,text="Indirizzo mail").pack()
        self.address = tk.Entry(level_one,width=35)
        self.address.pack()
        
        tk.Label(level_one,text="Password").pack()
        self.password = tk.Entry(level_one,width=35,show="*")
        self.password.pack()

        tk.Label(level_one,text="SMTP Server").pack()
        self.smtpserver = tk.Entry(level_one,width=35)
        self.smtpserver.pack()

        tk.Label(level_one,text="Porta SMTP").pack()
        self.port = tk.Entry(level_one,width=5)
        self.port.pack()

        tk.Button(level_one,text="Salva ed esci",command=settingssaver).pack(pady=10)
        tk.Button(level_one,text="Esci senza salvare",command=level_one.destroy).pack(pady=10)