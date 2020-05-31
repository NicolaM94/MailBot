import tkinter as tk
import json

class SettingsWindow :
    def __init__(self,level_one):
        self.level_one = level_one
        self.level_one.title ("RoboMail - Impostazioni")
        self.level_one.resizable(False,False)
        self.level_one.geometry("400x450")

        tk.Label(level_one,text="|----------------------------------------------|",height=1).pack()
        try:
            tk.Label(level_one,text="Impostazioni attuali",font="Helvetica 12 bold").pack()
            with open("./bin/account_settings.json") as file:
                reader = json.load(file)
                for key in reader:
                    if key != "Password":
                        printed_text = key + ":" + reader[key]
                        tk.Label(level_one,text=printed_text).pack()
                tk.Label(level_one,text="|----------------------------------------------|",height=2).pack()
        except:
            tk.Label(level_one,text="Non ci sono ancora impostazioni salvate").pack()
            tk.Label(level_one,text="|----------------------------------------------|",height=2).pack()
        

        tk.Label(level_one,text="Il tuo indirizzo mail:").pack()
        self.account = tk.Entry(level_one,width=30)
        self.account.pack()

        tk.Label(level_one,text="La tua password:").pack()
        self.password = tk.Entry(level_one,show="*",width=30)
        self.password.pack()

        tk.Label(level_one,text="Server SMTP:").pack()
        self.smtp_address = tk.Entry(level_one,width=30)
        self.smtp_address.pack()

        tk.Label(level_one,text="La porta del server SMTP:").pack()
        self.port =tk.Entry(level_one,width=5)
        self.port.pack()

        def savenexit_button_func():
            with open("./bin/account_settings.json","w") as file:
                sheet = {
                    "Indirizzo" : self.account.get(),
                    "Password" : self.password.get(),
                    "SMTP Server" : self.smtp_address.get(),
                    "Porta SMTP" : self.port.get()
                }
                json.dump(sheet,file,indent=4)
            level_one.destroy()
        self.savenexit_button = tk.Button(level_one,text="Salva ed esci",command = savenexit_button_func).pack(pady=15)
        self.exit_button = tk.Button(level_one,text="Esci senza salvare",command=level_one.destroy).pack()