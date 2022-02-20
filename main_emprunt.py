from atexit import register
import imp
from json import load
from pydoc import apropos
from tkinter import ttk
import tkinter as tk  # python3
# import Tkinter as tk   # python
from tkinter import *
from turtle import back, color

import webbrowser
import mysql.connector
from tkinter import messagebox
import sqlite3
import imp

# from menu import *

TITLE_FONT = ("Helvetica", 40, "bold")


def main_top(self):
        menu_bar = Menu(self)
        def acceuil():
            self.show_frame("Accueil")
        def journal():
            webbrowser.open('https://ekiosque.cm/')
        # def journal():
        #     self.show_frame("Journal")
        #     win = Toplevel()
        #     win.geometry("600x500")
        #     win.resizable(width=False, height=False)
        #     win.title('Formulaire de contact/fait par Issa olinga')
        #     title = Label(win, text= "Bienvenue!", font=("times new roman", 40, "bold"),
        #                 fg="#40FF33")
        #     title.grid(row=0,column=0,padx=200,pady=10,sticky="w")
        def volune():
            self.show_frame("Volumes")

        def diction():
            webbrowser.open('https://www.larousse.fr/dictionnaires/francais-monolingue')
        def emprunt():
            self.show_frame("Emprunt")
        def livres():
            self.show_frame("Livres")
        def remise():
            self.show_frame("Remise")
        def enseignant():
            self.show_frame("Enseignant")
        def etudiant():
            self.show_frame("Etudiant")
        def renise():
            self.show_frame("Remise")
        def personnel():
            self.show_frame("Personnel")
        def aide():
            webbrowser.open('https://www.google.com/')

        # Création du cadre-conteneur pour les menus
        zoneMenu = Menu(self)
        menuDeroulant = Menu(zoneMenu,tearoff=0)

        menuDeroulant_planification = Menu(menuDeroulant ,tearoff=0)
        menuDeroulant.add_cascade(label="Volune" ,menu=menuDeroulant_planification)
        menuDeroulant_planification.add_command(label="Emprunt de Livres", command=emprunt )
        menuDeroulant_planification.add_command(label="consulter les Dictionnaires", command= diction)
        menuDeroulant.add_separator()
        menuDeroulant.add_command(label="consulter les Journaux", command= journal)
        
        
        menuDeroulant0 = Menu(zoneMenu,tearoff=0)
        menuDeroulant0.add_command(label="Acceuil", command= acceuil)
        menuDeroulant0.add_command(label="Aide", command= aide)
        menuDeroulant0.add_separator()
        menuDeroulant0.add_command(label="Quiter", command=self.quit)


        menuDeroulant2 = Menu(zoneMenu ,tearoff=0)

        menuDeroulant_planification = Menu(menuDeroulant2 ,tearoff=0)
        menuDeroulant2.add_cascade(label="Volume" ,menu=menuDeroulant_planification)
        menuDeroulant_planification.add_command(label="Livres", command= livres)
        menuDeroulant_planification.add_command(label="Dictionnaire", command= diction)
        menuDeroulant2.add_separator()
        menuDeroulant2.add_command(label="Journaux", command= journal)
        
        menuDeroulant3 = Menu(zoneMenu ,tearoff=0)
        menuDeroulant3.add_command(label="Liste des étudiants et adhérants", command= etudiant)
        menuDeroulant3.add_command(label="Liste des livres empruntés", command= remise)


        #  creation des élément du menu
        zoneMenu.add_cascade(label="Fichier ", menu=menuDeroulant0)
        zoneMenu.add_cascade(label="Documents ", menu=menuDeroulant2)
        zoneMenu.add_cascade(label="Gestion des Emprunts ", menu=menuDeroulant)
        zoneMenu.add_cascade(label="Rapport et Statistiques ", menu=menuDeroulant3)
        # afficharge du menu
        self.configure(menu=zoneMenu)
#----------------- classe principale----------------------
class Principal(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

       #importation du module des menus
        main_top(self)
        
        self.frames = {}
        for F in (Accueil, Emprunt, Etudiant,Remise, Livres):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
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
        self.config(bg = "#5F9EA0")
        title = Label(self, text="Gestion de la bibliothèque", bd=10, relief=GROOVE, font=("times new roman", 40, "bold"),
                      bg="#8A2BE2", fg="#40FF33")
        title.pack(side=TOP, fill=X)

        #==========manage frame=====================

        self.Manage_Frame=Frame(self,bd=4,relief=RIDGE,bg="#143685")
        self.Manage_Frame.place(x=390,y=100,width=550,height=500)

        m_title=Label(self.Manage_Frame,text="Gestion d'Emprunt \n des Livres",bg="#143685",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,padx=120, pady=20)

#====================button Frame============
        btn_Frame=Frame(self.Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=65,y=150,width=420)

        Addbtn=Button(btn_Frame,text="Adhérants",width=10,command=lambda: controller.show_frame("Etudiant"),font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10)

        Clearbtn=Button(btn_Frame,text="Emprunts",width=10,command=lambda: controller.show_frame("Emprunt"),font=("times new roman",15,"bold")).grid(row=0,column=2,padx=120,pady=10)
#====================button Frame============
        btn_Frame=Frame(self.Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=65,y=280,width=420)
        def dicti():
            webbrowser.open('https://www.larousse.fr/dictionnaires/francais-monolingue')
        Addbtn=Button(btn_Frame,text="Consulter les Journaux/Dictionnaires",command= dicti,width=33,font=("times new roman",15,"bold")).grid(padx=3)
#====================button Frame============
        btn_Frame=Frame(self.Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=65,y=400,width=420)

        Addbtn=Button(btn_Frame,text="Listes des livres",width=10,command=lambda: controller.show_frame("Livres"),font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10)

        Clearbtn=Button(btn_Frame,text="Remise",width=10,command=lambda: controller.show_frame("Remise"),font=("times new roman",15,"bold")).grid(row=0,column=2,padx=120,pady=10)



#------------------------------- la gestion des fenetres des differents modules ------------------------------------------------#

class Livres(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg = "#87CEEB")
        
        title=Label(self,text="Gestion des livres",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#8A2BE2",fg="#40FF33")
        title.pack(side=TOP,fill=X) 


        #================All Variables=========================
        self.TITRE=StringVar()
        self.AUTEUR=StringVar()
        self.EDIT=StringVar()
        self.LANGUE=StringVar()
        self.Nbr=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()



        #==========manage frame=====================

        Manage_Frame=Frame(self,bd=4,relief=RIDGE,bg="#143685")
        Manage_Frame.place(x=20,y=100,width=475,height=490)

        m_title=Label(Manage_Frame,text="Enrégistrer \n un livre",bg="#143685",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_adh=Label(Manage_Frame,text="Titre :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_adh.grid(row=1,column=0,padx=20,pady=10,sticky="w")

        txt_adh=Entry(Manage_Frame,textvariable=self.TITRE,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE)
        txt_adh.grid(row=1,column=1,padx=2,pady=10,sticky="w")


        lbl_Matricule=Label(Manage_Frame,text="Auteur :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Matricule.grid(row=2,column=0,padx=20,pady=10,sticky="w")

        txt_Matricule=Entry(Manage_Frame,textvariable=self.AUTEUR,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE)
        txt_Matricule.grid(row=2,column=1,padx=2,pady=10,sticky="w")

        lbl_Nom=Label(Manage_Frame,text="Edition :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Nom.grid(row=3,column=0,padx=20,pady=10,sticky="w")

        txt_Nom=Entry(Manage_Frame,textvariable=self.EDIT,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE)
        txt_Nom.grid(row=3,column=1,padx=2,pady=10,sticky="w")

        lbl_Faculte=Label(Manage_Frame,text="Langue :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Faculte.grid(row=4,column=0,padx=20,pady=10,sticky="w")

        combo_Faculte=ttk.Combobox(Manage_Frame,textvariable=self.LANGUE,font=("times new roman",14,"bold"),state='readonly')
        combo_Faculte['values']=("Francaise","Anglaise","Chinoise","Latin","Greque","Autres")
        combo_Faculte.grid(row=4,column=1,pady=10,padx=0,sticky="w")

#====================button Frame============
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=10,y=400,width=420)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_etudiants).grid(row=0,column=0,padx=10,pady=10)
        updbtn=Button(btn_Frame,text="Update",width=10,command=self.update_date).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

#==========detail frame=====================
        Detail_Frame=Frame(self,bd=4,relief=RIDGE,bg="#143685")
        Detail_Frame.place(x=500,y=100,width=750,height=580)


        lbl_search=Label(Detail_Frame,text="Recherche",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("langue","edition","titre")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new rolan",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,padx=20,pady=10,sticky="w")

        searchbtn=Button(Detail_Frame,text="OK",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Retour",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

#=========Table Frame=====================
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#ED33FF")
        Table_Frame.place(x=10,y=70,width=720,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.livres_table=ttk.Treeview(Table_Frame,columns=("nbr","titre","auteur","edition","langue"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.livres_table.xview)
        scroll_y.config(command=self.livres_table.yview) 
        self.livres_table.heading("nbr",text="Nbr") 
        self.livres_table.heading("titre",text="Titre")
        self.livres_table.heading("auteur",text="Ateur")
        self.livres_table.heading("edition",text="Edition")
        self.livres_table.heading("langue",text="Langue")
        # self.Etudiants_table.heading("niveau",text="Niveau")
        # self.Etudiants_table.heading("photo",text="photo")
        # self.Etudiants_table.heading("address",text="address")
        self.livres_table['show']='headings'
        self.livres_table.column("nbr",width=50)
        self.livres_table.column("titre",width=125)
        self.livres_table.column("auteur",width=125)
        self.livres_table.column("edition",width=70)
        self.livres_table.column("langue",width=50)
        # self.Etudiants_table.column("photo",width=150)
        # self.Etudiants_table.column("address",width=150)
        self.livres_table.pack(fill=BOTH,expand=1)
        self.livres_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data() 

    def add_etudiants(self):
        if self.TITRE.get()=="" or self.AUTEUR.get()=="" or self.LANGUE.get()=="":
                messagebox.showerror("Error","remplir tous les champs!!!")
        else:
                try:
                        connexion = sqlite3.connect("Emprunt_livres.db")
                        #création du curser
                        curseur = connexion.cursor()
                        #Exécution unique 
                        # CREATE TABLE IF NOT EXISTS membres(IMARY KEY, pseudo TEXT NOT NULL,ordre INTEGER AUTO_INCREMENT, date_register DATETIME, classe INTEGER, statut INTEGER);
                        curseur.execute('''CREATE TABLE IF NOT EXISTS livres_pro(tailte TEXT PRIMARY KEY, Auteur TEXT, Edit TEXT, Langue TEXT)''')
                        
                        curseur.execute("insert into livres_pro (tailte,Auteur,Edit,Langue) values (?,?,?,?)",(
                                                                                                self.TITRE.get(),
                                                                                                self.AUTEUR.get(),
                                                                                                self.EDIT.get(),
                                                                                                self.LANGUE.get()
                                                                                                ))               
                        connexion.commit()
                        self.fetch_data()
                        self.clear()
                        curseur.close()
                        messagebox.showinfo("Success","Le livre est enrégistré")
                except Exception as es:
                        messagebox.showerror('error',f'error due to : {str(es)}', parent = self)

    def fetch_data(self):
        connexion = sqlite3.connect("Emprunt_livres.db")
        curse = connexion.cursor()
        curse.execute('''CREATE TABLE IF NOT EXISTS livres_pro(tailte TEXT PRIMARY KEY, Auteur TEXT, Edit TEXT, Langue TEXT)''')
                # ("Table score crée")
        sql = "SELECT * FROM livres_pro"
        curse.execute(sql)
        row=curse.fetchall()
        if len(row)!=0:
                self.livres_table.delete(*self.livres_table.get_children())
                for row in row:
                        self.livres_table.insert('',END,values=row)
                connexion.commit()
        connexion.close()

    def clear(self):
            self.TITRE.set("")
            self.AUTEUR.set("")
            self.EDIT.set("")
            self.LANGUE.set("")

    def get_cursor(self,ev):
            curosor_row = self.livres_table.focus()
            contents= self.livres_table.item(curosor_row)
            row=contents['values']
            (row)
            self.TITRE.set(row[1])
            self.AUTEUR.set(row[2])
            self.EDIT.set(row[3])
            self.LANGUE.set(row[4])

    def update_date(self):
            try:   
                connexion = sqlite3.connect("Emprunt_livres.db")
                cur = connexion.cursor()
                cur.execute('''CREATE TABLE IF NOT EXISTS livres_pro(tailte TEXT PRIMARY KEY, Auteur TEXT, Edit TEXT, Langue TEXT)''')
                        # ("Table score crée")
                cur.execute("update livres_pro set tailte=?,Auteur=?,Edit=?,Langue=? where tailte=?",(
                                                                                        self.TITRE.get(),
                                                                                        self.AUTEUR.get(),
                                                                                        self.EDIT.get(),
                                                                                        self.LANGUE.get(),
                                                                                        self.TITRE.get()
                                                                                        ))    
                connexion.commit()
                self.fetch_data()
                self.clear()
                cur.close()
            except Exception as es:
                messagebox.showerror('error',f'error due to : {str(es)}', parent = self)
    def delete_data(self):
            connexion = sqlite3.connect("Emprunt_livres.db")
            cur = connexion.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS livres_pro(tailte TEXT PRIMARY KEY, Auteur TEXT, Edit TEXT, Langue TEXT)''')
                        # ("Table score crée")
            sql = "DELETE FROM livres_pro WHERE tailte = ? "
            cur.execute(sql, (self.TITRE.get(),))

            connexion.commit()
            self.fetch_data()
            self.clear()
            cur.close()

    def search_data(self):
            connexion = sqlite3.connect("Emprunt_livres.db")
            cur = connexion.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS livres_pro(tailte TEXT PRIMARY KEY, Auteur TEXT, Edit TEXT, Langue TEXT)''')
            if self.search_by.get()== 'langue':
                    sql = "select * FROM livres_pro WHERE Langue = ? "
                    cur.execute(sql, (self.search_txt.get(),))

                    rows=cur.fetchall()
                    if len(rows)!=0:
                            self.livres_table.delete(*self.livres_table.get_children())
                            for row in rows:
                                    self.livres_table.insert('',END,values=row)
                            connexion.commit()  
                    connexion.close()
            elif self.search_by.get()== 'edition':
                    sql = "select * FROM livres_pro WHERE Edit = ? "
                    cur.execute(sql, (self.search_txt.get(),))
                    rows=cur.fetchall()
                    if len(rows)!=0:
                            self.livres_table.delete(*self.livres_table.get_children())
                            for row in rows:
                                    self.livres_table.insert('',END,values=row)
                            connexion.commit()  
                    connexion.close()
            elif self.search_by.get()== 'titre':
                    sql = "select * FROM livres_pro WHERE tailte = ? "
                    cur.execute(sql, (self.search_txt.get(),))
                    rows=cur.fetchall()
                    if len(rows)!=0:
                            self.livres_table.delete(*self.livres_table.get_children())
                            for row in rows:
                                    self.livres_table.insert('',END,values=row)
                            connexion.commit()  
                    connexion.close()
            else:
                   messagebox.showinfo("Ivalide","Renseigner le champ")

class Emprunt(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg = "#87CEEB")
        title=Label(self,text="Gestion des Emprunts",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#8A2BE2",fg="#40FF33")
        title.pack(side=TOP,fill=X) 

        #================All Variables=========================
        self.CODE=StringVar()
        self.TITRE=StringVar()
        self.NON_USER=StringVar()
        self.DATE1=StringVar()
        self.DATE2=StringVar()
        self.AUTEUR=StringVar()

        self.filename_var = StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        #==========manage frame=====================

        Manage_Frame=Frame(self,bd=4,relief=RIDGE,bg="#143685")
        Manage_Frame.place(x=20,y=100,width=475,height=580)

        m_title=Label(Manage_Frame,text="Enrégistrement \n un emprunts de livre",bg="#143685",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_adh=Label(Manage_Frame,text="Code d'emprunt :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_adh.grid(row=1,column=0,padx=20,pady=10,sticky="w")

        txt_adh=Entry(Manage_Frame,textvariable=self.CODE,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE)
        txt_adh.grid(row=1,column=1,padx=2,pady=10,sticky="w")


        lbl_Matricule=Label(Manage_Frame,text="Titre du livres :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Matricule.grid(row=2,column=0,padx=20,pady=10,sticky="w")

        txt_Matricule=Entry(Manage_Frame,textvariable=self.TITRE,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE)
        txt_Matricule.grid(row=2,column=1,padx=2,pady=10,sticky="w")

        lbl_Nom=Label(Manage_Frame,text="Matricule :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Nom.grid(row=3,column=0,padx=20,pady=10,sticky="w")

        txt_Nom=Entry(Manage_Frame,textvariable=self.AUTEUR,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE)
        txt_Nom.grid(row=3,column=1,padx=2,pady=10,sticky="w")

        lbl_Faculte=Label(Manage_Frame,text="Nom :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Faculte.grid(row=4,column=0,padx=20,pady=10,sticky="w")

        txt_Nom=Entry(Manage_Frame,textvariable=self.NON_USER,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE)
        txt_Nom.grid(row=4,column=1,pady=10,padx=0,sticky="w")

        lbl_Facul=Label(Manage_Frame,text="Date emprunt :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Facul.grid(row=5,column=0,padx=10,pady=10,sticky="w")

        txt_No=Entry(Manage_Frame,textvariable=self.DATE1,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE)
        txt_No.grid(row=5,column=1,padx=2,pady=10,sticky="w")

        lbl_niveau=Label(Manage_Frame,text="Date de remise :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_niveau.grid(row=6,column=0,padx=20,pady=10,sticky="w")

        txt_contact=Entry(Manage_Frame,textvariable=self.DATE2,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=6,column=1,padx=2,pady=10,sticky="w")

#====================button Frame============
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=10,y=500,width=420)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_etudiants).grid(row=0,column=0,padx=10,pady=10)
        updbtn=Button(btn_Frame,text="Update",width=10,command=self.update_date).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

#==========detail frame=====================
        Detail_Frame=Frame(self,bd=4,relief=RIDGE,bg="#143685")
        Detail_Frame.place(x=500,y=100,width=750,height=580)

        lbl_search=Label(Detail_Frame,text="Recherche",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("code","matricule","titre","date emprunt","date remise")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new rolan",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,padx=20,pady=10,sticky="w")

        searchbtn=Button(Detail_Frame,text="OK",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Retour/Actualiser",width=15,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

#=========Table Frame=====================
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#ED33FF")
        Table_Frame.place(x=10,y=70,width=720,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Emprunts_table=ttk.Treeview(Table_Frame,columns=("code emprunt","titre livre","matricule","nom user","date de prise","date de remise"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Emprunts_table.xview)
        scroll_y.config(command=self.Emprunts_table.yview)  
        self.Emprunts_table.heading("code emprunt",text="Code")
        self.Emprunts_table.heading("titre livre",text="Titre du livre")
        self.Emprunts_table.heading("matricule",text="Matricule")
        self.Emprunts_table.heading("nom user",text="Nom")
        self.Emprunts_table.heading("date de prise",text="Date de emprunt")
        self.Emprunts_table.heading("date de remise",text="Date de remise")
        # self.Etudiants_table.heading("photo",text="photo")
        # self.Etudiants_table.heading("address",text="address")
        self.Emprunts_table['show']='headings'
        self.Emprunts_table.column("code emprunt",width=40)
        self.Emprunts_table.column("titre livre",width=135)
        self.Emprunts_table.column("matricule",width=50)
        self.Emprunts_table.column("nom user",width=125)
        self.Emprunts_table.column("date de prise",width=100)
        self.Emprunts_table.column("date de remise",width=100)
        # self.Etudiants_table.column("photo",width=150)
        # self.Etudiants_table.column("address",width=150)
        self.Emprunts_table.pack(fill=BOTH,expand=1)
        self.Emprunts_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data() 
    def add_etudiants(self):
        if self.CODE.get()=="" or self.TITRE.get()=="" or self.NON_USER.get()=="" or self.DATE1.get()=="" or self.DATE2.get()=="":
                messagebox.showerror("Error","Renseigner les champs !!!")
        else:
                connexion = sqlite3.connect("Emprunt_livres.db")


                CUR_Test = connexion.cursor()
                CUR_Test.execute('''CREATE TABLE IF NOT EXISTS livres_pro(IMARY KEY, tailte TEXT, Auteur TEXT, Edit TEXT, Langue TEXT)''')
                            # ("Table score crée")
                CUR_Test.execute("SELECT tailte FROM livres_pro WHERE tailte = ? GROUP BY tailte ", (self.TITRE.get(),)) 
                # (CUR_Test.fetchone())
                y = 0 
                while True :
                    kfich = CUR_Test.fetchone ( )
                    if kfich == None :   
                        break
                    else :
                        sv = kfich
                        ex = sv[0]
                        y = 1
                (y)

                CUR_Testt = connexion.cursor()
                CUR_Testt.execute('''CREATE TABLE IF NOT EXISTS emprunts(code INTEGER PRIMARY KEY, Titre TEXT, matricule INTEGER, nom TEXT, date1 INTEGER, date2 INTEGER)''')
                            # ("Table score crée")
                CUR_Testt.execute("SELECT COUNT(matricule), Titre FROM emprunts WHERE matricule = ? ", (self.AUTEUR.get(),)) 
                # (CUR_Test.fetchone())

                while True :
                    kfiche = CUR_Testt.fetchone ( )
                    if kfiche == None :
                        break
                    else :
                        s = kfiche
                        x = s[0]

                if (x < 3 and y == 1):
                    try:
                        connexion = sqlite3.connect("Emprunt_livres.db")
                        curr = connexion.cursor()
                        curr.execute('''CREATE TABLE IF NOT EXISTS emprunts(code INTEGER PRIMARY KEY, Titre TEXT, matricule INTEGER, nom TEXT, date1 INTEGER, date2 INTEGER)''')
                        
                        curr.execute("insert into emprunts (code,Titre,matricule,nom,date1,date2) values(?,?,?,?,?,?)",(self.CODE.get(),
                                                                                        self.TITRE.get(),
                                                                                        self.AUTEUR.get(),
                                                                                        self.NON_USER.get(),
                                                                                        self.DATE1.get(),
                                                                                        self.DATE2.get()
                                                                                        ))
                        connexion.commit()
                        self.fetch_data()
                        self.clear()
                        curr.close()
                        messagebox.showinfo("Success","emprunt bien enrégistré")
                    except Exception as es:
                        messagebox.showerror('error',f'error due to : {str(es)}', parent = self)
                        
                else:
                        if(y == 0):
                                messagebox.showerror("Error","le livre n'existe pas dans la bibliothèque")
                        else:
                                messagebox.showerror("Error",f"vous avez déjà emprunter {x} livres \n le cota max est de 3 livres\n vous ne pouvez plus emprunter !!!")


    def fetch_data(self):
                connexion = sqlite3.connect("Emprunt_livres.db")
                cur = connexion.cursor()
                cur.execute('''CREATE TABLE IF NOT EXISTS emprunts(code INTEGER PRIMARY KEY, Titre TEXT, matricule INTEGER, nom TEXT, date1 INTEGER, date2 INTEGER)''')
                            # ("Table score crée")
                cur.execute("select * from emprunts")
                rows=cur.fetchall()
                if len(rows)!=0:
                        self.Emprunts_table.delete(*self.Emprunts_table.get_children())
                        for row in rows:
                                self.Emprunts_table.insert('',END,values=row)
                        connexion.commit()
                connexion.close()
    def clear(self):
            self.CODE.set("")
            self.TITRE.set("")
            self.AUTEUR.set("")
            self.NON_USER.set("")
            self.DATE1.set("")
            self.DATE2.set("")

    def get_cursor(self,ev):
            curosor_row = self.Emprunts_table.focus()
            contents= self.Emprunts_table.item(curosor_row)
            row=contents['values']
            (row)
            self.CODE.set(row[0])
            self.TITRE.set(row[1])
            self.AUTEUR.set(row[2])
            self.NON_USER.set(row[3])
            self.DATE1.set(row[4])
            self.DATE2.set(row[5])
            # self.txt_Address.delete("1.0",END)
            # self.txt_Address.insert(END,row[6]) 
    def update_date(self):
            try:   
                connexion = sqlite3.connect("Emprunt_livres.db")
                cur = connexion.cursor()
                cur.execute('''CREATE TABLE IF NOT EXISTS emprunts(code INTEGER PRIMARY KEY, Titre TEXT, matricule INTEGER, nom TEXT, date1 INTEGER, date2 INTEGER)''')
                                # ("Table score crée")
                cur.execute("update emprunts set Titre=?, matricule=?,nom=?,date1=?,date2=?  where code=?",(
                                                                                        self.TITRE.get(),
                                                                                        self.AUTEUR.get(),
                                                                                        self.NON_USER.get(),
                                                                                        self.DATE1.get(),
                                                                                        self.DATE2.get(),
                                                                                        self.CODE.get()
                                                                                ))
                connexion.commit()
                self.fetch_data()
                self.clear()
                cur.close()
            except Exception as es:
                messagebox.showerror('error',f'error due to : {str(es)}', parent = self)
    def delete_data(self):
            connexion = sqlite3.connect("Emprunt_livres.db")
            cur = connexion.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS emprunts(code INTEGER PRIMARY KEY, Titre TEXT, matricule INTEGER, nom TEXT, date1 INTEGER, date2 INTEGER)''')
                            # ("Table score crée")

            sql = "DELETE FROM emprunts WHERE code = ? "
            cur.execute(sql, (self.CODE.get(),))

            connexion.commit()
            self.fetch_data()
            self.clear()
            cur.close()
    def search_data(self):
            connexion = sqlite3.connect("Emprunt_livres.db")
            cur = connexion.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS emprunts(code INTEGER PRIMARY KEY, Titre TEXT, matricule INTEGER, nom TEXT, date1 INTEGER, date2 INTEGER)''')

            if self.search_by.get()== 'matricule':
                    sql = "select * FROM emprunts WHERE matricule = ? "
                    cur.execute(sql, (self.search_txt.get(),))
                    rows=cur.fetchall()
                    if len(rows)!=0:
                            self.Emprunts_table.delete(*self.Emprunts_table.get_children())
                            for row in rows:
                                    self.Emprunts_table.insert('',END,values=row)
                            connexion.commit()  
                    connexion.close()
            elif self.search_by.get()== 'code':
                    sql = "select * FROM emprunts WHERE code = ? "
                    cur.execute(sql, (self.search_txt.get(),))
                    rows=cur.fetchall()
                    if len(rows)!=0:
                            self.Emprunts_table.delete(*self.Emprunts_table.get_children())
                            for row in rows:
                                    self.Emprunts_table.insert('',END,values=row)
                            connexion.commit()  
                    connexion.close()
            elif self.search_by.get()== 'titre':
                    sql = "select * FROM emprunts WHERE Titre = ? "
                    cur.execute(sql, (self.search_txt.get(),))
                    rows=cur.fetchall()
                    if len(rows)!=0:
                            self.Emprunts_table.delete(*self.Emprunts_table.get_children())
                            for row in rows:
                                    self.Emprunts_table.insert('',END,values=row)
                            connexion.commit()  
                    connexion.close()
            elif self.search_by.get()== 'date emprunt':
                    sql = "select * FROM emprunts WHERE date1 = ? "
                    cur.execute(sql, (self.search_txt.get(),))
                    rows=cur.fetchall()
                    if len(rows)!=0:
                            self.Emprunts_table.delete(*self.Emprunts_table.get_children())
                            for row in rows:
                                    self.Emprunts_table.insert('',END,values=row)
                            connexion.commit()  
                    connexion.close()
            elif self.search_by.get()== 'date remise':
                    sql = "select * FROM emprunts WHERE date2 = ? "
                    cur.execute(sql, (self.search_txt.get(),))

                    rows=cur.fetchall()
                    if len(rows)!=0:
                            self.Emprunts_table.delete(*self.Emprunts_table.get_children())
                            for row in rows:
                                    self.Emprunts_table.insert('',END,values=row)
                            connexion.commit()  
                    connexion.close()
            else:
                    pass

class Remise(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg = "#87CEEB")
        title = Label(self, text="Gestion des Emprunts et Remises des livres", bd=10, relief=GROOVE, font=("times new roman", 40, "bold"),
                      bg="#8A2BE2", fg="#40FF33")
        title.pack(side=TOP, fill=X)

        #================All Variables=========================
        self.CODE=StringVar()
        self.TITRE=StringVar()
        self.NON_USER=StringVar()
        self.DATE1=StringVar()
        self.nb=StringVar()
        self.DATE2=StringVar()
        self.AUTEUR=StringVar()

        self.filename_var = StringVar()
        # self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt_mt=StringVar()
        self.search_txt_code=StringVar()
        self.search_txt=StringVar()


#==========detail frame=====================
        Detail_Frame=Frame(self,bd=4,relief=RIDGE,bg="#143685")
        Detail_Frame.place(x=17,y=100,width=1250,height=580)


        lbl_search=Label(Detail_Frame,text="Recherche/Rendre",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=23,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=17,font=("times new roman",20,"bold"),state='readonly')
        combo_search['values']=("livres emprunter","remettre")
        combo_search.grid(row=0,column=1,padx=30,pady=10)

        lbl_search=Label(Detail_Frame,text="Mt",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=2,pady=10,padx=5,sticky="w")

        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt_mt,width=10,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE,state='readonly')
        txt_Search.grid(row=0,column=3,padx=10,pady=10,sticky="w")

        lbl_search=Label(Detail_Frame,text="code",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=4,pady=10,padx=2,sticky="w")

        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt_code,width=10,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE,state='readonly')
        txt_Search.grid(row=0,column=5,padx=10,pady=10,sticky="w")

        searchbtn=Button(Detail_Frame,text="OK",width=10,pady=5,command=self.search_data).grid(row=0,column=6,padx=20,pady=10)
        # showallbtn=Button(Detail_Frame,text="Retour",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=20,pady=10)
        showallbtn=Button(Detail_Frame,text="Actualiser",width=10,pady=5,command=self.fetch_data).grid(row=0,column=7,padx=20,pady=10)
        # showallbtn=Button(Detail_Frame,text="Remetre",width=10,pady=5,command=self.fetch_data).grid(row=0,column=5,padx=20,pady=10)

#=========Table Frame=====================
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#ED33FF")
        Table_Frame.place(x=10,y=70,width=1220,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Emprunt_table=ttk.Treeview(Table_Frame,columns=("titre livre","auteur","edition","langue","code emprunt","nb","date de prise","date de remise"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Emprunt_table.xview)
        scroll_y.config(command=self.Emprunt_table.yview)
        self.Emprunt_table.heading("titre livre",text="Titre du livre")
        self.Emprunt_table.heading("auteur",text="Auteur")  
        self.Emprunt_table.heading("edition",text="Edition")
        self.Emprunt_table.heading("langue",text="Langue")
        self.Emprunt_table.heading("code emprunt",text="code emprunt")
        self.Emprunt_table.heading("nb",text="Matricule")
        # self.Emprunts_table.heading("nom user",text="Nom")
        self.Emprunt_table.heading("date de prise",text="Date de emprunt")
        self.Emprunt_table.heading("date de remise",text="Date de remise")
        # self.Etudiants_table.heading("photo",text="photo")
        # self.Etudiants_table.heading("address",text="address")
        self.Emprunt_table['show']='headings'
        self.Emprunt_table.column("titre livre",width=140)
        self.Emprunt_table.column("auteur",width=60)
        self.Emprunt_table.column("edition",width=45)
        self.Emprunt_table.column("langue",width=50)
        self.Emprunt_table.column("code emprunt",width=55)
        self.Emprunt_table.column("nb",width=15)
        # self.Emprunts_table.column("nom user",width=125)
        self.Emprunt_table.column("date de prise",width=100)
        self.Emprunt_table.column("date de remise",width=100)
        # self.Etudiants_table.column("photo",width=150)
        # self.Etudiants_table.column("address",width=150)
        self.Emprunt_table.pack(fill=BOTH,expand=1)
        self.Emprunt_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data() 
    def fetch_data(self):

        connexion = sqlite3.connect("Emprunt_livres.db")
        CUR_Test = connexion.cursor()
                # CREATE TABLE IF NOT EXISTS membres(IMARY KEY, pseudo TEXT NOT NULL,ordre INTEGER AUTO_INCREMENT, date_register DATETIME, classe INTEGER, statut INTEGER);
        CUR_Test.execute('''CREATE TABLE IF NOT EXISTS livres_pro(IMARY KEY, tailte TEXT, Auteur TEXT, Edit TEXT, Langue TEXT)''')
                # ("Table score crée")
        CUR_Test.execute('''CREATE TABLE IF NOT EXISTS emprunts(code INTEGER PRIMARY KEY, Titre TEXT, matricule INTEGER, nom TEXT, date1 INTEGER, date2 INTEGER)''')
                            # ("Table score crée")
        # CUR_Test.execute("SELECT  id,Auteur,Edit,Langue, code, date1, date2 FROM livres, emprunts WHERE livres.Titre= emprunts.Titre ")

        #Retrieving data
        sql = "SELECT  tailte,Auteur,Edit,Langue,code,matricule,date1,date2 FROM livres_pro INNER JOIN emprunts ON livres_pro.tailte= emprunts.Titre ORDER BY matricule "
        #Executing the query
        CUR_Test.execute(sql)

        rows=CUR_Test.fetchall()
        if len(rows)!=0:
            self.Emprunt_table.delete(*self.Emprunt_table.get_children())
            for row in rows:
                self.Emprunt_table.insert('',END,values=row)
            connexion.commit()
        connexion.close()
        self.search_txt_code.set("")
        self.search_txt_mt.set("")
        self.search_by.set("")


    def get_cursor(self,ev):
            curosor_row = self.Emprunt_table.focus()
            contents= self.Emprunt_table.item(curosor_row)
            row=contents['values']
            (row)
            self.TITRE.set(row[0])
            self.CODE.set(row[4])
            self.NON_USER.set(row[5])
            self.DATE1.set(row[6])
            self.DATE2.set(row[7])
            self.search_txt_code.set(row[4])
            self.search_txt_mt.set(row[5])
 
    def search_data(self):
        connexion = sqlite3.connect("Emprunt_livres.db")
        cur = connexion.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS emprunts(code INTEGER PRIMARY KEY, Titre TEXT, matricule INTEGER, nom TEXT, date1 INTEGER, date2 INTEGER)''')
                           

        cur.execute('''CREATE TABLE IF NOT EXISTS livres_pro(IMARY KEY, tailte TEXT, Auteur TEXT, Edit TEXT, Langue TEXT)''')

        if self.search_by.get()== 'livres emprunter':
                sql = "SELECT  tailte,Auteur,Edit,Langue FROM livres_pro INNER JOIN emprunts ON livres_pro.tailte= emprunts.Titre GROUP BY tailte, Auteur, Edit, Langue "
                cur.execute(sql)           
                rows=cur.fetchall()
                if len(rows)!=0:
                        self.Emprunt_table.delete(*self.Emprunt_table.get_children())
                        for row in rows:
                                self.Emprunt_table.insert('',END,values=row)
                        connexion.commit()
                connexion.close()
                self.search_txt_code.set("")
                self.search_txt_mt.set("")
        elif self.search_by.get()== 'remettre':

                if (self.CODE.get() != ""):
  
                        connexion = sqlite3.connect("Emprunt_livres.db")
                        cur = connexion.cursor()
                        cur.execute('''CREATE TABLE IF NOT EXISTS emprunts(code INTEGER PRIMARY KEY, Titre TEXT, matricule INTEGER, nom TEXT, date1 INTEGER, date2 INTEGER)''')
                                        
                        cur.execute("DELETE FROM emprunts where code=?",(
                                                                        self.CODE.get(),
                                                                        ))
                        connexion.commit()
                        self.fetch_data()
                        cur.close()
                        self.search_txt_code.set("")
                        self.search_txt_mt.set("")

                        cur = connexion.cursor()
                        cur.execute('''CREATE TABLE IF NOT EXISTS emprunts(code INTEGER PRIMARY KEY, Titre TEXT, matricule INTEGER, nom TEXT, date1 INTEGER, date2 INTEGER)''')
                                        

                        cur.execute('''CREATE TABLE IF NOT EXISTS livres_pro(IMARY KEY, tailte TEXT, Auteur TEXT, Edit TEXT, Langue TEXT)''')

                        if self.search_by.get()== 'livres emprunter':
                                sql = "SELECT  tailte,Auteur,Edit,Langue FROM livres_pro INNER JOIN emprunts ON livres_pro.tailte= emprunts.Titre GROUP BY tailte, Auteur, Edit, Langue "
                                cur.execute(sql)           
                                rows=cur.fetchall()
                                if len(rows)!=0:
                                        self.Emprunt_table.delete(*self.Emprunt_table.get_children())
                                        for row in rows:
                                                self.Emprunt_table.insert('',END,values=row)
                                        connexion.commit()
                                connexion.close()

                        messagebox.showinfo("Success","vous avez rendu le livre!")


                else:
                        messagebox.showinfo("Non achever","Selectionnez un champ!")
        else:
                messagebox.showinfo("Non","Selectionnez un champ!")

class Etudiant(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg = "#87CEEB")


        
        title=Label(self,text="Gestion des Adhérants",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#8A2BE2",fg="#40FF33")
        title.pack(side=TOP,fill=X) 


        #================All Variables=========================
        self.MATRICULE_var=StringVar()
        self.NOM_var=StringVar()
        self.PRENOM_var=StringVar()
        self.FACULTE_var=StringVar()
        self.GENRE_var=StringVar()
        self.ADHERANT_var=StringVar()

        self.filename_var = StringVar()
        # self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        #==========manage frame=====================

        Manage_Frame=Frame(self,bd=4,relief=RIDGE,bg="#143685")
        Manage_Frame.place(x=20,y=100,width=475,height=530)

        m_title=Label(Manage_Frame,text="Enrégistrement  \nEtudiants/Proffeseurs",bg="#143685",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_adh=Label(Manage_Frame,text="Adhérant :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_adh.grid(row=1,column=0,padx=20,pady=10,sticky="w")

        combo_adh=ttk.Combobox(Manage_Frame,textvariable=self.ADHERANT_var,font=("times new roman",14,"bold"),state='readonly')
        combo_adh['values']=("Enseignant","Etudiant")
        combo_adh.grid(row=1,column=1,padx=10,pady=10,sticky="w")

        lbl_Matricule=Label(Manage_Frame,text="Matricule :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Matricule.grid(row=2,column=0,padx=20,pady=10,sticky="w")

        txt_Matricule=Entry(Manage_Frame,textvariable=self.MATRICULE_var,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE)
        txt_Matricule.grid(row=2,column=1,padx=10,pady=10,sticky="w")

        lbl_Nom=Label(Manage_Frame,text="Nom/Prenom :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Nom.grid(row=3,column=0,padx=20,pady=10,sticky="w")

        txt_Nom=Entry(Manage_Frame,textvariable=self.NOM_var,font=("times new rolan",15,"bold"),bd=5,relief=GROOVE)
        txt_Nom.grid(row=3,column=1,padx=10,pady=10,sticky="w")

        lbl_Faculte=Label(Manage_Frame,text="Faculté :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Faculte.grid(row=4,column=0,padx=20,pady=10,sticky="w")

        combo_Faculte=ttk.Combobox(Manage_Frame,textvariable=self.FACULTE_var,font=("times new roman",14,"bold"),state='readonly')
        combo_Faculte['values']=("Informatique","Santé","Théologie","Etudation","Droit","Autres")
        combo_Faculte.grid(row=4,column=1,pady=10,padx=20)

        lbl_Genre=Label(Manage_Frame,text="Genre :",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_Genre.grid(row=5,column=0,padx=10,pady=10,sticky="w")

        self.values = {"Maxculin" : "Maxculin", "Feminin" : "Feminin"}

        i = 250
        for (text, value) in self.values.items():
            Radiobutton(Manage_Frame, text = text, variable = self.GENRE_var,
                value = value).place(x=i,y=370)
            i = i +100

#====================button Frame============
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=15,y=450,width=420)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_etudiants).grid(row=0,column=0,padx=10,pady=10)
        updbtn=Button(btn_Frame,text="Update",width=10,command=self.update_date).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

#==========detail frame=====================
        Detail_Frame=Frame(self,bd=4,relief=RIDGE,bg="#143685")
        Detail_Frame.place(x=500,y=100,width=750,height=580)

        lbl_search=Label(Detail_Frame,text="Recherche",bg="#143685",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("Adherant","Matricule","Nom","Genre")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new rolan",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,padx=20,pady=10,sticky="w")

        searchbtn=Button(Detail_Frame,text="OK",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Retour",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

#=========Table Frame=====================
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#ED33FF")
        Table_Frame.place(x=10,y=70,width=720,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Etudiants_table=ttk.Treeview(Table_Frame,columns=("adherant","matricule","nom","faculte","genre"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Etudiants_table.xview)
        scroll_y.config(command=self.Etudiants_table.yview)
        self.Etudiants_table.heading("adherant",text="Adherant")  
        self.Etudiants_table.heading("matricule",text="Matricule")
        self.Etudiants_table.heading("nom",text="Nom")
        # self.Etudiants_table.heading("prenom",text="Prenom")
        self.Etudiants_table.heading("faculte",text="Faculté")
        self.Etudiants_table.heading("genre",text="Genre")
        self.Etudiants_table['show']='headings'
        self.Etudiants_table.column("adherant",width=120)
        self.Etudiants_table.column("matricule",width=50)
        self.Etudiants_table.column("nom",width=125)
        # self.Etudiants_table.column("prenom",width=125)
        self.Etudiants_table.column("faculte",width=70)
        self.Etudiants_table.column("genre",width=50)
        # self.Etudiants_table.column("photo",width=150)
        # self.Etudiants_table.column("address",width=150)
        self.Etudiants_table.pack(fill=BOTH,expand=1)
        self.Etudiants_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data() 
    def add_etudiants(self):
        if self.MATRICULE_var.get()=="" or self.NOM_var.get()=="" or self.ADHERANT_var.get()=="":
                messagebox.showerror("Error","All fields are required!!!")
        else:
                try:

                        connexion = sqlite3.connect("Emprunt_livres.db")
                        cur = connexion.cursor()
                        cur.execute('''CREATE TABLE IF NOT EXISTS etudiants(adherant TEXT, matricule INTEGER PRIMARY KEY, nom TEXT, faculte TEXT, genre TEXT)''')

                        cur.execute("insert into etudiants values(?,?,?,?,?)",(self.ADHERANT_var.get(),
                                                                                        self.MATRICULE_var.get(),
                                                                                        self.NOM_var.get(),
                                                                                        self.FACULTE_var.get(),
                                                                                        self.GENRE_var.get(),
                                                                                        # self.PHOTO_var.get()
                                                                                        ))
                        connexion.commit()
                        self.fetch_data()
                        self.clear()
                        cur.close()
                        messagebox.showinfo("Success","oppération réussie!")
                except Exception as es:
                        messagebox.showerror('error',f'error due to : {str(es)}', parent = self)



    def fetch_data(self):
        con = sqlite3.connect("Emprunt_livres.db")
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS etudiants(adherant TEXT, matricule INTEGER PRIMARY KEY, nom TEXT, faculte TEXT, genre)''')
                
        cur.execute("select * from etudiants")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Etudiants_table.delete(*self.Etudiants_table.get_children())
                for row in rows:
                        self.Etudiants_table.insert('',END,values=row)
                con.commit()
        cur.close()
    def clear(self):
            self.ADHERANT_var.set("")
            self.MATRICULE_var.set("")
            self.NOM_var.set("")
            self.FACULTE_var.set("")
            self.GENRE_var.set("")
        #     self.PHOTO_var.set("")

    def get_cursor(self,ev):
            curosor_row = self.Etudiants_table.focus()
            contents= self.Etudiants_table.item(curosor_row)
            row=contents['values']
            (row)
            self.ADHERANT_var.set(row[0])
            self.MATRICULE_var.set(row[1])
            self.NOM_var.set(row[2])
            self.FACULTE_var.set(row[3])
            self.GENRE_var.set(row[4])
        #     self.PHOTO_var.set(row[5])
        #     self.txt_Address.delete("1.0",END)
        #     self.txt_Address.insert(END,row[6]) 
    def update_date(self): 
            try:  
                con = sqlite3.connect("Emprunt_livres.db")
                cur = con.cursor()
                cur.execute('''CREATE TABLE IF NOT EXISTS etudiants(adherant TEXT, matricule INTEGER PRIMARY KEY, nom TEXT, faculte TEXT, genre TEXT)''')
                        
                cur.execute("update etudiants set adherant=?, matricule=?, nom=?,faculte=?,genre=? where matricule=?",(
                                                                                                        self.ADHERANT_var.get(),
                                                                                                        self.MATRICULE_var.get(),
                                                                                                        self.NOM_var.get(),
                                                                                                        self.FACULTE_var.get(),
                                                                                                        self.GENRE_var.get(),
                                                                                                        # self.PHOTO_var.get(),
                                                                                                        self.MATRICULE_var.get()
                                                                                                        ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
            except Exception as es:
                messagebox.showerror('error',f'error due to : {str(es)}', parent = self)

    def delete_data(self):
        con = sqlite3.connect("Emprunt_livres.db")
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS etudiants(adherant TEXT, matricule INTEGER PRIMARY KEY, nom TEXT, faculte TEXT, genre)''')
               
        sql = "DELETE FROM etudiants WHERE matricule = ? "
        cur.execute(sql, (self.MATRICULE_var.get(),))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    def search_data(self):
        con = sqlite3.connect("Emprunt_livres.db")
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS etudiants(adherant TEXT, matricule INTEGER PRIMARY KEY, nom TEXT, faculte TEXT, genre)''')
               
        if self.search_by.get()== 'Matricule':
                sql = "select * FROM etudiants WHERE matricule = ? "
                cur.execute(sql, (self.search_txt.get(),))
                rows=cur.fetchall()
                if len(rows)!=0:
                        self.Etudiants_table.delete(*self.Etudiants_table.get_children())
                        for row in rows:
                                self.Etudiants_table.insert('',END,values=row)
                        con.commit()  
                con.close()
        elif self.search_by.get()== 'Nom':
                sql = "select * FROM etudiants WHERE nom = ? "
                cur.execute(sql, (self.search_txt.get(),))
                rows=cur.fetchall()
                if len(rows)!=0:
                        self.Etudiants_table.delete(*self.Etudiants_table.get_children())
                        for row in rows:
                                self.Etudiants_table.insert('',END,values=row)
                        con.commit()  
                con.close()
        elif self.search_by.get()== 'Faculté':
                sql = "select * FROM etudiants WHERE faculte = ? "
                cur.execute(sql, (self.search_txt.get(),))
                rows=cur.fetchall()
                if len(rows)!=0:
                        self.Etudiants_table.delete(*self.Etudiants_table.get_children())
                        for row in rows:
                                self.Etudiants_table.insert('',END,values=row)
                        con.commit()  
                con.close()
        elif self.search_by.get()== 'Adherant':
                sql = "select * FROM etudiants WHERE adherant = ? "
                cur.execute(sql, (self.search_txt.get(),))
                rows=cur.fetchall()
                if len(rows)!=0:
                        self.Etudiants_table.delete(*self.Etudiants_table.get_children())
                        for row in rows:
                                self.Etudiants_table.insert('',END,values=row)
                        con.commit()  
                con.close()
        elif self.search_by.get()== 'Genre':
                sql = "select * FROM etudiants WHERE niveau = ? "
                cur.execute(sql, (self.search_txt.get(),))
                rows=cur.fetchall()
                if len(rows)!=0:
                        self.Etudiants_table.delete(*self.Etudiants_table.get_children())
                        for row in rows:
                                self.Etudiants_table.insert('',END,values=row)
                        con.commit()  
                con.close()
        else:
                pass
                

if __name__ == "__main__":
    app = Principal()
    app.geometry("800x1000")
    app.title('Gestion des emprunts de la bibliotheque de l UAC')

    app.mainloop()
