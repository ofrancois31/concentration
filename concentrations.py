import tkinter as tk

class Fenetre(tk.Tk):
    def __init__(self):
        super().__init__()
        self.champ={"Densité": tk.DoubleVar(),
                      "Pureté": tk.IntVar(),
                      "Masse_molaire": tk.DoubleVar()}
        self._sqelette()
        self.title("Concentration")
    def _sqelette(self):
        self.label1=tk.Label(self, text="Affichage", bg="white")
        self.label1.grid(row=0, column=0,columnspan=2)
        self.label2=tk.Label(self, text="Densité")
        self.label2.grid(row=1,column=0)
        self.label3=tk.Label(self, text="Pureté (en %)")
        self.label3.grid(row=2, column=0)
        self.label4=tk.Label(self, text="Masse_molaire")
        self.label4.grid(row=3, column=0)
        self.entre1=tk.Entry(self, textvariable=self.champ["Densité"])
        self.entre1.grid(row=1,column=1)
        self.entre2=tk.Entry(self, textvariable=self.champ["Pureté"])
        self.entre2.grid(row=2,column=1)
        self.entre3=tk.Entry(self, textvariable=self.champ["Masse_molaire"])        
        self.entre3.grid(row=3, column=1)
        self.bouton=tk.Button(self,text="Calculer", command=self.action)
        self.bouton.grid(row=4, column=1)
        
    def action(self):
        v_densite=self.champ["Densité"].get()
        v_purete=self.champ["Pureté"].get()
        v_masse_molaire=self.champ["Masse_molaire"].get()
        resultat=(v_densite*10*v_purete)/v_masse_molaire
        result=round(resultat, 3)
        self.label1.configure(text=str(result)+" "+ "mol/L")       

app = Fenetre()
app.mainloop()        
