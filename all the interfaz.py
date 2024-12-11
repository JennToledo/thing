import tkinter as tk
from tkinter import ttk

# Definimos la clase CuentaArticulo
class CuentaArticulo:
    # Atributos
    __TotalDeCompra = 0.0
    __descuento1 = 0.10
    __descuento2 = 0.20
    __TotalApagar = 0.0

    def CalcularTotalAPagar(self, TotalDeCompra, descuento1, descuento2):
        self.__TotalDeCompra = TotalDeCompra
        self.__descuento1 = descuento1
        self.__descuento2 = descuento2

        if 100 <= self.__TotalDeCompra < 200:
            self.__TotalApagar = self.__TotalDeCompra * (1 - self.__descuento1)
        elif self.__TotalDeCompra >= 200:
            self.__TotalApagar = self.__TotalDeCompra * (1 - self.__descuento2)
        else:
            self.__TotalApagar = self.__TotalDeCompra
        return self.__TotalApagar


# Función para calcular el descuento
def calcularTotal():
    total_compra = 0.0
    try:
        total_compra = float(input_total_compra.get())
        etiqueta_error_total.config(text=f"")
    except ValueError as ve:
        etiqueta_error_total.config(text=f"Introduce un número válido")

    cuenta = CuentaArticulo()
    monto_final = cuenta.CalcularTotalAPagar(total_compra, cuenta._CuentaArticulo__descuento1, cuenta._CuentaArticulo__descuento2)

    etiqueta_total_pagar.config(text=f"El total a pagar es: ${monto_final:.2f}")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Total con Descuento")
ventana.config(width=400, height=200)

# Etiquetas
etiqueta_total_compra = ttk.Label(text="Introduce el total de la compra:")
etiqueta_total_compra.place(x=10, y=10)

# Etiqueta de error
etiqueta_error_total = ttk.Label(text="")
etiqueta_error_total.place(x=300, y=10)

# Campo de entrada para el total de la compra
input_total_compra = ttk.Entry()
input_total_compra.place(x=200, y=10, width=80)

# Botón para calcular el total a pagar
boton_calcular = ttk.Button(text="Calcular", command=calcularTotal)
boton_calcular.place(x=100, y=40)

# Etiqueta para mostrar el total a pagar
etiqueta_total_pagar = ttk.Label(text="El total a pagar es:")
etiqueta_total_pagar.place(x=10, y=100)

# Ejecutar la aplicación
ventana.mainloop()
