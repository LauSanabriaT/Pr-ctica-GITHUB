class Paciente:
    def __init__(self, nombre="", cedula=0, genero="", servicio=""):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__genero = genero
        self.__servicio = servicio

    def obtener_nombre(self):
        return self.__nombre

    def obtener_cedula(self):
        return self.__cedula

    def obtener_genero(self):
        return self.__genero

    def obtener_servicio(self):
        return self.__servicio

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def establecer_cedula(self, cedula):
        self.__cedula = cedula

    def establecer_genero(self, genero):
        self.__genero = genero

    def establecer_servicio(self, servicio):
        self.__servicio = servicio

class Sistema:
    def __init__(self):
        self.__pacientes = []

    def agregar_paciente(self):
        nombre = input("Ingrese el nombre: ")
        cedula = self.__solicitar_cedula()
        
        if any(paciente.obtener_cedula() == cedula for paciente in self.__pacientes):
            print("Ya existe un paciente con esta cédula.")
            return

        genero = input("Ingrese el género: ")
        servicio = input("Ingrese el servicio: ")

        paciente = Paciente(nombre, cedula, genero, servicio)
        self.__pacientes.append(paciente)
        print("Paciente agregado exitosamente.")

    def __solicitar_cedula(self):
        while True:
            try:
                return int(input("Ingrese la cédula: "))
            except ValueError:
                print("Ingrese valores numéricos.")

    def mostrar_datos_paciente(self):
        cedula = self.__solicitar_cedula()
        encontrado = False

        for paciente in self.__pacientes:
            if paciente.obtener_cedula() == cedula:
                print(f"""
    Nombre: {paciente.obtener_nombre()}
    Cédula: {paciente.obtener_cedula()}
    Género: {paciente.obtener_genero()}
    Servicio: {paciente.obtener_servicio()}
    """)
                encontrado = True
                break

        if not encontrado:
            print(f"No se ha encontrado un paciente con la cédula: {cedula}")

    def contar_pacientes(self):
        return len(self.__pacientes)

sistema = Sistema()

while True:
    try:
        opcion = int(input("""
1. Agregar paciente
2. Ver datos paciente
3. Ver número de pacientes
4. Salir
Elija una opción: """))

        if opcion == 1:
            sistema.agregar_paciente()
        elif opcion == 2:
            sistema.mostrar_datos_paciente()
        elif opcion == 3:
            print(f"Número de pacientes: {sistema.contar_pacientes()}")
        elif opcion == 4:
            print("Fin del programa.")
            break
        else:
            print("Ingrese una opción válida.")
    except ValueError:
        print("Ingrese un número válido.")
