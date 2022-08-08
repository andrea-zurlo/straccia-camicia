#include <vector>
#include <iostream>     // std::cout
#include <algorithm>    // std::shuffle
#include <array>        // std::array
#include <random>       // std::default_random_engine
#include <chrono>       // std::chrono::system_clock
#include <string>
#include <list>

using namespace std;

class Mazzo {
public:
    vector<int> mazzo = {1,2,3,1,2,3,1,2,3,1,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    
    void mescola() {
        unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
        shuffle(mazzo.begin(), mazzo.end(), std::default_random_engine(seed));
    }
};

class Giocatore {
public: 
    list<int> mano;
    string nome;
    
    Giocatore(string nome, list<int>* mano) : nome(nome), mano(*mano) {}
    
    int gioca_carta() {
        int ret = mano.back();
        mano.pop_back();
        return ret;
    }
    
};

class Piatto {
public:
    vector<int> piatto = {};
    int chiede = 0;
};

class Gioco {
public:
    Mazzo mazzo;
    Piatto piatto;
    Giocatore* g1,* g2;
    Giocatore* giocatori[2];
    int numero_mossa = 0;
    bool fine = false;
    int piatto_chiede = 0;
    bool log;
    
    
    Gioco(bool mescola, bool log) : log(log) {
        if (mescola) { 
            mazzo.mescola(); 
        }
        g1 = new Giocatore(string("Marco"), new list<int>(mazzo.mazzo.begin(), mazzo.mazzo.begin() + 20));
        g2 = new Giocatore(string("Luca"), new list<int>(mazzo.mazzo.begin() + 20, mazzo.mazzo.end()));
        giocatori[0] = g1;
        giocatori[1] = g2;
    }
    
    void valori_iniziali(){
        cout << "Mazzo:\n";
        for (int i : mazzo.mazzo) {
            cout << i << " ";
        }
        cout << endl;
        cout << "Mano giocatore 1:\n";
        for (int i : g1->mano) {
            cout << i << " ";
        }
        cout << endl;
        cout << "Mano giocatore 2:\n";
        for (int i : g2->mano) {
            cout << i << " ";
        }
        
    }
    
    void scambia_giocatori() {
        Giocatore* tmp = giocatori[0];
        giocatori[0] = giocatori[1];
        giocatori[1] = tmp;
        cout << "giocatori scambiati" << endl;
    }
    
    void consegna_piatto() {
        reverse(piatto.piatto.begin(), piatto.piatto.end());
        for (int i : piatto.piatto) {
            giocatori[1]->mano.push_front(i);
        }
        piatto = *(new Piatto());
    }
    
    void gioca_mano() {
        numero_mossa++;
        int carta = 0;
        if(giocatori[0]->mano.size() != 0){
            carta = giocatori[0]->gioca_carta();
            piatto.piatto.push_back(carta);
            if (log) { 
                cout << numero_mossa << " " << giocatori[0]->nome << " " << carta << endl; 
            }
            if (carta > 0) {
                piatto_chiede = carta;
                scambia_giocatori();
            } else {
                if (piatto_chiede == 0) {
                    scambia_giocatori();
                } else if (piatto_chiede == 1){
                    consegna_piatto();
                    scambia_giocatori();
                } else {
                    piatto_chiede--;
                }
            }
        } else {
            consegna_piatto();
            if (log) {
                cout << numero_mossa << " " << giocatori[0]->nome << "perde";
            }
            fine = true;
        }
    }
    
    void gioca(){
        while(!fine) {
            gioca_mano();
        }
    }
};

int main(){
    int mosse = 0;
    int max_iterazione = 10;
    Mazzo mazzo_base;
    Gioco g(true, true);
    g.gioca();
    
}