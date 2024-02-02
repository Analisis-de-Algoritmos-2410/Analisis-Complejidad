import random


class Persona:
    id: int
    nombre: str
    edad: int
    impuestos: bool

    def __init__(self, id):
        paga = [True, True, False, False, True]
        self.edad = random.randint(18, 99)
        self.impuestos = random.choice(paga)
        self.nombre = ''.join([chr(random.randint(65, 89)) for _ in range(4)])
        self.id = id

    def __str__(self):
        return f"ID: {self.id} - Nombre: {self.nombre} - Edad: {self.edad} - Impuestos [Y/N] {'Y' if self.impuestos else 'N' }"

    @staticmethod
    def generar_censo(n):
        censo = []
        for i in range(n):
            censo.append(Persona(i))
        return censo
