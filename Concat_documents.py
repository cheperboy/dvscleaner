import Tkinter
import tkFileDialog
import tkMessageBox
import dvscleaner

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.sourcefile = ""
        self.initialize()

    def initialize(self):
        self.grid()

        #boutton DOSSIER
        button1 = Tkinter.Button(self, text='Dossier', width=25, command=self.OnChooseFolderClick)
        button1.grid(column=0,row=0)

        #Label CHEMIN DOSSIER SOURCE
        self.labelVariable1 = Tkinter.StringVar()
        label1 = Tkinter.Label(self, textvariable=self.labelVariable1, anchor="e",fg="black",bg="white")
        label1.grid(column=1,row=0,columnspan=2,sticky='EW')
        self.labelVariable1.set(u"Choisir un dossier source")

        #Label CHEMIN DOSSIER CIBLE
        self.labelVariable2 = Tkinter.StringVar()
        label2 = Tkinter.Label(self,textvariable=self.labelVariable2, anchor="e",fg="black",bg="white")
        label2.grid(column=1,row=1,columnspan=2,sticky='EW')
        self.labelVariable2.set(u"")

        #boutton LANCER TRAITEMENT
        button2 = Tkinter.Button(self, text='Lancer le traitemement', width=25, command=self.OnLaunchClick)
        button2.grid(column=0,row=1)
 
        #Label CONSOLE
        self.labelVariable3 = Tkinter.StringVar()
        label3 = Tkinter.Label(self,textvariable=self.labelVariable3, anchor="w",fg="black",bg="white")
        label3.grid(column=0,row=2,columnspan=3,sticky='EW')
        self.labelVariable3.set(u"Test")


        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,True)

    def OnChooseFolderClick(self):
        folder = tkFileDialog.askdirectory()
        self.sourcefile = folder
        self.labelVariable1.set( folder )

    def OnLaunchClick(self):
        if (self.sourcefile == "") :
            self.labelVariable1.set( "pas de dossier selectionne")
        else :
            ret = dvscleaner.main_function(self.sourcefile)
            self.labelVariable2.set(ret)

        
        
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Concat Documents')
    app.mainloop()
