"""
archivo: ejercicio2.py
Este módulo contiene la interfaz gráfica para la simulación de una cola de atención en una clínica.
autores: Andrea Bojorge, Gabriel Gómez, Gabriel Lacayo
fecha: 10/05/2025
"""

import customtkinter as ctk

class ClinicaAtencionFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(4, weight=1)

        # Título
        self.label_title = ctk.CTkLabel(self, text="Atención Clínica - Cola de Pacientes", font=("Arial", 22, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, pady=10)

        # Entrada para nombre del paciente
        self.entry_patient_name = ctk.CTkEntry(self, placeholder_text="Nombre del paciente")
        self.entry_patient_name.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Botón para agregar paciente
        self.btn_add_patient = ctk.CTkButton(self, text="Registrar llegada")
        self.btn_add_patient.grid(row=1, column=1, padx=10, pady=5)

        # Botón para atender paciente
        self.btn_attend = ctk.CTkButton(self, text="Atender siguiente paciente")
        self.btn_attend.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Etiqueta de la cola actual
        self.label_queue = ctk.CTkLabel(self, text="Pacientes en espera:", font=("Arial", 16))
        self.label_queue.grid(row=3, column=0, columnspan=2, padx=10, pady=(5, 0), sticky="w")

        # Caja de texto para mostrar la cola
        self.queue_box = ctk.CTkTextbox(self, height=200)
        self.queue_box.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        # Pacientes precargados para la demostración
        self._cargar_pacientes_ejemplo()

    def _cargar_pacientes_ejemplo(self):
        texto = (
            "1. Elma Scapo Ronga\n"
            "2. Augusto Cesar Sandino\n"
            "3. ALGP Gutierrez\n"
        )
        self.queue_box.insert("0.0", texto)


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Simulación - Clínica de Atención")
    app.geometry("800x600")
    ctk.set_appearance_mode("light")

    frame = ClinicaAtencionFrame(master=app)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    app.mainloop()
