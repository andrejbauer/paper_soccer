import tkinter as tk
from GUI import * 

clovek = "Čarovnik"
racunalnik = "Duh"


class Zacetno:
    def __init__(self, master):
        self.tip_igralec1 = clovek
        self.tip_igralec2 = racunalnik

        self.dovoljene_barve = ['yellow', 'blue']
        self.barva_igralec1 = 'red'
        self.barva_igralec2 = 'green'

        self.tezavnost1 = 0
        self.tezavnost2 = 0

        self.sirina = 9
        self.visina = 13

        self.slika_ozadje = tk.PhotoImage(file='slike/hogwarts.gif')#Slika za ozadje
        ozadje_label = tk.Label(master, image=self.slika_ozadje)
        ozadje_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        naslov = tk.Label(master, text = "Čarovniški nogomet")
        naslov.grid(row=0, column=0, columnspan=7)
        
        self.gumb_tip_1igralec = tk.Button(master, text=self.tip_igralec1,
                                      command=lambda: self.spremeni_tip_igralca(self.gumb_tip_1igralec))
        self.gumb_tip_1igralec.grid(row=1, column=0)

        self.gumb_tip_2igralec = tk.Button(master, text=self.tip_igralec2,
                               command=lambda: self.spremeni_tip_igralca(self.gumb_tip_2igralec))
        self.gumb_tip_2igralec.grid(row=1, column=5)

        gumb_igraj = tk.Button(master, text='Igraj',
                               command=self.zacni_igro)
        gumb_igraj.grid(row=20, column=0, columnspan=7)

        #Gumbi za barve 1.igralca:
        barve_1 = tk.Label(master, text="Izberi dom:")
        barve_1.grid(row=2, column=0)
        self.slika_gryffindor = tk.PhotoImage(file='slike/gryffindor.gif')
        self.slika_hufflepuff = tk.PhotoImage(file='slike/hufflepuff.gif')
        self.slika_ravenclaw = tk.PhotoImage(file='slike/ravenclaw.gif')
        self.slika_slytherin = tk.PhotoImage(file='slike/slytherin.gif')

        G1 = tk.Button(master, #text = "Gryfondom", #bg = 'red',
                       image=self.slika_gryffindor, anchor='n',
                       height=50, width=50, relief='sunken',
                       command=lambda: self.izberi_barvo('red', G1))
        P1 = tk.Button(master, #text = "Pihpuff", bg = 'yellow',
                       image=self.slika_hufflepuff, anchor='n',
                       height=50, width=50,
                       command=lambda: self.izberi_barvo('yellow', P1))
        D1 = tk.Button(master, #text = "Drznvraan", bg= 'blue',
                       image=self.slika_ravenclaw, anchor='n',
                       height=50, width=50,
                       command=lambda: self.izberi_barvo('blue', D1))
        S1 = tk.Button(master, #text = "Spolzgad", bg= 'green',
                       image=self.slika_slytherin, anchor='n',
                       height=50, width=50,
                       command=lambda: self.izberi_barvo('green', S1))
         
        self.gumbi_barve_igralca1 = [G1, P1, D1, S1]

        for (i, gumb) in enumerate(self.gumbi_barve_igralca1):
            gumb.grid(row=i//2+3, column=i % 2)
            

    # Gumbi za barve 2.igralca:
        barve_2 = tk.Label(master, text="Izberi dom:")
        barve_2.grid(row=2, column=5)

        G2 = tk.Button(master, #text = "Gryfondom", bg = 'red',
                       image=self.slika_gryffindor, anchor='n',
                       height=50, width=50,
                       command=lambda: self.izberi_barvo('red', G2))
        P2 = tk.Button(master, #text = "Pihpuff", bg = 'yellow',
                       image=self.slika_hufflepuff, anchor='n',
                       height=50, width=50,
                       command=lambda: self.izberi_barvo('yellow', P2))
        D2 = tk.Button(master, #text = "Drznvraan", bg= 'blue',
                       image=self.slika_ravenclaw, anchor='n',
                       height=50, width=50,
                       command=lambda: self.izberi_barvo('blue', D2))
        S2 = tk.Button(master, #text = "Spolzgad", bg= 'green',
                       image=self.slika_slytherin, anchor='n',
                       height=50, width=50, relief='sunken',
                       command=lambda: self.izberi_barvo('green', S2))

        self.gumbi_barve_igralca2 = [G2, P2, D2, S2]
        
        for (i, gumb) in enumerate(self.gumbi_barve_igralca2):
            gumb.grid(row=i//2+3, column=i % 2 + 5)

        #gumbi za težavnost prvega igralca
        self.nastavi_tez1 = tk.Frame()
        self.nastavi_tez1.grid(row=6, column=0, columnspan=3)

        tez1 = tk.Label(self.nastavi_tez1, text="Izberi težavnost:")
        tez1.grid(column=1, row=0)

        Level11 = tk.Button(self.nastavi_tez1, text="Shamer",  relief='groove',
                            command=lambda: self.spremeni_tezavnost(0, Level11))
        Level21 = tk.Button(self.nastavi_tez1, text="Smottan",
                            command=lambda: self.spremeni_tezavnost(1, Level21))
        Level31 = tk.Button(self.nastavi_tez1, text="Wulf",
                            command=lambda: self.spremeni_tezavnost(2, Level31))
        self.gumbi_tezavnost = [ Level11, Level21, Level31]

        # gumbi za težavnost drugega igralca
        self.nastavi_tez2 = tk.Frame()
        self.nastavi_tez2.grid(row=6, column=4, columnspan=3)

        tez2 = tk.Label(self.nastavi_tez2, text="Izberi težavnost:")
        tez2.grid(column=1, row=0)

        Level12 = tk.Button(self.nastavi_tez2, text="Shamer",  relief='groove',
                            command=lambda: self.spremeni_tezavnost(0, Level12))
        Level22 = tk.Button(self.nastavi_tez2, text="Smottan",
                            command=lambda: self.spremeni_tezavnost(1, Level22))
        Level32 = tk.Button(self.nastavi_tez2, text="Wulf",
                            command=lambda: self.spremeni_tezavnost(2, Level32))
        self.gumbi_tezavnost += [Level12, Level22, Level32]

        # izrišemo vse gumbe za težavnost:
        for (i, gumb) in enumerate(self.gumbi_tezavnost):
            gumb.grid(column=i % 3, row = 1)
        self.nastavi_tez1.grid_remove()  # Ker default igralec 1 človek

        #Gumb za velikost polja
        #malo_polje = 

    def spremeni_tip_igralca(self, gumb):
        # print(gumb, self.gumb1)
        if gumb == self.gumb1igralec:
            tip = self.tip_igralec1
            if tip == clovek:
                self.tip_igralec1 = racunalnik
                self.nastavi_tez1.grid()
            elif tip == racunalnik:
                self.tip_igralec1 = clovek
                self.nastavi_tez1.grid_remove()
            self.gumb1igralec.config(text=self.tip_igralec1)
        if gumb == self.gumb2igralec:
            tip = self.tip_igralec2
            if tip == clovek:
                self.tip_igralec2 = racunalnik
                self.nastavi_tez2.grid()
            elif tip == racunalnik:
                self.tip_igralec2 = clovek
                self.nastavi_tez2.grid_remove()
            self.gumb2igralec.config(text=self.tip_igralec2)

    def izberi_barvo(self, barva, gumb):

        if barva in self.dovoljene_barve:
            self.dovoljene_barve.remove(barva)
            if gumb in self.gumbi_barve_igralca1:
                self.dovoljene_barve.append(self.barva_igralec1)
                self.barva_igralec1 = barva
                for gumbek in self.gumbi_igralca1:
                    gumbek.config(relief='raised')
            if gumb in self.gumbi_barve_igralca2:
                self.dovoljene_barve.append(self.barva_igralec2)
                self.barva_igralec2 = barva
                for gumbek in self.gumbi_igralca2:
                    gumbek.config(relief='raised')
            gumb.config(relief='sunken')
        else:
            pass
            # v tem primeru je uporabnik izbral za oba nasprotnika enako barvo
        # print(self.barva_igralec1,self.barva_igralec2, gumb)

    def spremeni_tezavnost(self, tezavnost, trenutni_gumb):
        trenutni_igralec = self.gumbi_tezavnost.index(trenutni_gumb) // 3  # 0 pomeni 1. igralca, 1 pa drugega
        if trenutni_igralec == 0:
            if tezavnost == self.tezavnost1:
                pass
            else:
                self.gumbi_tezavnost[self.tezavnost1].config(relief='raised')
                self.tezavnost1 = tezavnost
                trenutni_gumb.config(relief='groove')
        else:
            if tezavnost == self.tezavnost2:
                pass
            else:
                self.gumbi_tezavnost[self.tezavnost2 + 3].config(relief='raised')
                self.tezavnost2 = tezavnost
                trenutni_gumb.config(relief='groove')

      
    def zacni_igro(self):
        okno_igrisca = tk.Toplevel()
        gui = GUI(okno_igrisca, root)  # , self)
        root.withdraw()
        gui.zacetni = self
        # Guiju in igri sporoči nastavitve.
        (gui.tezavnost1, gui.tezavnost2) = (self.tezavnost1, self.tezavnost2)
        (gui.barva_igralec1, gui.barva_igralec2) = (self.barva_igralec1, self.barva_igralec2)
        (gui.tip_igralec1, gui.tip_igralec2) = (self.tip_igralec1, self.tip_igralec2)
        gui.trenutna_barva = self.barva_igralec1
        gui.sirina, gui.visina = self.sirina, self.visina
        #(gui.igra.igralec1, gui.igra.igralec2) = (self.igralec1, self.igralec2)
        #gui.igra.na_vrsti = self.igralec1
        okno_igrisca.geometry("{0}x{1}".format(
            (self.sirina + 1) * gui.sirina_kvadratka,
            (self.visina + 1) * gui.sirina_kvadratka))
        gui.zacni_igro()

root = tk.Tk()

root.title("Čarovniški nogomet")
root.geometry("370x260")

zacetni_meni = Zacetno(root)


root.mainloop()
