class Famosos:
    tipos = {"magos", "cientificos", "otros"}

    def __init__(self):
        self.personas = []

    def agregar_nombre(self, nombre, tipo):
        if tipo not in self.tipos:
            tipo = "otros"

        self.personas.append({
            "nombre": nombre,
            "tipo": tipo
        })

    def separar_nombres(self):
        magos = list(
            filter(lambda persona: persona["tipo"] == "magos", self.personas))
        cientificos = list(
            filter(lambda persona: persona["tipo"] == "cientificos", self.personas))
        otros = list(
            filter(lambda persona: persona["tipo"] == "otros", self.personas))
        return magos, cientificos, otros

    def hacer_grandioso(self, magos):
        magos_grandiosos = list(map(lambda persona: {
                                'nombre': 'El grandioso ' + persona["nombre"], 'tipo': persona["tipo"]}, magos))
        return magos_grandiosos

    def imprimir_nombres(self, nombres):
        for nombre in nombres:
            print(nombre['nombre'])


famoso = Famosos()
famoso.agregar_nombre("Harry Houdini", "magos")
famoso.agregar_nombre("Newton", "cientificos")
famoso.agregar_nombre("David Blaine", "magos")
famoso.agregar_nombre("Hawking", "cientificos")
famoso.agregar_nombre("Messi", "otros")
famoso.agregar_nombre("Teller", "magos")
famoso.agregar_nombre("Einstein", "cientificos")
famoso.agregar_nombre("Pele", "otros")
famoso.agregar_nombre("Juanes", "otros")

# Separamos los nombres en grupos
magos, cientificos, otros = famoso.separar_nombres()

# Modificamos los nombres de los magos grandiosos
magos_grandiosos = famoso.hacer_grandioso(magos)

# Imprimimos la lista completa de nombres antes de ser modificados
print("Lista completa de nombres: ")
famoso.imprimir_nombres(famoso.personas)
print()

# Imprimimos los nombres de los magos grandiosos
print("Magos grandiosos: ")
famoso.imprimir_nombres(magos_grandiosos)
print()

# Imprimimos los nombres de los científicos
print("Científicos: ")
famoso.imprimir_nombres(cientificos)
print()

# Imprimimos los nombres restantes
print("Otros: ")
famoso.imprimir_nombres(otros)
