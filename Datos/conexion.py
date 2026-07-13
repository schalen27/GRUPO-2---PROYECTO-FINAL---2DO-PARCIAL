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

import pyodbc

def conectar_bd():
    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=.\\SQLCHALENSHUSKAO;"
        "DATABASE=ClinicaMedica;"
        "Trusted_Connection=yes;"
    )
    return conexion