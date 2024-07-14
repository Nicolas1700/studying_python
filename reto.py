import math


class punto:
    def __init__(self, coordenada_x=0, coordenada_y=0):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y

    def __str__(self):
        return f"({self.coordenada_x},{self.coordenada_y})"

    def cuadrante(self):
        if self.coordenada_x == 0 & self.coordenada_y == 0:
            return "Origen"
        # El cuadrante es de lado  derecho
        if self.coordenada_x > 0:
            if self.coordenada_y > 0:
                return "Cuadrante #1"
            return "Cuadrante #4"
        else:  # El cuadrante es de lado izquierdo
            if self.coordenada_y > 0:
                return "Cuadrante #2"
            return "Cuadrante #3"

    def vector(self, coordenada2_x, coordenada2_y):
        x = coordenada2_x - self.coordenada_x
        y = coordenada2_y - self.coordenada_y
        return f"({x},{y})"

    def distancia(self, coordenada2_x, coordenada2_y):
        d = math.sqrt(
            (coordenada2_x - self.coordenada_x) ** 2
            + (coordenada2_y - self.coordenada_y) ** 2
        )
        return f"Distancia: {d}"


A = punto(2, 3)
B = punto(5, 5)
C = punto(-3, -1)
D = punto(0, 0)

# print(A.distancia(D.coordenada_x, D.coordenada_y))
# print(B.distancia(D.coordenada_x, D.coordenada_y))
# print(C.distancia(D.coordenada_x, D.coordenada_y))

# print(A.distancia(B.coordenada_x, B.coordenada_y))
# print(B.distancia(A.coordenada_x, A.coordenada_y))

# print(A.vector(B.coordenada_x, B.coordenada_y))
# print(B.vector(A.coordenada_x, A.coordenada_y))

# print(A.cuadrante())
# print(C.cuadrante())
# print(D.cuadrante())


class Rectangulo:
    def __init__(self, inicial=punto(), final=punto()):
        self.inicial = inicial
        self.final = final

    def base(self):
        return abs(self.inicial.coordenada_x - self.final.coordenada_x)

    def altura(self):
        return abs(self.inicial.coordenada_y - self.final.coordenada_y)

    def area(self):
        return self.base() * self.altura()


rect = Rectangulo(A, B)
print("base:", rect.base())
print("altura:", rect.altura())
print("area:", rect.area())
