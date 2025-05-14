"""
archivo: ejercicio1.py
Este módulo contiene la interfaz gráfica para la simulación de una cola de impresión compartida.
autores: Andrea Bojorge, Gabriel Gómez, Gabriel Lacayo
fecha: 10/05/2025
"""

import customtkinter as ctk

class Ej1Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Configuración general del grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(4, weight=1)

        # Título
        self.label_title = ctk.CTkLabel(self, text="Cola de Impresión Compartida", font=("Arial", 22, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, pady=10)

        # Campos de entrada
        self.entry_doc_name = ctk.CTkEntry(self, placeholder_text="Nombre del documento")
        self.entry_doc_name.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.entry_user_name = ctk.CTkEntry(self, placeholder_text="Nombre del usuario")
        self.entry_user_name.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.entry_pages = ctk.CTkEntry(self, placeholder_text="Número de páginas")
        self.entry_pages.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        # Botón para agregar documento
        self.btn_add = ctk.CTkButton(self, text="Agregar a la cola")
        self.btn_add.grid(row=2, column=1, padx=10, pady=5)

        # Etiqueta para la cola
        self.queue_label = ctk.CTkLabel(self, text="Documentos en cola:", font=("Arial", 16))
        self.queue_label.grid(row=3, column=0, columnspan=2, padx=10, pady=(15, 5), sticky="w")

        # Caja de texto para mostrar documentos en cola
        self.queue_box = ctk.CTkTextbox(self, height=200)
        self.queue_box.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        # Etiqueta del documento actual
        self.label_current = ctk.CTkLabel(self, text="Documento en impresión:", font=("Arial", 16))
        self.label_current.grid(row=5, column=0, columnspan=2, padx=10, pady=(15, 5), sticky="w")

        self.label_current_doc = ctk.CTkLabel(self, text="Memoria_Técnica.pdf (por Laura, 12 páginas)", font=("Arial", 14), text_color="green")
        self.label_current_doc.grid(row=6, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="w")

        # Simulación de datos precargados
        self._cargar_datos_ejemplo()

    def _cargar_datos_ejemplo(self):
        ejemplo_texto = (
            "1. Informe_Final.docx - Usuario: Tupu - Páginas: 8\n"
            "2. Proyecto_Sistemas.pdf - Usuario: Elver - Páginas: 15\n"
            "3. Tesis_UAM.docx - Usuario: Concha - Páginas: 25\n"
        )
        self.queue_box.insert("0.0", ejemplo_texto)


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Simulación - Cola de Impresión")
    app.geometry("800x600")
    ctk.set_appearance_mode("light")

    frame = Ej1Frame(master=app)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    app.mainloop()
