
class Clovek():
    
    def __init__(self, gui):
        self.gui = gui

    def povleci_potezo(self):
        #to funkcijo rabi samo računalnik - kot pri Bauerju igraj
        pass

    def prekini(self):
        # To metodo kliče GUI, če je treba prekiniti razmišljanje.
        # Človek jo lahko ignorira. Test
        pass

    def klik(self, novo):
        # Povlečemo potezo. Če ni veljavna, se ne bo zgodilo nič.
        self.gui.povleci_korak(novo)

    def povleci_korak(self):
        pass

