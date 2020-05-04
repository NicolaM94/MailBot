import tkinter as tk 
from funcs.contacts import ContactsWindow
from funcs.credits import CreditsWindow
from funcs.settings import SettingsWindow

class MainWindow:
    def __init__(self,master):
        self.master = master
        self.master.geometry("400x300")
        self.master.title("Mailbot - Nicola Moro 2020 - v. 0.1")


        def contacts_caller ():
            level_one = tk.Toplevel()
            engine_one = ContactsWindow (level_one)
            level_one.mainloop()
        self.button = tk.Button(text="Contatti",bg="#033a91",command=contacts_caller).pack(pady=5)


        self.button = tk.Button(text="Scrivi messaggio",bg="#033a91").pack(pady=5)

        def settings_caller ():
            level_one = tk.Toplevel()
            engine_one = SettingsWindow (level_one)
            level_one.mainloop()
        self.settingsbutton = tk.Button(text="Impostazioni",bg="#033a91",command=settings_caller).pack(pady=5)


        def credits_caller ():
            level_one = tk.Toplevel()
            engine_one = CreditsWindow (level_one)
            level_one.mainloop()
        self.creditsbutton = tk.Button(text="Crediti e contatti",bg="#033a91",command = credits_caller).pack(pady=5)


        self.exitbutton = tk.Button(text="Esci",bg="red",command = master.destroy).pack(pady=5)


if __name__ == "__main__":
    master = tk.Tk()
    engine_zero = MainWindow(master)
    master.mainloop()