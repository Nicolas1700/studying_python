class A:
    def __init__(self):
        print("Soy de clase A")


class B:
    def __init__(self):
        print("Soy de clase B")

# La clase B tiene prioridad
class C(B,A):
    pass

prueba = C() # Se imprimira lo de la clase B