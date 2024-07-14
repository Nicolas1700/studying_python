class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(
            color, ruedas
        )  # utilizamos super() sin self en lugar de Vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(
            self.velocidad, self.cilindrada
        )


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


coche = Coche("verde con negro", 4, 350, 1100)
bicicleta = Bicicleta("Negro", 2, "todo terreno")
camioneta = Camioneta("Verde oscuro", 4, 240, 990, 1000)
motocicleta = Motocicleta("Verde oscuro", 2, "todo terreno", 400, 1000)

# print("coche:", coche)
# print("bicicleta:", bicicleta)
# print("camioneta:", camioneta)
# print("motocicleta:", motocicleta)


def catalogar(vehiculos, ruedas=None):
    cantidadVehConRuedas = 0
    for veh in vehiculos:
        if ruedas == None:
            valuesInClass(veh)
        else:
            if veh.ruedas == ruedas:
                cantidadVehConRuedas = cantidadVehConRuedas + 1
                valuesInClass(veh)
    if ruedas != None:
        print(
            f"Se han encontrado {cantidadVehConRuedas} vehículos con {ruedas} ruedas:"
        )


def valuesInClass(veh):
    print("Clase: ", type(veh).__name__)
    print("Color: ", veh.color)
    print("Ruedas: ", veh.ruedas)
    if isinstance(veh, Coche) or isinstance(veh, Motocicleta):
        print("Velocidad: ", veh.velocidad)
        print("Cilindrada: ", veh.cilindrada)
    if isinstance(veh, Bicicleta):
        print("Tipo: ", veh.tipo)
    if isinstance(veh, Camioneta):
        print("Carga: ", veh.carga)
    print("\n")


vehiculos = [coche, bicicleta, camioneta, motocicleta]
catalogar(vehiculos)
