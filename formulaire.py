from msilib.schema import RadioButton
import tkinter as tk  # python3
from tkinter import *
from tkinter import messagebox

TITLE_FONT = ("Helvetica", 40, "bold")

#----------------- classe principale----------------------
class Principal(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Accueil,Accueil):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("Accueil")
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

#------------------------------- page d'accueil --------------------------#
class Accueil(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg = "#87CEEB")
        title = Label(self, text="Formulaire de contact", bd=10, relief=GROOVE, font=("times new roman", 40, "bold"),
                      bg="#33B3FF", fg="#40FF33")
        title.pack(side=TOP, fill=X)
        #================All Variables=========================
        self.MATRICULE_var=StringVar()
        self.NOM_var=StringVar()
        self.PRENOM_var=StringVar()
        self.EMAIL_var=StringVar()
        self.GENRE_var=StringVar(self, " ")

        #==========manage frame=====================

        self.Manage_Frame=Frame(self,bd=4,relief=RIDGE,bg="#143685")
        self.Manage_Frame.place(x=45,y=135,width=550,height=500)


        m_title=Label(self.Manage_Frame,text="Renseignements",bg="#143685",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,padx=120, pady=20)

        lbl_Nom=Label(self.Manage_Frame,text="Nom : ",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Nom.grid(row=1,column=0,padx=50,pady=10,sticky="w")

        txt_Nom=Entry(self.Manage_Frame,textvariable=self.NOM_var,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE)
        txt_Nom.grid(row=1,column=1,padx=10,pady=10,sticky="w")

        lbl_Prenom=Label(self.Manage_Frame,text="Prenom : ",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Prenom.grid(row=2,column=0,padx=50,pady=10,sticky="w")

        txt_Prenom=Entry(self.Manage_Frame,textvariable=self.PRENOM_var,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE)
        txt_Prenom.grid(row=2,column=1,padx=10,pady=10,sticky="w")


        lbl_Matricule=Label(self.Manage_Frame,text="Matricule :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Matricule.grid(row=3,column=0,padx=50,pady=10,sticky="w")

        txt_Matricule=Entry(self.Manage_Frame,textvariable=self.MATRICULE_var,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE)
        txt_Matricule.grid(row=3,column=1,padx=10,pady=10,sticky="w")


        lbl_Email=Label(self.Manage_Frame,text="Email :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=4,column=0,padx=50,pady=10,sticky="w")

        txt_Email=Entry(self.Manage_Frame,textvariable=self.EMAIL_var,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=4,column=1,padx=10,pady=10,sticky="w")


        lbl_Genre=Label(self.Manage_Frame,text="Genre :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Genre.grid(row=5,column=0,padx=50,pady=10,sticky="w")

        self.values = {"Maxculin" : "Maxculin",
                "Feminin" : "Feminin"}

        i = 262
        for (text, value) in self.values.items():
            Radiobutton(self.Manage_Frame, text = text, variable = self.GENRE_var,
                value = value).place(x=i,y=335)
            i = i +100
#====================button Frame============
        btn_Frame=Frame(self.Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=65,y=400,width=420)

        Addbtn=Button(btn_Frame,text="Soumettre",width=10,font=("times new roman",15,"bold"), command = self.create).grid(row=0,column=0,padx=10,pady=10)

        Clearbtn=Button(btn_Frame,text="Effacer",width=10,font=("times new roman",15,"bold"),command=self.clear).grid(row=0,column=2,padx=120,pady=10)

    def clear(self):
            self.MATRICULE_var.set("")
            self.NOM_var.set("")
            self.PRENOM_var.set("")
            self.EMAIL_var.set("")
            self.GENRE_var.set(" ")
            

    def create(self):
        if (self.MATRICULE_var.get()=="" or self.NOM_var.get()=="" or self.PRENOM_var.get()==""):
            messagebox.showerror("error","saisir vos les informations")
        else:
            win = Toplevel(self)
            win.geometry("600x500")
            win.resizable(width=False, height=False)
            win.title('Formulaire de contact/fait par Issa olinga')
            title = Label(win, text= "Bienvenue!", font=("times new roman", 40, "bold"),
                        fg="#40FF33")
            title.grid(row=0,column=0,padx=200,pady=10,sticky="w")

            lbl_Emai = Label(win, text= f"VOS INFORMATION:",font=("times new roman",30,"bold"))
            lbl_Emai.grid(row=1,column=0,padx=150,pady=10,sticky="w")

            lbl_Emai1 = Label(win, text= f"Nom : {self.NOM_var.get()}" ,font=("times new roman",20,"bold"))
            lbl_Emai1.grid(row=2,column=0,padx=50,pady=10,sticky="w")

            lbl_Emai2 = Label(win, text= f"Prenom : {self.PRENOM_var.get()}" ,font=("times new roman",20,"bold"))
            lbl_Emai2.grid(row=3,column=0,padx=50,pady=10,sticky="w")

            lbl_Emai3 = Label(win, text= f"Matricule : {self.MATRICULE_var.get()}" ,font=("times new roman",20,"bold"))
            lbl_Emai3.grid(row=4,column=0,padx=50,pady=10,sticky="w")

            lbl_Emai4 = Label(win, text= f"Genre : {self.GENRE_var.get()}",font=("times new roman",20,"bold"))
            lbl_Emai4.grid(row=5,column=0,padx=50,pady=10,sticky="w")

            lbl_Emai5 = Label(win, text= "Merci d'avoir fait confiance à Procity" ,font=("times new roman",15,"bold"))
            lbl_Emai5.grid(row=6,column=0,padx=150,pady=10,sticky="w")

if __name__ == "__main__":
    app = Principal()
    app.geometry("650x800")
    app.resizable(width=False, height=False)
    app.title('Formulaire de contact/fait par Issa olinga')
    app.mainloop()
