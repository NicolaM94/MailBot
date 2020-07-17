import tkinter as tk
import webbrowser
from dist.settingsmod import Settings
from dist.messagemod import Message

class MainBot:

    def __init__(self,master):
        self.master = master
        self.master.title("MailBot")
        self.master.resizable(False,False)
        self.master.geometry("500x275")
        

        def message_caller ():
            level_one = tk.Toplevel()
            Message (level_one)
            level_one.mainloop()
            

        def settings_caller ():
            level_one = tk.Tk()
            Settings (level_one)
            level_one.mainloop()
        
        def guide_caller ():
            webbrowser.open("https://github.com/NicolaM94/MailBot/blob/master/README.md")
                     
        
        tk.Button (master,text="Nuovo messaggio",width=30,command=message_caller).pack(pady=15)
        tk.Button (master,text="Impostazioni",width=30,command=settings_caller).pack(pady=15)
        tk.Button (master,text="Guida",width=30,command=guide_caller).pack(pady=15)
        tk.Button (master,text="Esci",width=30,command=engine.destroy).pack(pady=15)



if __name__ == "__main__":
    engine = tk.Tk()
    master = MainBot(engine)
    engine.mainloop()