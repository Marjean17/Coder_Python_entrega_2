class Persona():
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    #Getters y setters
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_apellido(self):
        return self.__apellido
    def set_apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido

    #otros Metodos
    def saludar(self):
        print(f"Hola, mi nombre es {self.__nombre} y mi condición es la de {type(self).__name__}")

# --------------------------------------------------------------------------------------------------
class Cliente(Persona):
    def __init__(self, nombre, apellido, telefono, dni, estado=True):
        Persona.__init__(self, nombre, apellido) # Persona en lugar de super para no generar conflicto de MRO si quisiera implementar luego herencia múltiple
        self.__telefono = telefono
        self.__dni = dni
        self.__estado = True

    def __str__(self):
      return f"\n\rNombre: {self.get_nombre()}, Apellido: {self.get_apellido()}, Teléfono: {self.__telefono}, Dni: {self.__dni}, Estado: {self.__estado}"


    #Getters y setters
    def get_telefono(self):
        return self.__telefono
    def set_telefono(self, nuevo_telefono):
        self.__telefono = nuevo_telefono

    def get_dni(self):
        return self.__dni
    def set_dni(self, nuevo_dni):
        self.__dni = nuevo_dni

    def get_estado(self):
        return self.__estado
    def set_estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    #otros Metodos
    def saludar(self): # Sobreescribimos aplicando poliformismo
        print(f"Hola, mi nombre es {Persona.get_nombre(self)} y mi condición es la de {type(self).__name__}")


# --------------------------------------------------------------------------------------------------
class Empleado(Persona):
    def __init__(self, nombre, apellido, legajo, estado=True):
        Persona.__init__(self, nombre, apellido) # Persona en lugar de super para no generar conflicto de MRO si quisiera implementar luego herencia múltiple
        self.__legajo = 0000
        self.__estado = True

    def __str__(self):
      return f"\n\rNombre: {self.get_nombre()}, Apellido: {self.get_apellido()}, Legajo: {self.__legajo}, Estado: {self.__estado}"

    #Getters y setters
    def get_legajo(self):
        return self.__legajo
    def set_legajo(self, legajo):
        self.__legajo = legajo

    def get_estado(self):
        return self.__estado
    def set_estado(self, estado):
        self.__estado = estado

    #otros Metodos
    def saludar(self): # Sobreescribimos aplicando poliformismo
        print(f"""Hola, mi nombre es {Persona.get_nombre(self)} y mi condición es la de {type(self).__name__}
mi Legajo es el Nro: {Empleado.get_legajo(self)}""")