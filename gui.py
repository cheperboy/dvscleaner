import Tkinter
import tkFileDialog
import tkMessageBox
#from dvscleaner import main_function
import dvscleaner

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.sourcefile = ""
        self.initialize()

    def initialize(self):
        self.grid()


        button1 = Tkinter.Button(self, text='Dossier', width=25, command=self.OnChooseFolderClick)
        button1.grid(column=0,row=0)

        self.labelVariable1 = Tkinter.StringVar()
        label1 = Tkinter.Label(self,textvariable=self.labelVariable1, anchor="w",fg="black",bg="white")
        label1.grid(column=1,row=0,columnspan=2,sticky='EW')
        self.labelVariable1.set(u"Choisir un dossier source")

        self.labelVariable2 = Tkinter.StringVar()
        label2 = Tkinter.Label(self,textvariable=self.labelVariable2, anchor="w",fg="black",bg="white")
        label2.grid(column=1,row=1,columnspan=2,sticky='EW')
        self.labelVariable2.set(u"")

        button2 = Tkinter.Button(self, text='Lancer le traitemement', width=25, command=self.OnLaunchClick)
        button2.grid(column=0,row=1)
    
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,True)

    def OnChooseFolderClick(self):
        folder = tkFileDialog.askdirectory()
        self.sourcefile = folder
        self.labelVariable1.set( folder )

    def OnLaunchClick(self):
        if (self.sourcefile == "") :
            self.labelVariable1.set( "pas de dossier selectionne")
#            self.tkMessageBox.showinfo("Say Hello", "Hello World")
        else :
            ret = dvscleaner.main_function(self.sourcefile)
            self.labelVariable2.set(ret)

        
        
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
