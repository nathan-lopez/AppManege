class Launcher:
    def __init__(self):
        self.nameOS = platform.system()
        # urls
        self.home = 'http://127.0.0.1:8000/'
        self.apropo = 'http://localhost:8888/prorpos.html'
        self.root = None
        self.nopage = True

    def init1(self):
        root = Tk()
        self.root = root
        height = 800
        width = 1000
        # proprietés de la fenetre
        root.geometry(f"{width}x{height}")
        if self.nameOS == "Windows":
            root.iconbitmap("static/images/logo.ico")
        root.minsize(width, height)
        root.maxsize(width, height)
        root.config(background='#acc0e4')
        root.title("Launcher")
        logo = PhotoImage(file="static/images/logo.png").zoom(19).subsample(19)
        message = "jean 3 : 16 car DIEU à tant aimé le monde  qu'IL à donné son Fils unique, enfin que quiconque" \
                       "croit en Lui ne périsse point, mais qu'il ai                                                 t la vie éternelle."
        self.main_body(root, message, logo)
        self.closed(root)

    def web_direct(self):
        if self.nopage:
            try:
               # self.root.quit()
               webbrowser.open_new(self.home)
               self.nopage = False
            except:
                pass

    def web_direct2(self):
        try:
            webbrowser.open_new(self.apropo)
            #self.root.quit()
        except:
            pass


    def main_body(self, root, msg, logo):
        # creation d'un frame au dessus
        top_bar = Frame(root, bg='#2d2e30')
        # composant de la top bar
        name__ministys = Label(top_bar, text='.ministrys', fg='#ffffff', bg='#2d2e30', font=("Terminal", 25), padx=0)
        name__ministys.place(x=180, y=23)
        name__groupe = Label(top_bar, text="GEADV", fg='#919be0', bg="#2d2e30", font=("Terminal", 45), padx=0, pady=0,
                             justify='center')
        name__groupe.place(x=5, y=0)
        top_bar.place(relwidth=1.0, height=60)
        # creation du footer
        bottom_bar = Frame(root, bg='#ffffff')
        #  components of bottom_bar
        message = Label(bottom_bar, text=msg, bg="#fffFff", font=('Terminal', 8), padx=0, pady=0, width=1,
                        justify="left")
        message.place(relwidth=1.0)
        bottom_bar.place(relwidth=1.0, y=780, height=20)
        # logo_canva
        logo_canva = Frame(root)
        # component of logo canva
        canva_img = Canvas(logo_canva, bg='#c8d7f1')
        canva_img.create_image(260, 360, image=logo)
        canva_img.place(relwidth=1.0, relheight=1.0)
        logo_canva.place(relwidth=0.52, x=0, y=60, height=720)

        # side_bar
        side_bar = Frame(root, bg='#ffffff')
        # compements
        bouton1 = Button(side_bar, text="Lancer GEADV.ministry", fg='#919be0', bg="#2d2e30", justify='center', padx=50,
                         command=self.web_direct)
        bouton1.place(y=50, x=23, relwidth=0.9, height=50)
        bouton2 = Button(side_bar, text="A propos de l'application", fg='#919be0', bg="#2d2e30", justify='center',
                         padx=50, command=self.web_direct2)
        bouton2.place(y=350, x=23, relwidth=0.9, height=50)
        bouton3 = Button(side_bar, text="Quitter l'application", fg='#919be0', bg="#2d2e30", justify='center', padx=50,
                         command=self.quiter)
        bouton3.place(y=650, x=23, relwidth=0.9, height=50)
        side_bar.place(relwidth=0.48, x=520, y=60, height=720)

    def quiter(self):
        rep = askokcancel("confirmer la fermeture ", "voulez-vous vraiment quitter?")
        if rep:
            self.root.destroy()
    def closed(self, root):
        self.root.protocol("WM_DELETE_WINDOW", self.quiter)
        root.mainloop()

    def contruction(self):
        if self.nameOS == "Linux":
            try:
                os.system("python3 manage.py runserver")
            except:
                print("erreur lier au système d'exploitation , il se peut que cette application ne peut passer "
                      "sur votre système")

        elif self.nameOS == "Windows":
            try:
                os.system("..\> py manage.py runserver")
            except:
                print("erreur lier au système d'exploitation , il se peut que cette application ne peut passer "
                      "sur votre système")


class GestionThread:
    def __init__(self):
        self.launcher = threading.Thread(target=Launcher().init1)
        self.server = threading.Thread(target=Launcher().contruction)
        self.server.start()
        self.launcher.start()
        self.server.join()


if __name__ == '__main__':
    from tkinter import *
    import webbrowser
    import platform
    import os
    import threading
    from tkinter.messagebox import askokcancel

    thead = GestionThread()
    # Launcher().init1()


