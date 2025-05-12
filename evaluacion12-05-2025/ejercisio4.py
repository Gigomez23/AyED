"""
archivo: ejercisio4.py
descripcion: Este archivo contiene la implementación de una interfaz gráfica para la gestión de un sistema de revision de tarea.
Segun el ejercicio 4 de la guia. 
"""
import customtkinter as ctk
from tkinter import messagebox
from models.pila_tareas import PilaTareas


class RevisionTareasFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Common school subjects
        self.materias = [
            "Programación",
            "Base de Datos",
            "Redes",
            "Ofimática",
            "Sistemas Operativos",
            "Diseño Web"
        ]

        # Grade levels
        self.grados = [str(i) + "°" for i in range(7, 12)]  # 7° to 11°

        self.pila = PilaTareas()
        self._crear_interfaz()

    def _crear_interfaz(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Title
        titulo = ctk.CTkLabel(
            self,
            text="Sistema de Revisión de Tareas",
            font=("Arial", 18, "bold"),
            text_color="#2E8B57"  # School green color
        )
        titulo.grid(row=0, column=0, pady=15, sticky="n")

        # Main frame
        marco_principal = ctk.CTkFrame(self)
        marco_principal.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        marco_principal.grid_columnconfigure(0, weight=1)

        # Registration form
        marco_formulario = ctk.CTkFrame(marco_principal)
        marco_formulario.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # Student name
        ctk.CTkLabel(marco_formulario, text="Estudiante:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_estudiante = ctk.CTkEntry(marco_formulario, width=250)
        self.entry_estudiante.grid(row=0, column=1, padx=5, pady=5)

        # Grade
        ctk.CTkLabel(marco_formulario, text="Grado:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.combo_grado = ctk.CTkComboBox(
            marco_formulario,
            values=self.grados,
            state="readonly"
        )
        self.combo_grado.grid(row=1, column=1, padx=5, pady=5)
        self.combo_grado.set(self.grados[0])  # Default value

        # Subject
        ctk.CTkLabel(marco_formulario, text="Materia:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.combo_materia = ctk.CTkComboBox(
            marco_formulario,
            values=self.materias,
            state="readonly"
        )
        self.combo_materia.grid(row=2, column=1, padx=5, pady=5)
        self.combo_materia.set(self.materias[0])  # Default value

        # Add button
        btn_agregar = ctk.CTkButton(
            marco_formulario,
            text="Recibir Tarea",
            command=self._agregar_tarea,
            fg_color="#2E8B57",
            hover_color="#3CB371"
        )
        btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

        # Actions frame
        marco_acciones = ctk.CTkFrame(marco_principal)
        marco_acciones.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        # Review button
        btn_revisar = ctk.CTkButton(
            marco_acciones,
            text="Revisar Última Tarea",
            command=self._revisar_tarea,
            fg_color="#4169E1",
            hover_color="#6495ED"
        )
        btn_revisar.pack(side="left", padx=5)

        # View next button
        btn_ver = ctk.CTkButton(
            marco_acciones,
            text="Ver Próxima a Revisar",
            command=self._ver_proxima,
            fg_color="#9370DB"
        )
        btn_ver.pack(side="left", padx=5)

        # Assignments list
        marco_lista = ctk.CTkFrame(marco_principal)
        marco_lista.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        marco_lista.grid_columnconfigure(0, weight=1)
        marco_lista.grid_rowconfigure(0, weight=1)

        ctk.CTkLabel(
            marco_lista,
            text="Tareas por revisar (última entregada primero):",
            font=("Arial", 12)
        ).grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.texto_tareas = ctk.CTkTextbox(
            marco_lista,
            wrap="word",
            state="disabled",
            font=("Arial", 12)
        )
        self.texto_tareas.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        # Status bar
        self.estado = ctk.StringVar(value="Sistema listo para recibir tareas")
        barra_estado = ctk.CTkLabel(
            self,
            textvariable=self.estado,
            font=("Arial", 12),
            anchor="w"
        )
        barra_estado.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 10))

    def _agregar_tarea(self):
        estudiante = self.entry_estudiante.get().strip()
        grado = self.combo_grado.get()
        materia = self.combo_materia.get()

        if not estudiante:
            messagebox.showwarning("Error", "Ingrese el nombre del estudiante")
            return

        tarea = self.pila.agregar_tarea(estudiante, grado, materia)
        self.estado.set(f"Tarea recibida: {estudiante} ({grado}) - {materia}")
        self._actualizar_lista()

        # Clear fields
        self.entry_estudiante.delete(0, "end")

    def _revisar_tarea(self):
        tarea = self.pila.revisar_tarea()
        if tarea is None:
            messagebox.showinfo("Pila vacía", "No hay tareas para revisar")
            return

        self.estado.set(f"Tarea revisada: {tarea.estudiante} ({tarea.grado})")
        messagebox.showinfo(
            "Tarea Revisada",
            f"Se revisó la última tarea entregada:\n\n"
            f"Estudiante: {tarea.estudiante}\n"
            f"Grado: {tarea.grado}\n"
            f"Materia: {tarea.materia}\n"
            f"Fecha entrega: {tarea.fecha_entrega}"
        )
        self._actualizar_lista()

    def _ver_proxima(self):
        tarea = self.pila.ver_proxima()
        if tarea is None:
            messagebox.showinfo("Pila vacía", "No hay tareas pendientes")
            return

        messagebox.showinfo(
            "Próxima Tarea",
            f"Próxima tarea a revisar:\n\n"
            f"Estudiante: {tarea.estudiante}\n"
            f"Grado: {tarea.grado}\n"
            f"Materia: {tarea.materia}\n"
            f"Fecha entrega: {tarea.fecha_entrega}\n\n"
            f"(Última tarea entregada)"
        )

    def _actualizar_lista(self):
        tareas = self.pila.mostrar_tareas()
        self.texto_tareas.configure(state="normal")
        self.texto_tareas.delete("1.0", "end")

        if not tareas:
            self.texto_tareas.insert("end", "No hay tareas pendientes de revisión")
        else:
            for i, tarea in enumerate(tareas, 1):
                self.texto_tareas.insert("end", f"{i}. {tarea}\n")

        self.texto_tareas.configure(state="disabled")