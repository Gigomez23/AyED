"""
archivo: ejercisio3.py
descripcion: Este archivo contiene la implementación de una interfaz gráfica para la gestión de donantes de sangre.
Segun el ejercicio 3 de la guia. 
"""

import customtkinter as ctk
from tkinter import messagebox
from models.pila_hospital import PilaDonantes


class DonacionSangreFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Tipos de sangre comunes
        self.tipos_sangre = [
            "O+", "O-",
            "A+", "A-",
            "B+", "B-",
            "AB+", "AB-"
        ]

        self.pila = PilaDonantes()
        self._crear_interfaz()

    def _crear_interfaz(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Título
        titulo = ctk.CTkLabel(
            self,
            text="Campaña de Donación de Sangre - Estelí",
            font=("Arial", 18, "bold"),
            text_color="#8B0000"  # Color rojo sangre
        )
        titulo.grid(row=0, column=0, pady=15, sticky="n")

        # Marco principal
        marco_principal = ctk.CTkFrame(self)
        marco_principal.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        marco_principal.grid_columnconfigure(0, weight=1)

        # Formulario de registro
        marco_formulario = ctk.CTkFrame(marco_principal)
        marco_formulario.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # Nombre
        ctk.CTkLabel(marco_formulario, text="Nombre completo:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nombre = ctk.CTkEntry(marco_formulario, width=250)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        # Cédula
        ctk.CTkLabel(marco_formulario, text="Cédula:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_cedula = ctk.CTkEntry(marco_formulario)
        self.entry_cedula.grid(row=1, column=1, padx=5, pady=5)

        # Tipo de sangre
        ctk.CTkLabel(marco_formulario, text="Tipo de sangre:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.combo_sangre = ctk.CTkComboBox(
            marco_formulario,
            values=self.tipos_sangre,
            state="readonly"
        )
        self.combo_sangre.grid(row=2, column=1, padx=5, pady=5)
        self.combo_sangre.set("O+")  # Valor por defecto

        # Botón registrar
        btn_registrar = ctk.CTkButton(
            marco_formulario,
            text="Registrar Donante",
            command=self._registrar_donante,
            fg_color="#8B0000",
            hover_color="#A52A2A"
        )
        btn_registrar.grid(row=3, column=0, columnspan=2, pady=10)

        # Marco de acciones
        marco_acciones = ctk.CTkFrame(marco_principal)
        marco_acciones.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        # Botón revertir
        btn_revertir = ctk.CTkButton(
            marco_acciones,
            text="Revertir Último (Problema Técnico)",
            command=self._revertir_ultimo,
            fg_color="#B22222",
            hover_color="#CD5C5C"
        )
        btn_revertir.pack(side="left", padx=5)

        # Botón ver actual
        btn_ver = ctk.CTkButton(
            marco_acciones,
            text="Ver Donante Actual",
            command=self._ver_actual,
            fg_color="#DC143C"
        )
        btn_ver.pack(side="left", padx=5)

        # Lista de donantes
        marco_lista = ctk.CTkFrame(marco_principal)
        marco_lista.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        marco_lista.grid_columnconfigure(0, weight=1)
        marco_lista.grid_rowconfigure(0, weight=1)

        ctk.CTkLabel(
            marco_lista,
            text="Donantes registrados (último primero):",
            font=("Arial", 12)
        ).grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.texto_donantes = ctk.CTkTextbox(
            marco_lista,
            wrap="word",
            state="disabled",
            font=("Arial", 12)
        )
        self.texto_donantes.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        # Barra de estado
        self.estado = ctk.StringVar(value="Sistema listo para registrar donantes")
        barra_estado = ctk.CTkLabel(
            self,
            textvariable=self.estado,
            font=("Arial", 12),
            anchor="w"
        )
        barra_estado.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 10))

    def _registrar_donante(self):
        nombre = self.entry_nombre.get().strip()
        cedula = self.entry_cedula.get().strip()
        tipo_sangre = self.combo_sangre.get()

        if not nombre or not cedula:
            messagebox.showwarning("Error", "Complete todos los campos obligatorios")
            return

        donante = self.pila.registrar_donante(nombre, cedula, tipo_sangre)
        self.estado.set(f"Donante registrado: {nombre} ({tipo_sangre}) a las {donante.hora_registro}")
        self._actualizar_lista()

        # Limpiar campos
        self.entry_nombre.delete(0, "end")
        self.entry_cedula.delete(0, "end")

    def _revertir_ultimo(self):
        donante = self.pila.revertir_ultimo()
        if donante is None:
            messagebox.showinfo("Pila vacía", "No hay donantes para revertir")
            return

        self.estado.set(f"Donante revertido: {donante.nombre} (C.I. {donante.cedula})")
        messagebox.showinfo(
            "Registro revertido",
            f"Se eliminó el último registro por problema técnico:\n\n"
            f"Nombre: {donante.nombre}\n"
            f"Cédula: {donante.cedula}\n"
            f"Tipo sangre: {donante.tipo_sangre}\n"
            f"Hora registro: {donante.hora_registro}"
        )
        self._actualizar_lista()

    def _ver_actual(self):
        donante = self.pila.ver_actual()
        if donante is None:
            messagebox.showinfo("Pila vacía", "No hay donantes en proceso")
            return

        messagebox.showinfo(
            "Donante actual",
            f"Donante en proceso:\n\n"
            f"Nombre: {donante.nombre}\n"
            f"Cédula: {donante.cedula}\n"
            f"Tipo sangre: {donante.tipo_sangre}\n"
            f"Hora registro: {donante.hora_registro}\n\n"
            f"(Último donante registrado)"
        )

    def _actualizar_lista(self):
        donantes = self.pila.mostrar_donantes()
        self.texto_donantes.configure(state="normal")
        self.texto_donantes.delete("1.0", "end")

        if not donantes:
            self.texto_donantes.insert("end", "No hay donantes registrados")
        else:
            for i, donante in enumerate(donantes, 1):
                self.texto_donantes.insert("end", f"{i}. {donante}\n")

        self.texto_donantes.configure(state="disabled")