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

class ExamenLaboratorio(ServicioMedico):

    def __init__(self, codigo, nombre_servicio, costo_base, paciente, tipo_analisis, requiere_urgencia, numero_muestras):
        super().__init__(codigo, nombre_servicio, costo_base, paciente)

        self._tipo_analisis = tipo_analisis
        self._requiere_urgencia = requiere_urgencia
        self._numero_muestras = numero_muestras

    @property
    def tipo_analisis(self):
        return self._tipo_analisis

    @tipo_analisis.setter
    def tipo_analisis(self, valor):
        if valor == '':
            print('Error. Tipo de análisis inválido')
        else:
            self._tipo_analisis = valor

    @property
    def requiere_urgencia(self):
        return self._requiere_urgencia

    @requiere_urgencia.setter
    def requiere_urgencia(self, valor):
        if valor == '':
            print ('Error. Urgencia inválida')
        else:
            self._requiere_urgencia = valor

    @property
    def numero_muestras(self):
        return self._numero_muestras

    @numero_muestras.setter
    def numero_muestras(self, valor):
        if valor <= 0:
            print('Error. Número de muestras inválido')
        else:
            self._numero_muestras = valor

    def calcular_costo(self):
        recargo = 1.5 if self._requiere_urgencia.lower() == 'alta' else 1.0
        return self._costo_base * recargo

    def mostrar_info(self):
        return (
            f'{super().mostrar_info()} | '
            f'Código: {self._codigo} | '
            f'Servicio: {self._nombre_servicio} | '
            f'Costo: ${self.calcular_costo():.2f} | '
            f'Paciente: {self._paciente} | '
            f'Tipo de análisis: {self._tipo_analisis} | '
            f'Muestras: {self._numero_muestras} | '
            f'Urgente: {self._requiere_urgencia}'
        )

    def __str__(self):
        return self.mostrar_info()