class perro:

    listaPerros = []

    def __init__(self) -> None:
        print()
        
    def crear(self, nombre):
        self.listaPerros.append(nombre)
        
    def borrar(self, nombre):
        self.listaPerros.remove(nombre)

    def editar(self, name, numero):
        self.listaPerros[numero] = name

    def leer(self):
        print(self.listaPerros)

d = perro()

d.crear('Monti')
d.crear('Luck')
d.crear('Lucas')

d.leer()

d.borrar('Luck')

d.leer()

d.editar('Sam', 1)

d.leer()