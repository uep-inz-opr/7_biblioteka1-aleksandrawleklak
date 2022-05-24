import ast

ilosc_ksiazek = int(input())


class Biblioteka():
    def __init__(self,tytul,autor,rok): 
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.ewidencja = 0
        
    def __repr__(self):
        return "'"+self.autor+"', "+str(self.ewidencja+1)
    

spis = {}

for ilosc in range(ilosc_ksiazek):
    nowa = eval(input())
    tytul = nowa[0].strip()
    autor = nowa[1].strip()
    rok = nowa[2]

    if tytul in spis:
        spis[tytul].ewidencja = spis[tytul].ewidencja+1
    else:
        spis[tytul] = Biblioteka(tytul,autor,rok)

spis_alfabetyczny = sorted(spis.items())

for ksiazka in spis_alfabetyczny:
    print(ksiazka)