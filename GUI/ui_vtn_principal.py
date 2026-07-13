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


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTimeEdit,
    QWidget)

class Ui_Sistema_de_Gestion_Servicios_Medicos(object):
    def setupUi(self, Sistema_de_Gestion_Servicios_Medicos):
        if not Sistema_de_Gestion_Servicios_Medicos.objectName():
            Sistema_de_Gestion_Servicios_Medicos.setObjectName(u"Sistema_de_Gestion_Servicios_Medicos")
        Sistema_de_Gestion_Servicios_Medicos.resize(1002, 600)
        self.centralwidget = QWidget(Sistema_de_Gestion_Servicios_Medicos)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_registrar = QPushButton(self.centralwidget)
        self.btn_registrar.setObjectName(u"btn_registrar")
        self.btn_registrar.setGeometry(QRect(60, 340, 111, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        font.setBold(True)
        self.btn_registrar.setFont(font)
        self.btn_registrar.setStyleSheet(u"QPushButton{\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45A049;\n"
"}")
        self.btn_limpiar = QPushButton(self.centralwidget)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setGeometry(QRect(670, 430, 111, 31))
        self.btn_limpiar.setFont(font)
        self.btn_limpiar.setStyleSheet(u"QPushButton{\n"
"    background-color: #757575;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #616161;\n"
"}")
        self.btn_mostrar_informacion = QPushButton(self.centralwidget)
        self.btn_mostrar_informacion.setObjectName(u"btn_mostrar_informacion")
        self.btn_mostrar_informacion.setGeometry(QRect(330, 380, 211, 31))
        self.btn_mostrar_informacion.setFont(font)
        self.btn_mostrar_informacion.setStyleSheet(u"QPushButton{\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #1976D2;\n"
"}")
        self.lbl_titulo = QLabel(self.centralwidget)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        self.lbl_titulo.setGeometry(QRect(220, 40, 451, 20))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.lbl_titulo.setFont(font1)
        self.gb_paciente = QGroupBox(self.centralwidget)
        self.gb_paciente.setObjectName(u"gb_paciente")
        self.gb_paciente.setGeometry(QRect(10, 120, 461, 191))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.gb_paciente.setFont(font2)
        self.lbl_nombre = QLabel(self.gb_paciente)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(10, 70, 71, 21))
        self.lbl_nombre.setFont(font)
        self.txt_nombre = QLineEdit(self.gb_paciente)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(80, 70, 341, 21))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.txt_nombre.setFont(font3)
        self.txt_nombre.setMaxLength(60)
        self.lbl_apellido = QLabel(self.gb_paciente)
        self.lbl_apellido.setObjectName(u"lbl_apellido")
        self.lbl_apellido.setGeometry(QRect(10, 110, 81, 21))
        self.lbl_apellido.setFont(font)
        self.txt_apellido_2 = QLineEdit(self.gb_paciente)
        self.txt_apellido_2.setObjectName(u"txt_apellido_2")
        self.txt_apellido_2.setGeometry(QRect(90, 110, 331, 21))
        self.txt_apellido_2.setFont(font3)
        self.lbl_cedula = QLabel(self.gb_paciente)
        self.lbl_cedula.setObjectName(u"lbl_cedula")
        self.lbl_cedula.setGeometry(QRect(10, 30, 61, 21))
        self.lbl_cedula.setFont(font)
        self.txt_cedula_2 = QLineEdit(self.gb_paciente)
        self.txt_cedula_2.setObjectName(u"txt_cedula_2")
        self.txt_cedula_2.setGeometry(QRect(70, 30, 221, 21))
        self.txt_cedula_2.setFont(font3)
        self.lbl_email = QLabel(self.gb_paciente)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(10, 150, 61, 20))
        self.lbl_email.setFont(font)
        self.txt_email_2 = QLineEdit(self.gb_paciente)
        self.txt_email_2.setObjectName(u"txt_email_2")
        self.txt_email_2.setGeometry(QRect(60, 150, 361, 21))
        self.txt_email_2.setFont(font3)
        self.btn_actualizar = QPushButton(self.centralwidget)
        self.btn_actualizar.setObjectName(u"btn_actualizar")
        self.btn_actualizar.setGeometry(QRect(60, 430, 111, 31))
        self.btn_actualizar.setFont(font)
        self.btn_actualizar.setStyleSheet(u"QPushButton{\n"
"    background-color: #FF9800;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #F57C00;\n"
"}")
        self.btn_eliminar = QPushButton(self.centralwidget)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setGeometry(QRect(670, 340, 111, 31))
        self.btn_eliminar.setFont(font)
        self.btn_eliminar.setStyleSheet(u"QPushButton{\n"
"    background-color: #E53935;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #C62828;\n"
"}")
        self.gb_servicio = QGroupBox(self.centralwidget)
        self.gb_servicio.setObjectName(u"gb_servicio")
        self.gb_servicio.setGeometry(QRect(500, 120, 391, 191))
        self.gb_servicio.setFont(font2)
        self.lbl_servicio_nombre = QLabel(self.gb_servicio)
        self.lbl_servicio_nombre.setObjectName(u"lbl_servicio_nombre")
        self.lbl_servicio_nombre.setGeometry(QRect(10, 70, 171, 20))
        self.lbl_servicio_nombre.setFont(font)
        self.lbl_costo_base = QLabel(self.gb_servicio)
        self.lbl_costo_base.setObjectName(u"lbl_costo_base")
        self.lbl_costo_base.setGeometry(QRect(10, 110, 91, 21))
        self.lbl_costo_base.setFont(font)
        self.txt_costo_base = QLineEdit(self.gb_servicio)
        self.txt_costo_base.setObjectName(u"txt_costo_base")
        self.txt_costo_base.setGeometry(QRect(110, 110, 81, 21))
        self.txt_costo_base.setFont(font3)
        self.txt_costo_base.setMaxLength(4)
        self.txt_costo_base.setReadOnly(True)
        self.cmb_servicio = QComboBox(self.gb_servicio)
        self.cmb_servicio.addItem("")
        self.cmb_servicio.addItem("")
        self.cmb_servicio.addItem("")
        self.cmb_servicio.addItem("")
        self.cmb_servicio.addItem("")
        self.cmb_servicio.addItem("")
        self.cmb_servicio.addItem("")
        self.cmb_servicio.addItem("")
        self.cmb_servicio.setObjectName(u"cmb_servicio")
        self.cmb_servicio.setGeometry(QRect(170, 70, 171, 22))
        self.cmb_servicio.setFont(font3)
        self.label = QLabel(self.gb_servicio)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 110, 16, 21))
        font4 = QFont()
        font4.setPointSize(10)
        self.label.setFont(font4)
        self.lbl_fecha = QLabel(self.gb_servicio)
        self.lbl_fecha.setObjectName(u"lbl_fecha")
        self.lbl_fecha.setGeometry(QRect(10, 30, 51, 20))
        self.lbl_fecha.setFont(font4)
        self.date_fecha = QDateEdit(self.gb_servicio)
        self.date_fecha.setObjectName(u"date_fecha")
        self.date_fecha.setGeometry(QRect(60, 30, 110, 22))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(10)
        self.date_fecha.setFont(font5)
        self.lbl_hora = QLabel(self.gb_servicio)
        self.lbl_hora.setObjectName(u"lbl_hora")
        self.lbl_hora.setGeometry(QRect(190, 30, 47, 21))
        self.lbl_hora.setFont(font4)
        self.time_hora = QTimeEdit(self.gb_servicio)
        self.time_hora.setObjectName(u"time_hora")
        self.time_hora.setGeometry(QRect(240, 30, 101, 22))
        self.time_hora.setFont(font3)
        Sistema_de_Gestion_Servicios_Medicos.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Sistema_de_Gestion_Servicios_Medicos)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1002, 21))
        Sistema_de_Gestion_Servicios_Medicos.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Sistema_de_Gestion_Servicios_Medicos)
        self.statusbar.setObjectName(u"statusbar")
        Sistema_de_Gestion_Servicios_Medicos.setStatusBar(self.statusbar)

        self.retranslateUi(Sistema_de_Gestion_Servicios_Medicos)

        QMetaObject.connectSlotsByName(Sistema_de_Gestion_Servicios_Medicos)
    # setupUi

    def retranslateUi(self, Sistema_de_Gestion_Servicios_Medicos):
        Sistema_de_Gestion_Servicios_Medicos.setWindowTitle(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"MainWindow", None))
        self.btn_registrar.setText(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"REGISTRAR", None))
        self.btn_limpiar.setText(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"LIMPIAR", None))
        self.btn_mostrar_informacion.setText(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"MOSTRAR REGISTROS", None))
        self.lbl_titulo.setText(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"SISTEMA DE GESTI\u00d3N DE SERVICIOS M\u00c9DICOS", None))
        self.gb_paciente.setTitle(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"DATOS DEL PACIENTE:", None))
        self.lbl_nombre.setText(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"NOMBRES:", None))
        self.lbl_apellido.setText(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"APELLIDOS:", None))
        self.lbl_cedula.setText(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"C\u00c9DULA:", None))
        self.lbl_email.setText(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"EMAIL:", None))
        self.btn_actualizar.setText(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"ACTUALIZAR", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"ELIMINAR", None))
        self.gb_servicio.setTitle(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"DATOS DEL SERVICIO:", None))
        self.lbl_servicio_nombre.setText(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"NOMBRE DEL SERVICIO:", None))
        self.lbl_costo_base.setText(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"COSTO BASE:", None))
        self.txt_costo_base.setText("")
        self.cmb_servicio.setItemText(0, QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"MEDICINA GENERAL", None))
        self.cmb_servicio.setItemText(1, QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"OFTALMOLOG\u00cdA", None))
        self.cmb_servicio.setItemText(2, QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"CARDIOLOG\u00cdA", None))
        self.cmb_servicio.setItemText(3, QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"ODONTOLOG\u00cdA", None))
        self.cmb_servicio.setItemText(4, QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"PEDIATR\u00cdA", None))
        self.cmb_servicio.setItemText(5, QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"LABORATORIO", None))
        self.cmb_servicio.setItemText(6, QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"FISIOTERAPIA", None))
        self.cmb_servicio.setItemText(7, QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"EMERGENCIAS", None))

        self.label.setText(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"$", None))
        self.lbl_fecha.setText(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"FECHA:", None))
        self.lbl_hora.setText(QCoreApplication.translate("Sistema_de_Gestion_Servicios_Medicos", u"HORA:", None))
    # retranslateUi

