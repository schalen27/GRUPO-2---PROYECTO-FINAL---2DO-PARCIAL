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

import sys
import re

from PySide6.QtCore import (
    QRegularExpression,
    QDate,
    QTime
)
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox
)

from GUI.ui_vtn_principal import Ui_Sistema_de_Gestion_Servicios_Medicos
from Datos.conexion import conectar_bd


PATRON_EMAIL = r"^[\w\.-]+@[\w\.-]+\.\w+$"


class ServicioMedico:
    def __init__(
        self,
        nombre_servicio,
        costo_base,
        nombre,
        apellido,
        cedula,
        email
    ):
        self._nombre_servicio = nombre_servicio
        self._costo_base = costo_base
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._email = email

    @property
    def nombre_servicio(self):
        return self._nombre_servicio

    @property
    def costo_base(self):
        return self._costo_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def cedula(self):
        return self._cedula

    @property
    def email(self):
        return self._email

    def calcular_costo(self):
        return self._costo_base

    def mostrar_info(self):
        return (
            f"Servicio: {self._nombre_servicio}\n"
            f"Costo: ${self.calcular_costo():.2f}\n"
            f"Nombre: {self._nombre}\n"
            f"Apellido: {self._apellido}\n"
            f"Cédula: {self._cedula}\n"
            f"Email: {self._email}"
        )

    def __str__(self):
        return self.mostrar_info()


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Sistema_de_Gestion_Servicios_Medicos()
        self.ui.setupUi(self)

        # Mostrar fecha y hora actuales.
        self.actualizar_fecha_hora()

        # Evitar que fecha, hora y costo sean modificados.
        self.ui.date_fecha.setReadOnly(True)
        self.ui.time_hora.setReadOnly(True)
        self.ui.txt_costo_base.setReadOnly(True)

        self.configurar_validadores()
        self.conectar_controles()

        # Mostrar el costo del primer servicio al iniciar.
        self.actualizar_costo(
            self.ui.cmb_servicio.currentText()
        )

    def configurar_validadores(self):
        """Configura las validaciones de los campos."""

        # Nombre y apellido: letras, tildes, ñ y espacios.
        regex_texto = QRegularExpression(
            r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+"
        )

        validador_texto = QRegularExpressionValidator(
            regex_texto
        )

        self.ui.txt_nombre.setValidator(
            validador_texto
        )

        self.ui.txt_apellido_2.setValidator(
            validador_texto
        )

        # Cédula: máximo 10 números.
        regex_cedula = QRegularExpression(
            r"\d{0,10}"
        )

        validador_cedula = QRegularExpressionValidator(
            regex_cedula
        )

        self.ui.txt_cedula_2.setValidator(
            validador_cedula
        )

        self.ui.txt_cedula_2.setMaxLength(10)

    def conectar_controles(self):
        """Conecta los botones con sus funciones."""

        self.ui.btn_registrar.clicked.connect(
            self.registrar_datos
        )

        self.ui.btn_mostrar_informacion.clicked.connect(
            self.mostrar_informacion
        )

        self.ui.btn_actualizar.clicked.connect(
            self.actualizar_datos
        )

        self.ui.btn_eliminar.clicked.connect(
            self.eliminar_datos
        )

        self.ui.btn_limpiar.clicked.connect(
            self.limpiar
        )

        self.ui.cmb_servicio.currentTextChanged.connect(
            self.actualizar_costo
        )

    def actualizar_fecha_hora(self):
        """Muestra la fecha y la hora actuales."""

        self.ui.date_fecha.setDate(
            QDate.currentDate()
        )

        self.ui.time_hora.setTime(
            QTime.currentTime()
        )

    def actualizar_costo(self, nombre_servicio):
        """Coloca automáticamente el costo del servicio."""

        costos = {
            "MEDICINA GENERAL": 25.00,
            "OFTALMOLOGÍA": 35.00,
            "OFTAMOLOGÍA": 35.00,
            "CARDIOLOGÍA": 50.00,
            "ODONTOLOGÍA": 40.00,
            "PEDIATRÍA": 45.00,
            "LABORATORIO": 30.00,
            "FISIOTERAPIA": 28.00,
            "EMERGENCIAS": 60.00
        }

        costo = costos.get(
            nombre_servicio,
            0.00
        )

        self.ui.txt_costo_base.setText(
            f"{costo:.2f}"
        )

    def validar_cedula_busqueda(self):
        """Valida la cédula utilizada para buscar o eliminar."""

        cedula = self.ui.txt_cedula_2.text().strip()

        if len(cedula) != 10 or not cedula.isdigit():
            QMessageBox.warning(
                self,
                "Cédula incorrecta",
                "Ingrese una cédula de exactamente 10 números."
            )
            return None

        return cedula

    def obtener_datos_formulario(self):
        """Obtiene y valida los datos de la interfaz."""

        nombre_servicio = (
            self.ui.cmb_servicio.currentText().strip()
        )

        costo_texto = (
            self.ui.txt_costo_base.text().strip()
        )

        nombre = (
            self.ui.txt_nombre.text().strip()
        )

        apellido = (
            self.ui.txt_apellido_2.text().strip()
        )

        cedula = (
            self.ui.txt_cedula_2.text().strip()
        )

        email = (
            self.ui.txt_email_2.text().strip()
        )

        if not all([
            nombre_servicio,
            costo_texto,
            nombre,
            apellido,
            cedula,
            email
        ]):
            QMessageBox.warning(
                self,
                "Campos incompletos",
                "Todos los campos son obligatorios."
            )
            return None

        if len(cedula) != 10 or not cedula.isdigit():
            QMessageBox.warning(
                self,
                "Cédula incorrecta",
                "La cédula debe contener exactamente 10 números."
            )
            return None

        if not re.fullmatch(PATRON_EMAIL, email):
            QMessageBox.warning(
                self,
                "Correo incorrecto",
                "Ingrese un correo electrónico válido."
            )
            return None

        try:
            costo_base = float(costo_texto)

        except ValueError:
            QMessageBox.warning(
                self,
                "Costo incorrecto",
                "El costo del servicio no es válido."
            )
            return None

        if costo_base < 0:
            QMessageBox.warning(
                self,
                "Costo incorrecto",
                "El costo no puede ser negativo."
            )
            return None

        return ServicioMedico(
            nombre_servicio,
            costo_base,
            nombre,
            apellido,
            cedula,
            email
        )

    def registrar_datos(self):
        """Registra un servicio médico en SQL Server."""

        self.actualizar_fecha_hora()

        servicio = self.obtener_datos_formulario()

        if servicio is None:
            return

        conexion = None

        try:
            conexion = conectar_bd()
            cursor = conexion.cursor()

            cursor.execute("""
                INSERT INTO Registros
                (
                    Nombre_Servicio,
                    Costo_Base,
                    Nombre,
                    Apellido,
                    Cedula,
                    Email
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                servicio.nombre_servicio,
                servicio.costo_base,
                servicio.nombre,
                servicio.apellido,
                servicio.cedula,
                servicio.email
            )

            conexion.commit()

            QMessageBox.information(
                self,
                "Registro exitoso",
                "El servicio médico fue registrado correctamente."
            )

            self.limpiar()

        except Exception as error:
            if conexion is not None:
                conexion.rollback()

            QMessageBox.critical(
                self,
                "Error al registrar",
                str(error)
            )

        finally:
            if conexion is not None:
                conexion.close()

    def mostrar_informacion(self):
        """Busca un registro por cédula y carga sus datos."""

        cedula = self.validar_cedula_busqueda()

        if cedula is None:
            return

        conexion = None

        try:
            conexion = conectar_bd()
            cursor = conexion.cursor()

            cursor.execute("""
                SELECT
                    Nombre_Servicio,
                    Costo_Base,
                    Nombre,
                    Apellido,
                    Email
                FROM Registros
                WHERE Cedula = ?
            """, cedula)

            registro = cursor.fetchone()

            if registro is None:
                QMessageBox.information(
                    self,
                    "Registro no encontrado",
                    "No existe un registro con esa cédula."
                )
                return

            nombre_servicio = registro[0]
            costo_base = registro[1]
            nombre = registro[2]
            apellido = registro[3]
            email = registro[4]

            indice = self.ui.cmb_servicio.findText(
                nombre_servicio
            )

            if indice >= 0:
                self.ui.cmb_servicio.setCurrentIndex(
                    indice
                )

            self.ui.txt_costo_base.setText(
                f"{float(costo_base):.2f}"
            )

            self.ui.txt_nombre.setText(
                nombre
            )

            self.ui.txt_apellido_2.setText(
                apellido
            )

            self.ui.txt_email_2.setText(
                email
            )

            QMessageBox.information(
                self,
                "Información encontrada",
                "Los datos se cargaron correctamente."
            )

        except Exception as error:
            QMessageBox.critical(
                self,
                "Error al consultar",
                str(error)
            )

        finally:
            if conexion is not None:
                conexion.close()

    def actualizar_datos(self):
        """Actualiza un registro utilizando la cédula."""

        servicio = self.obtener_datos_formulario()

        if servicio is None:
            return

        respuesta = QMessageBox.question(
            self,
            "Confirmar actualización",
            "¿Está segura de que desea actualizar este registro?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if respuesta != QMessageBox.StandardButton.Yes:
            return

        conexion = None

        try:
            conexion = conectar_bd()
            cursor = conexion.cursor()

            cursor.execute("""
                UPDATE Registros
                SET
                    Nombre_Servicio = ?,
                    Costo_Base = ?,
                    Nombre = ?,
                    Apellido = ?,
                    Email = ?
                WHERE Cedula = ?
            """,
                servicio.nombre_servicio,
                servicio.costo_base,
                servicio.nombre,
                servicio.apellido,
                servicio.email,
                servicio.cedula
            )

            if cursor.rowcount == 0:
                conexion.rollback()

                QMessageBox.warning(
                    self,
                    "Registro no encontrado",
                    "No existe un registro con esa cédula."
                )
                return

            conexion.commit()

            QMessageBox.information(
                self,
                "Actualización exitosa",
                "El registro fue actualizado correctamente."
            )

            self.limpiar()

        except Exception as error:
            if conexion is not None:
                conexion.rollback()

            QMessageBox.critical(
                self,
                "Error al actualizar",
                str(error)
            )
        finally:
            if conexion is not None:
                conexion.close()

    def eliminar_datos(self):
        """Elimina un registro utilizando la cédula."""
        cedula = self.validar_cedula_busqueda()
        if cedula is None:
            return
        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            "¿Está segura de que desea eliminar este registro?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if respuesta != QMessageBox.StandardButton.Yes:
            return
        conexion = None
        try:
            conexion = conectar_bd()
            cursor = conexion.cursor()
            cursor.execute(
                "DELETE FROM Registros WHERE Cedula = ?",
                cedula
            )
            if cursor.rowcount == 0:
                conexion.rollback()
                QMessageBox.warning(
                    self,
                    "Registro no encontrado",
                    "No existe un registro con esa cédula."
                )
                return
            conexion.commit()
            QMessageBox.information(
                self,
                "Eliminación exitosa",
                "El registro fue eliminado correctamente."
            )
            self.limpiar()
        except Exception as error:
            if conexion is not None:
                conexion.rollback()
            QMessageBox.critical(
                self,
                "Error al eliminar",
                str(error)
            )
        finally:
            if conexion is not None:
                conexion.close()

    def limpiar(self):
        """Limpia los campos del formulario."""

        self.ui.txt_nombre.clear()
        self.ui.txt_apellido_2.clear()
        self.ui.txt_cedula_2.clear()
        self.ui.txt_email_2.clear()

        self.ui.cmb_servicio.setCurrentIndex(0)

        self.actualizar_costo(
            self.ui.cmb_servicio.currentText()
        )
        self.actualizar_fecha_hora()
        self.ui.txt_cedula_2.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())