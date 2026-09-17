import pandas as pd

from src.analisis import (
    calcular_ventas_totales,
    producto_mas_vendido,
    cantidad_total_productos,
)


def crear_datos_prueba():
    return pd.DataFrame(
        {
            "producto": ["Laptop", "Mouse", "Laptop"],
            "categoria": ["Electronica", "Electronica", "Electronica"],
            "cantidad": [2, 5, 1],
            "precio_unitario": [1000, 100, 1000],
        }
    )


def test_calcular_ventas_totales():
    ventas = crear_datos_prueba()

    resultado = calcular_ventas_totales(ventas)

    assert resultado == 3500


def test_producto_mas_vendido():
    ventas = crear_datos_prueba()

    resultado = producto_mas_vendido(ventas)

    assert resultado == "Mouse"


def test_cantidad_total_productos():
    ventas = crear_datos_prueba()

    resultado = cantidad_total_productos(ventas)

    assert resultado == 8

