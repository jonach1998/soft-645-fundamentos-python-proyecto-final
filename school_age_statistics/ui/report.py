import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from school_age_statistics.security.password import es_contrasena_valida, MAX_INTENTOS
from school_age_statistics.calculations.age_statistics import calculate_statistics
from school_age_statistics.data_entry.age_input import request_age_sample

_MIN_AGE = 1
_MAX_AGE = 120


class AgeStatisticsApp:
    """
    Aplicación de escritorio (Tkinter) del Sistema de Estadísticas de Edades.
    Reutiliza la lógica de negocio de security/password.py y
    statistics/calculations.py, que también usa la versión de consola.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Estadísticas de Edades - Colegio San Pascualin")
        self.root.geometry("650x680")
        self.root.resizable(False, False)

        self.intentos_restantes = MAX_INTENTOS
        self.cantidad = 0
        self.edades = []
        self.estadisticas = None

        self._construir_encabezado()
        self._construir_frame_login()
        self._construir_frame_principal()
        self._construir_frame_reporte()

        self.frame_login.pack(pady=20)

    # ----------------------------------------------------------------
    # CONSTRUCCIÓN DE LA INTERFAZ
    # ----------------------------------------------------------------

    def _construir_encabezado(self):
        fecha_actual = datetime.now()

        tk.Label(
            self.root,
            text="SISTEMA DE ESTADÍSTICAS DE EDADES",
            font=("Arial", 18, "bold"),
        ).pack(pady=10)

        tk.Label(self.root, text="Colegio San Pascualin", font=("Arial", 12, "italic")).pack()

        tk.Label(
            self.root,
            text=f"Fecha: {fecha_actual.strftime('%d/%m/%Y')}     "
                 f"Hora: {fecha_actual.strftime('%H:%M:%S')}",
            font=("Arial", 10),
        ).pack(pady=(0, 10))

    def _construir_frame_login(self):
        self.frame_login = tk.Frame(self.root)

        tk.Label(self.frame_login, text="Ingrese la contraseña", font=("Arial", 12)).pack(pady=5)

        self.entry_password = tk.Entry(self.frame_login, show="*", width=30)
        self.entry_password.pack(pady=5)
        self.entry_password.bind("<Return>", lambda event: self._ingresar())

        self.lbl_intentos = tk.Label(
            self.frame_login,
            text=f"Intentos restantes: {self.intentos_restantes}",
            fg="gray",
        )
        self.lbl_intentos.pack(pady=5)

        tk.Button(
            self.frame_login,
            text="Ingresar",
            command=self._ingresar,
            bg="#4CAF50",
            fg="white",
            width=20,
        ).pack(pady=5)

    def _construir_frame_principal(self):
        self.frame_principal = tk.Frame(self.root)

        tk.Label(self.frame_principal, text="Cantidad de alumnos (tamaño de la muestra)").pack()

        self.entry_cantidad = tk.Entry(self.frame_principal)
        self.entry_cantidad.pack()

        tk.Button(
            self.frame_principal,
            text="Crear Lista",
            command=self._crear_lista,
        ).pack(pady=5)

        tk.Label(self.frame_principal, text=f"Edad (entre {_MIN_AGE} y {_MAX_AGE})").pack()

        self.entry_edad = tk.Entry(self.frame_principal)
        self.entry_edad.pack()
        self.entry_edad.bind("<Return>", lambda event: self._agregar())

        tk.Button(
            self.frame_principal,
            text="Agregar Edad",
            command=self._agregar,
        ).pack(pady=5)

        self.lista = tk.Listbox(self.frame_principal, width=25, height=8)
        self.lista.pack(pady=10)

        botones = tk.Frame(self.frame_principal)
        botones.pack(pady=5)

        tk.Button(
            botones,
            text="Calcular y Generar Reporte",
            command=self._calcular_y_generar_reporte,
            bg="#2196F3",
            fg="white",
            width=24,
        ).grid(row=0, column=0, columnspan=2, pady=5)

        tk.Button(
            botones,
            text="Limpiar",
            command=self._limpiar,
            bg="#FF9800",
            fg="white",
            width=11,
        ).grid(row=1, column=0, padx=3)

        tk.Button(
            botones,
            text="Salir",
            command=self.root.destroy,
            bg="#F44336",
            fg="white",
            width=11,
        ).grid(row=1, column=1, padx=3)

    def _construir_frame_reporte(self):
        self.frame_reporte = tk.Frame(self.root)

        tk.Label(
            self.frame_reporte,
            text="REPORTE DE ESTADÍSTICAS",
            font=("Arial", 14, "bold"),
        ).pack(pady=10)

        self.texto_reporte = tk.Text(self.frame_reporte, width=55, height=18, wrap="word")
        self.texto_reporte.pack(pady=5)
        self.texto_reporte.config(state="disabled")

        self.lbl_guardado = tk.Label(self.frame_reporte, text="", fg="green")
        self.lbl_guardado.pack(pady=5)

        tk.Button(
            self.frame_reporte,
            text="Volver",
            command=self._volver_a_principal,
            width=20,
        ).pack(pady=5)

    # ----------------------------------------------------------------
    # LOGIN
    # ----------------------------------------------------------------

    def _ingresar(self):
        intento = self.entry_password.get()

        if es_contrasena_valida(intento):
            messagebox.showinfo("Acceso concedido", "Bienvenido al sistema.")
            self.frame_login.pack_forget()
            self.frame_principal.pack(pady=10)
            return

        self.intentos_restantes -= 1
        self.entry_password.delete(0, tk.END)

        if self.intentos_restantes <= 0:
            messagebox.showerror(
                "Acceso denegado", "Demasiados intentos fallidos. El programa se cerrará."
            )
            self.root.destroy()
            return

        self.lbl_intentos.config(text=f"Intentos restantes: {self.intentos_restantes}")
        messagebox.showerror("Error", "Contraseña incorrecta.")

    # ----------------------------------------------------------------
    # INGRESO DE DATOS
    # ----------------------------------------------------------------

    def _crear_lista(self):
        try:
            cantidad = int(self.entry_cantidad.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número entero válido.")
            return

        if cantidad <= 0:
            messagebox.showwarning("Aviso", "El tamaño de la muestra debe ser mayor que 0.")
            return

        self.cantidad = cantidad
        self.edades.clear()
        self.lista.delete(0, tk.END)

        messagebox.showinfo("Correcto", f"Ahora puede ingresar las {cantidad} edades.")

    def _agregar(self):
        if self.cantidad == 0:
            messagebox.showwarning("Aviso", "Primero indique la cantidad de alumnos.")
            return

        if len(self.edades) >= self.cantidad:
            messagebox.showwarning("Aviso", "Ya ingresó todas las edades de la muestra.")
            return

        try:
            edad = int(self.entry_edad.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese una edad válida (número entero).")
            return

        if edad < _MIN_AGE or edad > _MAX_AGE:
            messagebox.showwarning(
                "Aviso", f"La edad debe estar entre {_MIN_AGE} y {_MAX_AGE}."
            )
            return

        self.edades.append(edad)
        self.lista.insert(tk.END, edad)
        self.entry_edad.delete(0, tk.END)

    # ----------------------------------------------------------------
    # CÁLCULO Y REPORTE
    # ----------------------------------------------------------------

    def _calcular_y_generar_reporte(self):
        if len(self.edades) == 0:
            messagebox.showwarning("Aviso", "No hay edades registradas.")
            return

        if len(self.edades) < self.cantidad:
            messagebox.showwarning(
                "Aviso",
                f"Faltan edades por ingresar ({len(self.edades)}/{self.cantidad}).",
            )
            return

        self.estadisticas = calculate_statistics(self.edades)
        contenido = self._construir_contenido_reporte()

        self.texto_reporte.config(state="normal")
        self.texto_reporte.delete("1.0", tk.END)
        self.texto_reporte.insert(tk.END, contenido)
        self.texto_reporte.config(state="disabled")

        ruta_archivo = self._guardar_reporte(contenido)
        self.lbl_guardado.config(text=f"Reporte guardado automáticamente en: {ruta_archivo}")

        self.frame_principal.pack_forget()
        self.frame_reporte.pack(pady=10)

    def _construir_contenido_reporte(self):
        ahora = datetime.now()
        est = self.estadisticas

        lineas = []
        lineas.append("REPORTE DE ESTADÍSTICAS DE EDADES")
        lineas.append("Colegio San Pascualin")
        lineas.append("=" * 40)
        lineas.append(f"Fecha: {ahora.strftime('%d/%m/%Y')}")
        lineas.append(f"Hora : {ahora.strftime('%H:%M:%S')}")
        lineas.append("")
        lineas.append(f"Tamaño de la muestra: {self.cantidad}")
        lineas.append("Edades ingresadas:")

        for i, edad in enumerate(self.edades, start=1):
            lineas.append(f"  #{i}: {edad}")

        lineas.append("")
        lineas.append(f"Edad mayor  : {est['max_age']}")
        lineas.append(f"Edad menor  : {est['min_age']}")
        lineas.append(f"Promedio    : {est['average']}")
        lineas.append(f"Mediana     : {est['median']}")

        return "\n".join(lineas)

    def _guardar_reporte(self, contenido):
        nombre_archivo = "Reporte_Edades.txt"

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)

        return nombre_archivo

    # ----------------------------------------------------------------
    # NAVEGACIÓN Y LIMPIEZA
    # ----------------------------------------------------------------

    def _volver_a_principal(self):
        self.frame_reporte.pack_forget()
        self.frame_principal.pack(pady=10)

    def _limpiar(self):
        self.cantidad = 0
        self.edades.clear()
        self.estadisticas = None

        self.lista.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)


def iniciar_aplicacion_gui():
    root = tk.Tk()
    AgeStatisticsApp(root)
    root.mainloop()
