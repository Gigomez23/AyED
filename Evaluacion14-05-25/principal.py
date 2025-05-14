"""
archivo: principal.py
Este módulo contiene la implementación de la interfaz gráfica principal del sistema.
autores: Andrea Bojorge, Gabriel Gómez, Gabriel Lacayo
fecha: 14/05/2025
para poder ejecutar el programa asegurese de instalar la libreria customtkinter
ejecutando el siguiente comando:
pip install customtkinter
pip install CtkMessagebox
"""
import customtkinter as ctk
from Ejercicio_clinica import ClinicaAtencionFrame
from Ejerccio1_gui import Ej1Frame


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Ejemplificacion de Colas en diversos módulos")
        self.geometry("1200x850")
        ctk.set_appearance_mode("light")

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create tab view
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Add tabs
        self.tabview.add("Gestión Clinica")
        self.tabview.add("Control de Impresora")
        self.tabview.add("Acerca de")


        # Add frames to tabs
        self._add_clinic_frame()
        self._add_bakery_frame()
        self._add_about_frame()


    def _add_clinic_frame(self):
        self.doc_frame = ClinicaAtencionFrame(self.tabview.tab("Gestión Clinica"))
        self.doc_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def _add_bakery_frame(self):
        self.bakery_frame = Ej1Frame(self.tabview.tab("Control de Impresora"))
        self.bakery_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def _add_about_frame(self):
        about_frame = ctk.CTkFrame(self.tabview.tab("Acerca de"), fg_color="transparent")
        about_frame.pack(fill="both", expand=True)

        info_text = """
        Ejemplo de Colas
        Este sistema es una demostración de la implementación de colas en diferentes contextos.

        Módulos incluidos:
        1. Gestión Clinica - Clinica de atención
        2. Control de Impresora - ejemplificación de cola de impresión compartida
        

        Desarrollado por:
        Andrea Bojorge
        Gabriel Gómez
        Gabriel Lacayo
        """

        ctk.CTkLabel(
            about_frame,
            text=info_text,
            font=("Arial", 14),
            justify="left"
        ).pack(pady=50, padx=50, anchor="w")



if __name__ == "__main__":
    app = MainApp()
    app.mainloop()