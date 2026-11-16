import tkinter as tk
from tkinter import ttk


def saludar():
    nombre = entrada_nombre.get().strip()
    if nombre:
        etiqueta_saludo.config(text=f"¡Hola, {nombre}!")
    else:
        etiqueta_saludo.config(text="¡Hola! Por favor ingresa tu nombre.")


# Ventana principal
ventana = tk.Tk()
ventana.title("Saludo")
ventana.geometry("320x160")
ventana.resizable(False, False)

# Marco principal con padding
marco = ttk.Frame(ventana, padding=15)
marco.pack(fill="both", expand=True)

# Etiqueta de instrucción
etiqueta_pregunta = ttk.Label(marco, text="¿Cómo te llamas?")
etiqueta_pregunta.pack(pady=(0, 5))

# Campo de texto para ingresar el nombre
entrada_nombre = ttk.Entry(marco)
entrada_nombre.pack(fill="x", pady=5)
entrada_nombre.focus()

# Botón para saludar
boton_saludar = ttk.Button(marco, text="Saludar", command=saludar)
boton_saludar.pack(pady=5)

# Etiqueta para mostrar el saludo resultante
etiqueta_saludo = ttk.Label(marco, text="", font=("Segoe UI", 10, "bold"))
etiqueta_saludo.pack(pady=5)

# Permitir presionar Enter para saludar
ventana.bind("<Return>", lambda event: saludar())

# Bucle principal de la interfaz
ventana.mainloop()
