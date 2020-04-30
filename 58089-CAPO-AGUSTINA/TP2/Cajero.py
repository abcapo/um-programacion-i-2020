from Billete import (Billete_100, Billete_200, Billete_500, Billete_1000)
import math


class Cajero_Automatico():

    def __init__(self):
        self.billete100 = []
        self.billete200 = []
        self.billete500 = []
        self.billete1000 = []

    def Agregar_Dinero(self, listado_billetes):
        for i in listado_billetes:
            if i.denominacion == 100:
                self.billete100.append(i)
            elif i.denominacion == 200:
                self.billete200.append(i)
            elif i.denominacion == 500:
                self.billete500.append(i)
            elif i.denominacion == 1000:
                self.billete1000.append(i)

    def Contar_Dinero(self):
        self.total = 0
        B100 = len(self.billete100) * 100
        B200 = len(self.billete200) * 200
        B500 = len(self.billete500) * 500
        B1000 = len(self.billete1000) * 1000
        self.total = B1000 + B500 + B200 + B100
        return(B1000, B500, B200, B100, self.total)

    def Extraer_Dinero(self, monto):
        disponible = [len(self.billete1000), len(self.billete500),
                        len(self.billete200), len(self.billete100)]
        '''if percentage < 100 or percentage > 0:
            percentage = math.trunc(monto * percentage / 100)
            monto = monto - percentage'''
        retiro = 0
        cant = 0
        i = 0
        if monto <= self.total:
            if monto % 100 == 0:
                cant = monto//1000
                if cant <= disponible[0]:
                    for i in range(cant):
                        disponible[0] -= 1
                    retiro = cant * 1000
                    monto -= cant * 1000
                cant = monto//500
                if cant <= disponible[1]:
                    i = 0
                    for i in range(cant):
                        disponible[1] -= 1
                    retiro += cant * 500
                    monto -= cant * 500
                cant = monto//200
                if cant <= disponible[2]:
                    i = 0
                    for i in range(cant):
                        disponible[2] -= 1
                    retiro += cant * 200
                    monto -= cant * 200
                cant = monto//100
                if cant <= disponible[3]:
                    i = 0
                    for i in range(cant):
                        disponible[3] -= 1
                    retiro += cant * 100
                print("Dinero extraidos ", retiro)
            else:
                print("Monto no válido, ingrese monto multiplo de 100")
        else:
            print("Monto no válido, ingrese un monto menor")

    def Extraer_Cambio(self, monto, percentage):
        disponible = [len(self.billete1000), len(self.billete500),
                        len(self.billete200), len(self.billete100)]
        cambio = 0
        retiro = 0
        rcambio = 0
        if monto <= self.total:
            if percentage < 100 or percentage > 0:
                if monto % 100 == 0:
                    percentage = math.trunc(monto * percentage / 100)
                    while percentage % 100 != 0:
                        percentage += 10
                    cambio = percentage
                    monto -= cambio
                    cant = monto//1000
                    if cant <= disponible[0]:
                        for i in range(cant):
                            disponible[0] -= 1
                        retiro = cant * 1000
                        monto -= cant * 1000
                    cant = monto//500
                    if cant <= disponible[1]:
                        i = 0
                        for i in range(cant):
                            disponible[1] -= 1
                        retiro += cant * 500
                        monto -= cant * 500
                    cant = monto//200
                    if cant <= disponible[2]:
                        i = 0
                        for i in range(cant):
                            disponible[2] -= 1
                        retiro += cant * 200
                        monto -= cant * 200
                    cant = monto//100
                    if cant <= disponible[3]:
                        i = 0
                        for i in range(cant):
                            disponible[3] -= 1
                        retiro += cant * 100
                    print("Dinero extraidos ", retiro)

                    while cambio != 0:
                        cant = cambio//100
                        cant1 = cant
                        while cant1 != 0 or disponible[3] != 0:
                            i = 0
                            for i in range(cant):
                                disponible[3] -= 1
                                cant1 -= 1
                            rcambio += cant * 100
                            cambio -= cant * 100
                            break

                        cant = cambio//200
                        cant1 = cant
                        while cant1 != 0 or disponible[2] != 0:
                            i = 0
                            for i in range(cant):
                                disponible[2] -= 1
                                cant1 -= 1
                            rcambio += cant * 200
                            cambio -= cant * 200
                            break
                        cant = cambio//500
                        cant1 = cant
                        while cant1 != 0 or disponible[1] != 0:
                            i = 0
                            for i in range(cant):
                                disponible[1] -= 1
                                cant1 -= 1
                            rcambio += cant * 500
                            cambio -= cant * 500
                            break
                        cant = cambio//1000
                        cant1 = cant
                        while cant1 != 0 or disponible[0] != 0:
                            i = 0
                            for i in range(cant):
                                disponible[0] -= 1
                                cant1 -= 1
                            rcambio += cant * 1000
                            cambio -= cant * 1000
                            break
                        break
                    print("Dinero extraidos", rcambio)
                else:
                    print("Monto no válido, ingrese monto multiplo de 100")
            else:
                print("El porcentaje ingresado es incorrecto")
        else:
            print("Monto no válido, ingrese un monto menor")
