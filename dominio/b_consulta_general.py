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

from a_servicio_medico import ServicioMedico

class ConsultaGeneral(ServicioMedico):
    def __init__(self, codigo, nombre_servicio, costo_base, paciente, especialidad, duracion, nivel_urgencia):
        super().__init__(codigo, nombre_servicio, costo_base, paciente)

        self._especialidad = especialidad
        self._duracion = duracion
        self._nivel_urgencia = nivel_urgencia
    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):
        if valor == '':
            print('Error. Especialidad inválida')
        else:
            self._especialidad = valor

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, valor):
        if valor <= 0:
            print('Error. Duración inválida')
        else:
            self._duracion = valor

    @property
    def nivel_urgencia(self):
        return self._nivel_urgencia

    @nivel_urgencia.setter
    def nivel_urgencia(self, valor):
        if valor == '':
            print('Error. Nivel de urgencia inválido')
        else:
            self._nivel_urgencia = valor

    def calcular_costo(self):
        return self._costo_base + (self._duracion * 0.5)

    def mostrar_info(self):
        return (
            f'{super().mostrar_info()} | '
            f'Especialidad: {self._especialidad} | '
            f'Duración: {self._duracion} min | '
            f'Urgencia: {self._nivel_urgencia}'
        )

    def __str__(self):
        return self.mostrar_info()