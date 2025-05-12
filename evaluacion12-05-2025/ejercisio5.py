import customtkinter as ctk
from tkinter import messagebox
from models.pila_sacos import PilaSacos


class MercadoFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Common market products in Chinandega
        self.productos = [
            "Maíz", "Frijol", "Arroz",
            "Sorgo", "Maní", "Ajonjolí",
            "Café", "Azúcar", "Sal"
        ]

        self.pila = PilaSacos()
        self._crear_interfaz()

    def _crear_interfaz(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Title
        titulo = ctk.CTkLabel(
            self,
            text="Carga/Descarga de Sacos - Mercado de Chinandega",
            font=("Arial", 18, "bold"),
            text_color="#8B4513"  # Earth tone
        )
        titulo.grid(row=0, column=0, pady=15, sticky="n")

        # Main frame
        marco_principal = ctk.CTkFrame(self)
        marco_principal.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        marco_principal.grid_columnconfigure(0, weight=1)

        # Loading form
        marco_formulario = ctk.CTkFrame(marco_principal)
        marco_formulario.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # Product
        ctk.CTkLabel(marco_formulario, text="Producto:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.combo_producto = ctk.CTkComboBox(
            marco_formulario,
            values=self.productos,
            state="readonly"
        )
        self.combo_producto.grid(row=0, column=1, padx=5, pady=5)
        self.combo_producto.set(self.productos[0])

        # Weight
        ctk.CTkLabel(marco_formulario, text="Peso (kg):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_peso = ctk.CTkEntry(marco_formulario, width=100)
        self.entry_peso.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Load button
        btn_cargar = ctk.CTkButton(
            marco_formulario,
            text="Cargar Saco",
            command=self._cargar_saco,
            fg_color="#D2691E",
            hover_color="#CD853F"
        )
        btn_cargar.grid(row=2, column=0, columnspan=2, pady=10)

        # Actions frame
        marco_acciones = ctk.CTkFrame(marco_principal)
        marco_acciones.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        # Unload button
        btn_descargar = ctk.CTkButton(
            marco_acciones,
            text="Descargar Último Saco",
            command=self._descargar_saco,
            fg_color="#A0522D",
            hover_color="#8B4513"
        )
        btn_descargar.pack(side="left", padx=5)

        # View top button
        btn_ver = ctk.CTkButton(
            marco_acciones,
            text="Ver Saco Superior",
            command=self._ver_tope,
            fg_color="#D2B48C"
        )
        btn_ver.pack(side="left", padx=5)

        # Sacks list
        marco_lista = ctk.CTkFrame(marco_principal)
        marco_lista.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        marco_lista.grid_columnconfigure(0, weight=1)
        marco_lista.grid_rowconfigure(0, weight=1)

        ctk.CTkLabel(
            marco_lista,
            text="Sacos en el camión (último cargado primero):",
            font=("Arial", 12)
        ).grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.texto_sacos = ctk.CTkTextbox(
            marco_lista,
            wrap="word",
            state="disabled",
            font=("Arial", 12)
        )
        self.texto_sacos.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        # Status bar
        self.estado = ctk.StringVar(value="Camión listo para carga/descarga")
        barra_estado = ctk.CTkLabel(
            self,
            textvariable=self.estado,
            font=("Arial", 12),
            anchor="w"
        )
        barra_estado.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 10))

    def _cargar_saco(self):
        producto = self.combo_producto.get()
        peso = self.entry_peso.get().strip()

        if not peso or not peso.isdigit():
            messagebox.showwarning("Error", "Ingrese un peso válido")
            return

        saco = self.pila.apilar_saco(producto, peso)
        self.estado.set(f"Saco cargado: {producto} ({peso} kg) a las {saco.hora_carga}")
        self._actualizar_lista()

        # Clear weight field
        self.entry_peso.delete(0, "end")

    def _descargar_saco(self):
        saco = self.pila.desapilar_saco()
        if saco is None:
            messagebox.showinfo("Camión vacío", "No hay sacos para descargar")
            return

        self.estado.set(f"Saco descargado: {saco.producto} ({saco.peso} kg)")
        messagebox.showinfo(
            "Saco Descargado",
            f"Se descargó el último saco cargado:\n\n"
            f"Producto: {saco.producto}\n"
            f"Peso: {saco.peso} kg\n"
            f"Hora carga: {saco.hora_carga}"
        )
        self._actualizar_lista()

    def _ver_tope(self):
        saco = self.pila.ver_tope()
        if saco is None:
            messagebox.showinfo("Camión vacío", "No hay sacos en el camión")
            return

        messagebox.showinfo(
            "Saco Superior",
            f"Próximo saco a descargar:\n\n"
            f"Producto: {saco.producto}\n"
            f"Peso: {saco.peso} kg\n"
            f"Hora carga: {saco.hora_carga}\n\n"
            f"(Último saco cargado)"
        )

    def _actualizar_lista(self):
        sacos = self.pila.mostrar_sacos()
        self.texto_sacos.configure(state="normal")
        self.texto_sacos.delete("1.0", "end")

        if not sacos:
            self.texto_sacos.insert("end", "El camión está vacío")
        else:
            for i, saco in enumerate(sacos, 1):
                self.texto_sacos.insert("end", f"{i}. {saco}\n")

        self.texto_sacos.configure(state="disabled")