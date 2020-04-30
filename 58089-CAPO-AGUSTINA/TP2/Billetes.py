class Billete():

    def __init__(self):
        self.denominacion = 0
        self.moneda = None
        self.representacion = None


class Billete_100(Billete):

    def __init__(self):
        self.denominacion = 100
        self.moneda = "pesos"
        self.representacion = "$100"


class Billete_200(Billete):

    def __init__(self):
        self.denominacion = 200
        self.moneda = "pesos"
        self.representacion = "$200"


class Billete_500(Billete):

    def __init__(self):
        self.denominacion = 500
        self.moneda = "pesos"
        self.representacion = "$500"


class Billete_1000(Billete):

    def __init__(self):
        self.denominacion = 1000
        self.moneda = "pesos"
        self.representacion = "$1000"
