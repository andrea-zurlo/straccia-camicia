import random

class Mazzo(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self.semi = ['B','C','D','S']
        self.numeri = [str(i) for i in range(1,11)]

        for s in self.semi:
            for n in self.numeri:
                self.append(s+n)

    def mescola(self):
        random.shuffle(self)

class Giocatore():
    def __init__(self, mano, nome):
        self.mano = mano
        self.nome = nome
    
    def gioca_carta(self):
        return self.mano.pop()

    def __str__(self):
        return self.nome

class Piatto(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self.chiede = 0

class Gioco():
    def __init__(self):
        self.mazzo = Mazzo()
        self.g1 = Giocatore(self.mazzo[:20], 'g1')
        self.g2 = Giocatore(self.mazzo[20:], 'g2')
        self.piatto = Piatto()
        self.g_attivo = self.g1
        self.g_inattivo = self.g2
        self.numero_mossa = 0

    def scambia(self):
        if self.g_attivo == self.g1:
            self.g_attivo = self.g2
            self.g_inattivo = self.g1
        elif self.g_attivo == self.g2:
            self.g_attivo = self.g1
            self.g_inattivo = self.g2

    def gioca_mano(self):
        self.numero_mossa += 1
        carta = self.g_attivo.gioca_carta()
        self.piatto.append(carta)
        print(str(self.numero_mossa)+' - '+self.g_attivo.nome+': '+carta)

        if carta[-1] in ['1', '2', '3']:
            self.piatto.chiede = int(carta[-1])
            self.scambia()
        else:
            if self.piatto.chiede == 0:
                self.scambia()
            elif self.piatto.chiede == 1:
                self.g_inattivo.mano = self.piatto + self.g_inattivo.mano
                self.piatto = []
            else:
                self.piatto.chiede -= 1

g = Gioco()
for _ in range(10):
    g.gioca_mano()