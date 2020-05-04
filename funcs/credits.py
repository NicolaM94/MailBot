import tkinter as tk

class CreditsWindow:

    def __init__(self,level_one):
        self.level_one = level_one
        self.level_one.title ("Contatti - MailBot")
        self.level_one.geometry ("400x250")

        text = '''
        MailBot per l'invio di mail a contatti multipli.
        Creato da Nicola Moro, sotto licenza GNU.

        Per info,segnalazioni e contatti scrivere a:

        "nicola.moro@live.it"'''
        self.label = tk.Label(level_one,text=text).pack()

        self.exitbutton = tk.Button(level_one,bg="#033a91",text="Indietro",command=level_one.destroy).pack(pady=10)