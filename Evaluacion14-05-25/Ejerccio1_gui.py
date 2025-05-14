"""
archivo: ejercicio1.py
Este módulo contiene la interfaz gráfica para la simulación de una cola de impresión compartida.
autores: Andrea Bojorge, Gabriel Gómez, Gabriel Lacayo
fecha: 10/05/2025
"""
from ejercicio_2.cola import *
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

class Ej1Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.lista = ColaImpresion()
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

        self.frame_botones = ctk.CTkFrame(self)
        self.frame_botones.grid(row=2, column=1, columnspan=2, padx=10, pady=(5, 0), sticky="ew")

        # Botón para agregar documento
        self.btn_add = ctk.CTkButton(self.frame_botones, text="Agregar a la cola", command=self.agregar_documento)
        self.btn_add.grid(row=0, column=0, padx=10, pady=5)

        self.btn_view = ctk.CTkButton(self.frame_botones, text="Ver Cola", command=self.mostrar_documento_actual)
        self.btn_view.grid(row=0, column=1, padx=10, pady=5)

        self.btn_print = ctk.CTkButton(self.frame_botones, text="Imprimir", command=self.imprimir_documento)
        self.btn_print.grid(row=0, column=2, padx=10, pady=5)

        # Etiqueta para la cola
        self.queue_label = ctk.CTkLabel(self, text="Documentos en cola:", font=("Arial", 16))
        self.queue_label.grid(row=3, column=0, columnspan=2, padx=10, pady=(15, 5), sticky="w")

        # Caja de texto para mostrar documentos en cola
        self.queue_box = ctk.CTkTextbox(self, height=200)
        self.queue_box.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        # # Simulación de datos precargados
        # self._cargar_datos_ejemplo()

    def agregar_documento(self):
        nombre = self.entry_doc_name.get()
        usuario = self.entry_user_name.get()
        paginas = self.entry_pages.get()
        doc = Documento(nombre, usuario, int(paginas))
        self.lista.agregar_documento(doc)
        self.queue_box.insert("end", f"{doc}\n")


    def imprimir_documento(self):
        self.lista.procesar_siguiente()
        CTkMessagebox(title="Impresión", message="El documento ha sido enviado a la impresora.")
        self.eliminar_primera_linea()

    def eliminar_primera_linea(self):
        """
        Elimina la primera línea de la caja de texto queue_box.
        """
        first_line_index = self.queue_box.index("1.0").split(".")[0]
        if int(self.queue_box.index("end-1c").split(".")[0]) > 1:  # Verifica que haya más de una línea
            self.queue_box.delete(f"{first_line_index}.0", f"{first_line_index}.end+1c")

    def mostrar_documento_actual(self):
        documento = self.lista.documento_actual()
        nombre = documento.nombre if documento else "No hay documentos"
        usuario = documento.usuario if documento else "N/A"
        paginas = documento.num_paginas if documento else "N/A"
        CTkMessagebox(title="Documento Actual", message=f"{documento}")


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Simulación - Cola de Impresión")
    app.geometry("800x600")
    ctk.set_appearance_mode("light")

    frame = Ej1Frame(master=app)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    app.mainloop()
