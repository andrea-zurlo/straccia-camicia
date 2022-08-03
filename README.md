# straccia-camicia

Mazzo italiano da 40 carte, due giocatori, 20 carte a testa in modo casuale. I giocatori tengono i due mazzi a faccia in giu e scoprono le carte dall'alto.
Se si gioca una carta che non prende la mano passa all'altro giocatore.
Le carte che prendono sono l'asso, il due e il tre, per ciascuna di esse l'altro giocatore deve giocare rispettivamente 1, 2 e 3 carte.
Se il giocatore non riesce a rispondere con una carta che prende allora perde la mano e il giocatore che vince la mano prende il piatto e lo mette in ordine sotto il suo mazzo (ho realizzato adesso che ho sbagliato a fare questa cosa nel programma python perché quando uno prende il piatto deve rovesciare il mazzetto a faccia in giù, però direi che si risolve con un reverse). 
La mano la inizia il giocatore che vince, chi rimane senza carte perde.

Il numero di mazzi iniziali possibili è pari al numero di permutazioni di 40 elementi diversi, ovvero 40! Ordine di grandezza ~ E47.
Tuttavia si deve tenere conto che scambiare due carte con lo stesso valore (e.g. asso con asso, due con due, carta che non prende con carta che non prende, etc.) porta ad una diversa permutazione ma il mazzo è equivalente perché la meccanica della partita è la stessa.
Quindi solo le posizioni delle 12 carte che prendono sono rilevanti.
[Da finire..]
