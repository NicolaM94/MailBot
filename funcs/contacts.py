import tkinter as tk
import json

class ContactsWindow:
    
    def __init__(self,level_one):
        level_one.geometry("400x400")
        level_one.title("MailBot - Contatti")
        self.level_one = level_one

        with open("./bin/contacts.json") as file:
            reader = []
            try:
                reader = json.load(file)
            except:
                pass
        
        self.viewer = tk.Listbox(level_one)
        if len(reader) == 0:
            self.viewer.insert(tk.END,"Non hai contatti, aggiungine uno!")
        else:
            for name in reader:
                self.viewer.insert(tk.END,name)
        self.viewer.config()
        self.viewer.pack(side=tk.TOP,expand=.7,fill=tk.X)

        def new_contact_caller ():
                level_two = tk.Toplevel()
                engine_two = NewContactPopUp(level_two)
                level_two.mainloop()
        self.newcontact = tk.Button(level_one,bg="#033a91",text="Nuovo contatto",command=new_contact_caller).pack()

        self.backbutton = tk.Button(level_one,bg="#033a91",text="Indietro",command=level_one.destroy).pack()


class NewContactPopUp:

    def __init__(self,level_two):
        self.level_two = level_two
        level_two.title("MailBot - Nuovo Contatto")

        self.label = tk.Label(level_two,text="Nome contatto").grid(row=0,column=0)
        self.name_entry = tk.Entry(level_two,)
        self.name_entry.grid(row=0,column=1)

        self.address_label = tk.Label(level_two,text="Indirizzo").grid(row=1,column=0)
        self.address_entry = tk.Entry(level_two)
        self.address_entry.grid(row=1,column=1)

        def addcontact ():
            with open("./bin/contacts.json","r") as file:
                reader = json.load(file)
                scheda = {
                    "Nome":self.name_entry.get(),
                    "Indirizzo":self.address_entry.get()
                }
                reader.append(scheda)
                lista = []
                for dic in reader:
                    lista.append(dic["Nome"])
                print(reader)
            with open("./bin/contacts.json","w") as file:
                json.dump(reader,file,indent=4)
            level_two.destroy ()
        
        self.addcontactbutton = tk.Button(level_two,text="Aggiungi contatto",command=addcontact).grid(row=2,column=0,pady=10)
        self.backbutton = tk.Button(level_two,text="Indietro").grid(row=2,column=1,pady=10)