import random
import itertools

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
        
    def __str__(self):
        s = 'Mazzo:'
        for c in self:
            s+= ' '+c
        return s

class Giocatore():
    def __init__(self, mano, nome):
        self.mano = mano
        self.nome = nome
        
    def gioca_carta(self):
        return self.mano.pop()
        
    def __str__(self):
        s = 'Mano '+self.nome+':'
        for c in self.mano:
            s += ' '+c
        return s

class Piatto(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self.chiede = 0

class Gioco():
    def __init__(self, mazzo = Mazzo()):
        self.mazzo = mazzo
        self.mazzo.mescola()
        self.g1 = Giocatore(self.mazzo[:20], 'g1')
        self.g2 = Giocatore(self.mazzo[20:], 'g2')
        self.piatto = Piatto()
        self.g_attivo = self.g1
        self.g_inattivo = self.g2
        self.numero_mossa = 0
        self.fine = False
    
    def valori_iniziali(self):
        print(self.mazzo)
        print()
        print(self.g1)
        print()
        print(self.g2)
        print()
        
    def scambia_giocatore(self):
        if self.g_attivo == self.g1:
            self.g_attivo = self.g2
            self.g_inattivo = self.g1
        elif self.g_attivo == self.g2:
            self.g_attivo = self.g1
            self.g_inattivo = self.g2
    
    def consegna_piatto(self):
        self.g_inattivo.mano = self.piatto + self.g_inattivo.mano
        self.piatto = Piatto()

    def gioca_mano(self):
        self.numero_mossa += 1
        if len(self.g_attivo.mano) != 0:
            carta = self.g_attivo.gioca_carta()
            self.piatto.append(carta)
            #print(str(self.numero_mossa)+' - '+self.g_attivo.nome+': '+carta)
            if carta[-1] in ['1','2','3']:
                self.piatto.chiede = int(carta[-1])
                self.scambia_giocatore()
            else:
                if self.piatto.chiede == 0:
                    self.scambia_giocatore()
                elif self.piatto.chiede == 1:
                    self.consegna_piatto()
                    self.scambia_giocatore()
                else:
                    self.piatto.chiede -= 1                
        else:
            self.consegna_piatto()
            #print(str(self.numero_mossa)+' - '+self.g_attivo.nome+': perde')
            self.fine = True                

'''
l = []
mosse = 0
while True:
    g = Gioco()
    #g.valori_iniziali()
    while not g.fine:
        g.gioca_mano()
    mosse = g.numero_mossa
    if mosse > 1500:
        print(mosse)
        g.valori_iniziali()
        break
'''
'''
mazzo = Mazzo()
mosse = 0
set = []
for i, m in enumerate(itertools.permutations(mazzo)):
    g = Gioco(list(m))
    while not g.fine:
        g.gioca_mano()
    if g.numero_mossa > mosse:
        mosse = g.numero_mossa
        print(str(i)+' '+str(mosse))
        set = g.mazzo
'''
mosse = 0
i = 0
while True:
    i += 1
    print('* ', end='')
    g = Gioco()
    while not g.fine:
        g.gioca_mano()
    if g.numero_mossa > mosse:
        mosse = g.numero_mossa
        print('\n'+str(i)+' '+str(mosse))