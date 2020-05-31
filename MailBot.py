'''This mailbot is a completely personal project by Nicola Moro, under the GNU licence made with Python3. All right for usage and referral are meant to be given to the producer'''

import tkinter as tk
import json
from dist.message_window import MessageWindow
from dist.contacts_window import ContactsWindow
from dist.settings_window import SettingsWindow
from dist.assistance_window import AssistanceWindow
import webbrowser

class MailBot:

    def __init__(self,master):
        self.master = master
        self.master.resizable(False,False)
        self.master.geometry("350x340")
        self.master.title("MailBot - Menù")

        def message_button_func ():
            subengine = tk.Toplevel()
            level_one = MessageWindow(subengine)
            subengine.mainloop()
        
        def contacts_button_func ():
            subengine = tk.Toplevel()
            level_one = ContactsWindow(subengine)
            subengine.mainloop()
        
        def settings_button_func ():
            subengine = tk.Toplevel()
            level_one = SettingsWindow(subengine)
            subengine.mainloop()
        
        def assistance_button_func():
            webbrowser.open("https://github.com/NicolaM94/Automail/blob/master/README.md")
        
        space_label = tk.Label().pack()
        self.message_button = tk.Button(text="Nuovo messaggio",height=2,width=15,command=message_button_func).pack(pady=5)
        self.contacts_button = tk.Button(text="Contatti",height=2,width=15,command=contacts_button_func).pack(pady=5)
        self.settings_button = tk.Button(text="Impostazioni",height=2,width=15,command=settings_button_func).pack(pady=5)
        self.assistance_button = tk.Button(text="Assistenza",height=2,width=15,command=assistance_button_func).pack(pady=5)
        self.exit_button = tk.Button(text="Esci",height=2,width=15,command=engine.destroy).pack(pady=5)
        end_space_label = tk.Label().pack()



if __name__ == "__main__":
    engine = tk.Tk()
    master = MailBot(engine)
    engine.mainloop()