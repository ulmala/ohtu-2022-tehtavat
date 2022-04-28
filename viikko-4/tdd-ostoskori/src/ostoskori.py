from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._kori = {}

    def tavaroita_korissa(self):
        tavaroita = 0
        for ostos in self._kori.values():
            tavaroita += ostos.lukumaara()
        return tavaroita

    def hinta(self):
        hinta = 0
        for ostos in self._kori.values():
            hinta += ostos.hinta()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi() in self._kori.keys():
            self._kori[lisattava.nimi()].muuta_lukumaaraa(1)
        else:
            self._kori[lisattava.nimi()] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        if poistettava.nimi() in self._kori.keys():
            if self._kori[poistettava.nimi()].lukumaara() > 1:
                self._kori[poistettava.nimi()].muuta_lukumaaraa(-1)
            else:
                del self._kori[poistettava.nimi()]

    def tyhjenna(self):
        self._kori = {}

    def ostokset(self):
        return [ostos for ostos in self._kori.values()]
