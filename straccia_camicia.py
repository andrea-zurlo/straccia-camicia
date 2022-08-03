import random
from itertools import permutations
import matplotlib.pyplot as  plt
import math

class Mazzo(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        for i in list('123'*4+'-'*28): self.append(i)

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
    def __init__(self, mazzo = Mazzo(), mescola = False):
        self.mazzo = mazzo
        if mescola: self.mazzo.mescola()
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

    def gioca_mano(self, log = False):
        self.numero_mossa += 1
        if len(self.g_attivo.mano) != 0:
            carta = self.g_attivo.gioca_carta()
            self.piatto.append(carta)
            if log : print(str(self.numero_mossa)+' - '+self.g_attivo.nome+': '+carta)
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
            if log: print(str(self.numero_mossa)+' - '+self.g_attivo.nome+': perde')
            self.fine = True                

    def gioca(self, log = False):
        while not self.fine:
            self.gioca_mano(log)


def unique_permutations(iterable, r=None):
    # https://stackoverflow.com/questions/6284396/permutations-with-unique-values
    previous = tuple()
    for p in permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p
'''
mosse = 0
iterazione = 0
# max_iterazioni = 100000
mazzo = Mazzo(['-']*40)
for map in permutations(range(40), 12):
    for per in unique_permutations('123'*4, 12):
        iterazione+=1
        mazzo = Mazzo(['-']*40)
        for i, p in zip(map, per):
            mazzo[i] = p
        # 
        g = Gioco(mazzo)
        g.gioca()
        if g.numero_mossa > mosse:
            mosse = g.numero_mossa
            print('\n'+str(iterazione)+' '+str(mosse)+' '+str(g.mazzo))
    #     if iterazione == max_iterazioni: break
    # if iterazione == max_iterazioni: break
'''

mosse = 0
iterazione = 0
max_iterazione = 10000
mazzo_base = Mazzo()
l = []
while iterazione < max_iterazione:
    iterazione += 1

    g = Gioco(mazzo = mazzo_base, mescola=True)
    g.gioca()
    l.append(g.numero_mossa)
    if g.numero_mossa > mosse:
        mosse = g.numero_mossa
        print('\n'+str(iterazione)+' '+str(mosse)+' '+str(g.mazzo))

plt.hist(l, max_iterazione)
plt.show()


# partita più lunga trovata
# 623286 2494 Mazzo: - - 2 - 3 3 - - - - - - 3 1 - - - - 2 - 1 1 1 - - - - - - - 3 - - - - - 2 - 2 -