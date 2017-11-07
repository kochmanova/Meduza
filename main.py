import zvirata
import time

if __name__ == "__main__":

    ptacek=zvirata.Zvire(True,False,False,True,True,0.2,1,0,0.2)
    ptacek.vypis()

    meduza=zvirata.Medusa()
    meduza.vypis()

    meduza.proved_mutaci(ptacek)