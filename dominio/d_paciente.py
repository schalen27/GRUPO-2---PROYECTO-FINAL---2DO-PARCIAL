# Proyecto Segundo Parcial - GUI con Base de Datos
# Programación Orientada a Objetos
# Jornada: Matutina
# Grupo 2 - Sistema de Gestión de Servicios de Clínica
#Integrantes:
# 1. Bermeo Cevallos Jorge Alejandro
# 2. Caceres Medina Bolivar Santiago
# 3. Chalen Ochoa Shuska Akyra
# 4. Gonzalez Rodríguez Scarlet Anabella
# 5. Rivera Valdiviezo Ashley Daniela
# 6. Silva Parrales Jipson Alexander

class Paciente:
    def __init__(self, cedula, nombre, edad, telefono, genero):
        self._cedula = cedula
        self._nombre = nombre
        self._edad = edad
        self._telefono = telefono
        self._genero = genero

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        if valor == '':
            print('Error. Cédula inválida')
        else:
            self._cedula = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor == '':
            print('Error. Nombre inválido')
        else:
            self._nombre = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor <= 0:
            print('Error. Edad inválida')
        else:
            self._edad = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if valor == '':
            print('Error. Teléfono inválido')
        else:
            self._telefono = valor
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        if valor == '':
            print('Error. Género inválido')
        else:
            self._genero = valor

    def mostrar_info(self):
        return (
            f'Cédula: {self._cedula} | '
            f'Nombre: {self._nombre} | '
            f'Edad: {self._edad} | '
            f'Teléfono: {self._telefono} |'
            f'Genero: {self._genero}'
        )
    def __str__(self):
        return self.mostrar_info()