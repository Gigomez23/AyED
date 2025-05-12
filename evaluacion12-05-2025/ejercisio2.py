import customtkinter as ctk
from tkinter import messagebox
from models.pilas_pan import PilaPanes
from datetime import datetime


class PanaderiaApp(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Tipos de pan tradicionales de León
        self.tipos_pan = [
            "Pan de León",
            "Bollo preñao",
            "Pan de trigo",
            "Pan de centeno",
            "Pan de maíz",
            "Hojaldre",
            "Pan de pueblo"
        ]

        self.pila = PilaPanes()
        self._crear_interfaz()

    def _crear_interfaz(self):
        # Configurar grid principal
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Título
        titulo = ctk.CTkLabel(
            self,
            text="Panadería Tradicional de León",
            font=("Arial", 20, "bold"),
            text_color="#8B4513"  # Color marrón panadero
        )
        titulo.grid(row=0, column=0, pady=20, padx=20, sticky="n")

        # Marco principal
        marco_principal = ctk.CTkFrame(self)
        marco_principal.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
        marco_principal.grid_columnconfigure(0, weight=1)

        # Sección de agregar pan
        marco_agregar = ctk.CTkFrame(marco_principal)
        marco_agregar.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ctk.CTkLabel(marco_agregar, text="Tipo de pan:").grid(row=0, column=0, padx=5, pady=5)
        self.combo_tipo = ctk.CTkComboBox(
            marco_agregar,
            values=self.tipos_pan,
            state="readonly"
        )
        self.combo_tipo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.combo_tipo.set(self.tipos_pan[0])

        btn_agregar = ctk.CTkButton(
            marco_agregar,
            text="Agregar a la bandeja",
            command=self._agregar_pan,
            fg_color="#D2B48C"  # Color tierra
        )
        btn_agregar.grid(row=0, column=2, padx=5, pady=5)

        # Sección de acciones
        marco_acciones = ctk.CTkFrame(marco_principal)
        marco_acciones.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        btn_vender = ctk.CTkButton(
            marco_acciones,
            text="Vender último pan",
            command=self._vender_pan,
            fg_color="#A0522D"  # Color sienna
        )
        btn_vender.pack(side="left", padx=5, pady=5)

        btn_ver = ctk.CTkButton(
            marco_acciones,
            text="Ver próximo pan",
            command=self._ver_proximo,
            fg_color="#CD853F"  # Color peru
        )
        btn_ver.pack(side="left", padx=5, pady=5)

        # Lista de panes
        marco_lista = ctk.CTkFrame(marco_principal)
        marco_lista.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        marco_lista.grid_columnconfigure(0, weight=1)
        marco_lista.grid_rowconfigure(0, weight=1)

        self.titulo_lista = ctk.CTkLabel(
            marco_lista,
            text="Panes en bandeja (el último agregado aparece primero):",
            font=("Arial", 12)
        )
        self.titulo_lista.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.lista_panes = ctk.CTkTextbox(
            marco_lista,
            wrap="none",
            state="disabled",
            font=("Arial", 12)
        )
        self.lista_panes.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        # Barra de estado
        self.estado = ctk.StringVar(value="Listo para trabajar")
        barra_estado = ctk.CTkLabel(
            self,
            textvariable=self.estado,
            font=("Arial", 12),
            anchor="w"
        )
        barra_estado.grid(row=2, column=0, padx=20, pady=(0, 10), sticky="ew")

    def _agregar_pan(self):
        tipo_pan = self.combo_tipo.get()
        if not tipo_pan:
            messagebox.showwarning("Error", "Seleccione un tipo de pan")
            return

        pan = self.pila.agregar_pan(tipo_pan)
        self.estado.set(f"Pan agregado: {tipo_pan} a las {pan.hora_horneado}")
        self._actualizar_lista()

    def _vender_pan(self):
        pan = self.pila.vender_pan()
        if pan is None:
            messagebox.showinfo("Bandeja vacía", "No hay panes para vender")
            return

        self.estado.set(f"Pan vendido: {pan.tipo} (horneado a las {pan.hora_horneado})")
        messagebox.showinfo(
            "Pan vendido",
            f"Se vendió el último pan agregado:\n\n"
            f"Tipo: {pan.tipo}\n"
            f"Horneado a las: {pan.hora_horneado}"
        )
        self._actualizar_lista()

    def _ver_proximo(self):
        pan = self.pila.ver_proximo()
        if pan is None:
            messagebox.showinfo("Bandeja vacía", "No hay panes en la bandeja")
            return

        messagebox.showinfo(
            "Próximo pan a vender",
            f"Próximo pan en la bandeja:\n\n"
            f"Tipo: {pan.tipo}\n"
            f"Horneado a las: {pan.hora_horneado}\n\n"
            f"(Último pan agregado)"
        )

    def _actualizar_lista(self):
        panes = self.pila.mostrar_panes()
        self.lista_panes.configure(state="normal")
        self.lista_panes.delete("1.0", "end")

        if not panes:
            self.lista_panes.insert("end", "La bandeja está vacía")
        else:
            for i, pan in enumerate(panes, 1):
                self.lista_panes.insert("end", f"{i}. {pan.tipo} - Horneado: {pan.hora_horneado}\n")

        self.lista_panes.configure(state="disabled")


if __name__ == "__main__":
    app = PanaderiaApp()
    app.mainloop()