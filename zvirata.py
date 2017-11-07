import time
import random
import numpy as np

class Zvire(object):

    def __init__(self,vyska,sirka,ramena,barva,chapadla,rychlost,jidlo,elektrika,pst):
        "vzhled"
        vlastnosti={"hlava_vyska":vyska,"hlava_sirka":sirka,"pocet_ramen":ramena,"barva":barva,
                    "delka_chapadelek":chapadla}
        if vyska:
            self.hlava_vyska=np.random.randint(2,size=7)
        if sirka:
            self.hlava_sirka=np.random.randint(2,size=4)
        if ramena:
            self.pocet_ramen=np.random.randint(2,size=5)
        if barva:
            self.barva=np.random.randint(255,size=3)
        if chapadla:
            self.delka_chapadelek=np.random.randint(2,size=3)
        "vlastnosti"
        self.rychlost=1+rychlost*random.random() #1-2
        self.jidlo=jidlo #0-100
        self.elektrika=elektrika #0-100
        self.vlastnosti=vlastnosti
        self.pst=pst

    def spocti_vysku(self):
        # [min, max] min=1, max = 8
        # vyska hlavy [1,2,..8]
        if self.vlastnosti["hlava_vyska"]:
            vyska = 1+np.sum(self.hlava_vyska)
            return vyska
        else:
            return None

    def spocti_sirku(self):
        # sirka hlavy [1,2..5]
        if self.vlastnosti["hlava_sirka"]:
            sirka = 1+np.sum(self.hlava_sirka)
            return sirka
        else:
            return None

    def spocti_ramena(self):
        # pocet zahavych ramen [3,4, ..8]
        if self.vlastnosti["pocet_ramen"]:
            ramen = 3+np.sum(self.pocet_ramen)
            return ramen
        else:
            return None

    def spocti_chapadla(self):
        if self.vlastnosti["delka_chapadelek"]:
            chapadla =1+np.sum(self.delka_chapadelek)
            return chapadla
        else:
            return None

    def vypis(self):
        # vyska = np.sum(self.hlava_vyska)
        # sirka = np.sum(self.hlava_sirka)
        # ramen = np.sum(self.pocet_ramen)
        # chapadla = np.sum(self.delka_chapadelek)
        print("Máme vytvořené zvířátko, která má {} vysku hlavy, {} sirku, {} ramen, {} dlouhá chapadla"
              .format(self.spocti_vysku(),self.spocti_sirku(),self.spocti_ramena(),self.spocti_chapadla()))
        #print(self.hlava_vyska)
        #print(self.hlava_sirka)
        #print(self.pocet_ramen)
        #print(self.delka_chapadelek)

        print("Toto zvířátko jede {} rychlostí, nasytí {}, nabije {} elektrikou "
              .format(self.rychlost,self.jidlo,self.elektrika))

class Medusa(Zvire):
    "Medusa"

    def __init__(self):
        "vzhled"
        #Zvire.__init__(True,True,True,True,True,True,0.3,50,0)
        self.hlava_vyska=np.random.randint(2,size=7)
        self.hlava_sirka=np.random.randint(2,size=4)
        self.pocet_ramen=np.random.randint(2,size=5)
        self.barva=np.random.randint(255,size=3)
        self.delka_chapadelek=np.random.randint(2,size=3)
        "vlastnosti"
        self.rychlost=1+0.3*random.random() #1-2
        self.jidlo=50 #0-100
        self.zivot=10
        self.elektrika=0 #0-100
        self.vlastnosti={"hlava_vyska":True,"hlava_sirka":True,"pocet_ramen":True,"barva":True,
                    "delka_chapadelek":True}

    def proved_mutaci(self,zvire):
        if zvire.vlastnosti["hlava_vyska"]:
            self.hlava_vyska=self.mutace(self.hlava_vyska,zvire.hlava_vyska,zvire.pst)
        if zvire.vlastnosti["hlava_sirka"]:
            self.hlava_sirka=self.mutace(self.hlava_sirka,zvire.hlava_sirka,zvire.pst)
        if zvire.vlastnosti["pocet_ramen"]:
            self.pocet_ramen=self.mutace(self.pocet_ramen,zvire.pocet_ramen,zvire.pst)
        if zvire.vlastnosti["delka_chapadelek"]:
            self.delka_chapadelek=self.mutace(self.delka_chapadelek,zvire.delka_chapadelek,zvire.pst)
        print("Meduza se zmutovala na {} vyska hlavy, {} sirka hlavy, {} ramen, {} delka chapadel".format
              (self.spocti_vysku(),self.spocti_sirku(),self.spocti_ramena(),self.spocti_chapadla()))

    def mutace(self, hodnoty1, hodnoty2, pst):
        nove_hodnoty=list()
        for i in range(len(hodnoty1)):
            p=random.random()
            if p<pst:
                nove_hodnoty.append(hodnoty2[i])
            else:
                nove_hodnoty.append(hodnoty1[i])
        return nove_hodnoty

    # def spocti_vysku(self):
    #     # [min, max] min=1, max = 8
    #     # vyska hlavy [1,2,..8]
    #     vyska = 1+np.sum(self.hlava_vyska)
    #     return vyska
    #
    # def spocti_sirku(self):
    #     # sirka hlavy [1,2..5]
    #     sirka = 1+np.sum(self.hlava_sirka)
    #     return sirka
    #
    # def spocti_ramena(self):
    #     # pocet zahavych ramen [3,4, ..8]
    #     ramen = 3+np.sum(self.pocet_ramen)
    #     return ramen
    #
    # def spocti_chapadla(self):
    #     chapadla =1+np.sum(self.delka_chapadelek)
    #     return chapadla

    def vypis(self):
        # vyska = np.sum(self.hlava_vyska)
        # sirka = np.sum(self.hlava_sirka)
        # ramen = np.sum(self.pocet_ramen)
        # chapadla = np.sum(self.delka_chapadelek)
        print("Máme vytvořenou meduzu, která má {} vysku hlavy, {} sirku, {} ramen, {} dlouhá chapadla"
              .format(self.spocti_vysku(),self.spocti_sirku(),self.spocti_ramena(),self.spocti_chapadla()))
        #print(self.hlava_vyska)
        #print(self.hlava_sirka)
        #print(self.pocet_ramen)
        #print(self.delka_chapadelek)

        print("Tato meduza jede {} rychlostí, má {}. hlad, {}. životů z 10, {} elektriku ze 100"
              .format(self.rychlost,100-self.jidlo,self.zivot,self.elektrika))