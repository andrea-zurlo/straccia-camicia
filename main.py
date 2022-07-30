import random
import matplotlib.pylab as plt

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

# le carte piu in basso sono quelle all'inizio della lista,
# vengono giocate prima quelle alla fine della lista

class Gioco():
    def __init__(self):
        self.mazzo = Mazzo()
        self.mazzo.mescola()
        self.mani = {'g1': self.mazzo[:20], 'g2': self.mazzo[20:]}
        self.piatto = []
        self.giocatore = 'g1'
        self.altro = 'g2'
        self.mossa = 0

    def gioca(self, n = 0, cambia_giocatore = False):
        self.mossa += 1
        if cambia_giocatore:
            if self.giocatore == 'g1':
                self.giocatore = 'g2'
                self.altro = 'g1'
            elif self.giocatore == 'g2':
                self.giocatore = 'g1'
                self.altro = 'g2'
        
        if len(self.mani[self.giocatore]) == 0:
            self.mani[self.altro] = self.piatto + self.mani[self.altro]
            # print(self.altro+' vince')
            # print(self.mani)
            return

        self.piatto.append(self.mani[self.giocatore].pop())
        carta = self.piatto[-1]
        # print(str(self.mossa)+' - '+self.giocatore+': '+carta)

        if carta[-1] == '1':
            self.gioca(1, True)
        elif carta[-1] == '2':
            self.gioca(2, True)
        elif carta[-1] == '3':
            self.gioca(3, True)
        else:
            if n!= 0:
                if n == 1:
                    # print('piatto: ', self.piatto)
                    # print(self.altro, self.mani[self.altro])
                    self.mani[self.altro] = self.piatto + self.mani[self.altro]
                    # print('altro + piatto: ', self.mani[self.altro])
                    # print(self.giocatore, self.mani[self.giocatore])
                    self.piatto = []
                    self.gioca(0, True)
                else:
                    self.gioca(n-1, False)
            else:    
                self.gioca(0, True)

                
l = []            


for _ in range(1000):
    sc = Gioco()
    # print('g1: '+str(sc.mani['g1']))
    # print('g2: '+str(sc.mani['g2']))
    sc.gioca()
    l.append(sc.mossa)

n, bins, patches = plt.hist(l, 100)
plt.show()