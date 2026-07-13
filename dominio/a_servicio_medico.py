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

class ServicioMedico:

    def __init__(self, codigo, nombre_servicio, costo_base, paciente):
        self._codigo = codigo
        self._nombre_servicio = nombre_servicio
        self._costo_base = costo_base
        self._paciente = paciente

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor == '':
            print('Error. Código inválido')
        else:
            self._codigo = valor

    @property
    def nombre_servicio(self):
        return self._nombre_servicio

    @nombre_servicio.setter
    def nombre_servicio(self, valor):
        if valor == '':
            print('Error. Nombre inválido del servicio')
        else:
            self._nombre_servicio = valor

    @property
    def costo_base(self):
        return self._costo_base

    @costo_base.setter
    def costo_base(self, valor):
        if valor < 0:
            print('Costo inválido')
        else:
            self._costo_base = valor

    @property
    def paciente(self):
        return self._paciente

    @paciente.setter
    def paciente(self, valor):
        if valor == '':
            print('Error. El paciente no está registrado.')
        else:
            self._paciente = valor

    def calcular_costo(self):
        return self._costo_base

    def mostrar_info(self):
        return (
            f'Código: {self._codigo} | '
            f'Servicio: {self._nombre_servicio} | '
            f'Costo: ${self.calcular_costo()} |'
            f'Paciente: {self._paciente}'
        )

    def __str__(self):
        return self.mostrar_info()