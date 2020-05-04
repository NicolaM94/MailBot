import tkinter as tk
from json import dump,load

class SettingsWindow:

    def __init__(self,level_one):
        level_one.geometry("300x400")
        level_one.title("Impostazioni - MailBot")
        level_one.resizable(False,False)
        self.level_one = level_one

        with open("./bin/settings.json","r") as file:
            reader = load(file)
            print(reader)
            for key in reader:
                if key != "Password":
                    string = key + ": " + reader[key]
                    tk.Label(level_one,text=string).pack()

        self.mail_label = tk.Label(level_one,text="Indirizzo mail").pack(pady=5)
        self.mail_entry = tk.Entry(level_one,)
        self.mail_entry.pack()

        self.pass_label = tk.Label(level_one,text="Password").pack()
        self.pass_entry = tk.Entry(level_one,show="*")
        self.pass_entry.pack()

        self.smtp_label = tk.Label(level_one,text="SMTP Server").pack()
        self.smtp_entry = tk.Entry(level_one)
        self.smtp_entry.pack()

        self.port_label = tk.Label(level_one,text="Porta del server").pack()
        self.port_entry = tk.Entry(level_one)
        self.port_entry.pack()

        def save_info_func ():
            with open("./bin/settings.json","w") as file:
                sheet = {
                    "Indirizzo" : self.mail_entry.get(),
                    "Password" : self.pass_entry.get(),
                    "SMTP Server" : self.smtp_entry.get(),
                    "Porta" : self.port_entry.get()
                }
                dump(sheet,file,indent=4)
            level_one.destroy()
        self.savebutton = tk.Button(level_one,bg="#033a91",text="Salva ed esci",command=save_info_func).pack(pady=10)

        self.backbutton = tk.Button(level_one,bg="#033a91",text="Indietro",command=level_one.destroy).pack()