"""
archivo: principal.py
Este módulo contiene la implementación de la interfaz gráfica principal del sistema.
autores: Andrea Bojorge, Gabriel Gómez, Gabriel Lacayo
fecha: 10/05/2025
"""
import customtkinter as ctk
from ejercisio1 import DocumentReviewFrame
from ejercisio2 import PanaderiaApp
from ejercisio3 import DonacionSangreFrame
from ejercisio4 import RevisionTareasFrame
from ejercisio5 import MercadoFrame


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema Integrado Nicaragüense")
        self.geometry("1400x850")
        ctk.set_appearance_mode("light")

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create tab view
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Add tabs
        self.tabview.add("Gestión Documental")
        self.tabview.add("Panadería Tradicional")
        self.tabview.add("Donación de Sangre")
        self.tabview.add("Revisión de Tareas")
        self.tabview.add("Mercado Chinandega")
        self.tabview.add("Acerca de")

        # Add frames to tabs
        self._add_document_frame()
        self._add_bakery_frame()
        self._add_blood_frame()
        self._add_homework_frame()
        self._add_market_frame()
        self._add_about_frame()

    def _add_document_frame(self):
        self.doc_frame = DocumentReviewFrame(self.tabview.tab("Gestión Documental"))
        self.doc_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def _add_bakery_frame(self):
        self.bakery_frame = PanaderiaFrame(self.tabview.tab("Panadería Tradicional"))
        self.bakery_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def _add_blood_frame(self):
        self.blood_frame = DonacionSangreFrame(self.tabview.tab("Donación de Sangre"))
        self.blood_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def _add_homework_frame(self):
        self.homework_frame = RevisionTareasFrame(self.tabview.tab("Revisión de Tareas"))
        self.homework_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def _add_market_frame(self):
        self.market_frame = MercadoFrame(self.tabview.tab("Mercado Chinandega"))
        self.market_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def _add_about_frame(self):
        about_frame = ctk.CTkFrame(self.tabview.tab("Acerca de"), fg_color="transparent")
        about_frame.pack(fill="both", expand=True)

        info_text = """
        Sistema Integrado Nicaragüense

        Módulos incluidos:
        1. Gestión Documental - Oficina de atención
        2. Panadería Tradicional - Control de ventas
        3. Donación de Sangre - Campaña hospitalaria
        4. Revisión de Tareas - Control docente
        5. Mercado Chinandega - Carga/descarga

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


class PanaderiaFrame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.app = PanaderiaApp(master=self)
        self.app.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()