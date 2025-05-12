"""
archivo: ejercisio1.py
descripcion: Este archivo contiene la implementación de una interfaz gráfica para la gestión de documentos municipales.
Segun el ejercicio 1 de la guia. 
"""

import customtkinter as ctk
from tkinter import messagebox, ttk
from datetime import datetime
from models.pilas_documento import Documento, PilaDocumentos


class DocumentReviewFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Initialize document stack
        self.pila_documentos = PilaDocumentos()

        # Document types for combobox
        self.tipos_documento = [
            "Solicitud",
            "Reclamo",
            "Denuncia",
            "Certificación",
            "Permiso",
            "Otro"
        ]

        # Create UI
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Title
        self.title_label = ctk.CTkLabel(
            self,
            text="Gestión de Documentos Municipales",
            font=("Arial", 16, "bold")
        )
        self.title_label.grid(row=0, column=0, pady=(10, 20), padx=20, sticky="n")

        # Main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Document form
        self.form_frame = ctk.CTkFrame(self.main_frame)
        self.form_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Document name
        ctk.CTkLabel(self.form_frame, text="Nombre del Documento:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.nombre_entry = ctk.CTkEntry(self.form_frame, width=300)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Document type
        ctk.CTkLabel(self.form_frame, text="Tipo de Documento:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.tipo_combobox = ctk.CTkComboBox(self.form_frame, values=self.tipos_documento)
        self.tipo_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Applicant
        ctk.CTkLabel(self.form_frame, text="Solicitante:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.solicitante_entry = ctk.CTkEntry(self.form_frame)
        self.solicitante_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Buttons frame
        self.buttons_frame = ctk.CTkFrame(self.main_frame)
        self.buttons_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Add document button
        self.agregar_btn = ctk.CTkButton(
            self.buttons_frame,
            text="Agregar Documento",
            command=self.agregar_documento
        )
        self.agregar_btn.pack(side="left", padx=5, pady=5)

        # Review document button
        self.revisar_btn = ctk.CTkButton(
            self.buttons_frame,
            text="Revisar Último",
            command=self.revisar_documento
        )
        self.revisar_btn.pack(side="left", padx=5, pady=5)

        # View next button
        self.siguiente_btn = ctk.CTkButton(
            self.buttons_frame,
            text="Ver Siguiente",
            command=self.ver_siguiente
        )
        self.siguiente_btn.pack(side="left", padx=5, pady=5)

        # Pending documents treeview
        self.tree_frame = ctk.CTkFrame(self.main_frame)
        self.tree_frame.grid(row=2, column=0, padx=10, pady=(10, 20), sticky="nsew")
        self.tree_frame.grid_columnconfigure(0, weight=1)
        self.tree_frame.grid_rowconfigure(0, weight=1)

        # Configure treeview style
        style = ttk.Style()
        style.configure("Treeview",
                        font=('Arial', 10),
                        rowheight=25)
        style.configure("Treeview.Heading",
                        font=('Arial', 10, 'bold'))

        # Create treeview with scrollbar
        self.tree_scroll = ctk.CTkScrollbar(self.tree_frame)
        self.tree_scroll.pack(side="right", fill="y")

        self.documentos_tree = ttk.Treeview(
            self.tree_frame,
            columns=("Nombre", "Tipo", "Solicitante", "Fecha"),
            show="headings",
            yscrollcommand=self.tree_scroll.set,
            selectmode="browse"
        )
        self.documentos_tree.pack(expand=True, fill="both")
        self.tree_scroll.configure(command=self.documentos_tree.yview)

        # Configure columns
        self.documentos_tree.heading("Nombre", text="Nombre")
        self.documentos_tree.heading("Tipo", text="Tipo")
        self.documentos_tree.heading("Solicitante", text="Solicitante")
        self.documentos_tree.heading("Fecha", text="Fecha")

        self.documentos_tree.column("Nombre", width=150)
        self.documentos_tree.column("Tipo", width=100)
        self.documentos_tree.column("Solicitante", width=150)
        self.documentos_tree.column("Fecha", width=100)

        # Status bar
        self.status_var = ctk.StringVar(value="Sistema listo")
        self.status_bar = ctk.CTkLabel(
            self,
            textvariable=self.status_var,
            font=("Arial", 12),
            anchor="w"
        )
        self.status_bar.grid(row=2, column=0, padx=20, pady=(0, 10), sticky="ew")

    def agregar_documento(self):
        nombre = self.nombre_entry.get().strip()
        tipo = self.tipo_combobox.get()
        solicitante = self.solicitante_entry.get().strip()

        if not nombre or not solicitante:
            messagebox.showwarning("Datos incompletos", "Por favor complete todos los campos")
            return

        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
        documento = Documento(nombre, tipo, fecha, solicitante)
        self.pila_documentos.agregar_documento(documento)

        # Clear form
        self.nombre_entry.delete(0, "end")
        self.solicitante_entry.delete(0, "end")

        self.actualizar_treeview()
        self.status_var.set(f"Documento agregado: {nombre}")

    def revisar_documento(self):
        if not self.pila_documentos.documentos_pendientes():
            messagebox.showinfo("Pila vacía", "No hay documentos pendientes de revisión")
            return

        documento = self.pila_documentos.revisar_ultimo_documento()
        self.actualizar_treeview()
        self.status_var.set(f"Documento revisado: {documento.nombre}")
        messagebox.showinfo("Documento Revisado",
                            f"Se revisó el documento:\n\n"
                            f"Nombre: {documento.nombre}\n"
                            f"Tipo: {documento.tipo}\n"
                            f"Solicitante: {documento.solicitante}\n"
                            f"Fecha: {documento.fecha}")

    def ver_siguiente(self):
        documento = self.pila_documentos.ver_ultimo_pendiente()
        if documento is None:
            messagebox.showinfo("Pila vacía", "No hay documentos pendientes de revisión")
        else:
            messagebox.showinfo("Próximo Documento",
                                f"Próximo documento a revisar:\n\n"
                                f"Nombre: {documento.nombre}\n"
                                f"Tipo: {documento.tipo}\n"
                                f"Solicitante: {documento.solicitante}\n"
                                f"Fecha: {documento.fecha}")

    def actualizar_treeview(self):
        # Clear current items
        for item in self.documentos_tree.get_children():
            self.documentos_tree.delete(item)

        # Add current documents
        documentos = self.pila_documentos.mostrar_pendientes()
        for doc in reversed(documentos):  # Show most recent at top
            self.documentos_tree.insert("", "end",
                                        values=(doc.nombre, doc.tipo, doc.solicitante, doc.fecha))

    def get_documentos_pendientes(self):
        """Returns list of pending documents for parent application"""
        return self.pila_documentos.mostrar_pendientes()