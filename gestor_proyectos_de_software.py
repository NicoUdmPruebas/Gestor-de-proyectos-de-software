from dataclasses import dataclass

@dataclass
class Colaborador:
    nombre: str
    email: str

class Proyecto:
    def __init__(self, nombre: str, lenguaje: str) -> None:
        self.nombre = nombre
        self.lenguaje = lenguaje
        self.colaboradores: list[Colaborador] = []

    def agregar_colaborador(self, colaborador: Colaborador) -> None | str:
        if colaborador not in self.colaboradores:
            self.colaboradores.append(colaborador)
        else:
            return f'Ya existe el colaborador {colaborador.nombre}' 

    def listar_colaboradores(self) -> list[Colaborador]:
        return self.colaboradores

    def tiene_colaborador(self, nombre_colaborador: str) -> bool:
        for colaborador_lista in self.colaboradores:
            if nombre_colaborador == colaborador_lista.nombre:
                return True
        return False
        
    def __str__(self) -> str:
        return f'Proyecto: {self.nombre} [{self.lenguaje}] - {len(self.colaboradores)} colaborador(es)'

class GestorProyectos:
    def __init__(self) -> None:
        self.proyectos: list[Proyecto] = []

    def registrar_proyecto(self, proyecto: Proyecto) -> None | str:
        if proyecto not in self.proyectos:
            self.proyectos.append(proyecto)
        else: 
            return f'Ya existe el proyecto {proyecto.nombre}' 

    def buscar_proyecto(self, nombre_proyecto: str) -> Proyecto | None:
        for proyecto in self.proyectos:
            if nombre_proyecto == proyecto.nombre: # Corrección: comparar con el atributo nombre
                return proyecto
        return None

    def listar_proyectos(self) -> list[Proyecto]:
        return self.proyectos
    

ana   = Colaborador("ana_dev", "ana@mail.com")
luis  = Colaborador("luis99",  "luis@mail.com")
sofia = Colaborador("sofiaml", "sofia@mail.com")

# Proyectos
p1 = Proyecto(nombre="InventarioApp", lenguaje="Python")
p1.agregar_colaborador(ana)
p1.agregar_colaborador(luis)
p1.agregar_colaborador(ana)   # aviso: ya existe

p2 = Proyecto(nombre="WebStore", lenguaje="JavaScript")
p2.agregar_colaborador(sofia)

# __str__
print(p1)  # Proyecto: InventarioApp [Python] — 2 colaborador(es)
print(p2)  # Proyecto: WebStore [JavaScript] — 1 colaborador(es)

# tiene_colaborador
print(p1.tiene_colaborador("ana_dev"))  # True
print(p1.tiene_colaborador("sofiaml"))  # False

# Gestor
gestor = GestorProyectos()
gestor.registrar_proyecto(p1)
gestor.registrar_proyecto(p2)
gestor.registrar_proyecto(p1)  # aviso: ya existe

encontrado = gestor.buscar_proyecto("WebStore")
print(encontrado)  # Proyecto: WebStore [JavaScript] — 1 colaborador(es)

no_existe = gestor.buscar_proyecto("OtroProyecto")
print(no_existe)   # None

print(len(gestor.listar_proyectos()))  # 2