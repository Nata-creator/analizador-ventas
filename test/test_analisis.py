import pandas as pd
import pytest

from src.analisis import (
    calcular_ventas_totales,
    producto_mas_vendido,
    cantidad_total_productos,
    validar_datos,
    ventas_por_categoria
)


def crear_datos_prueba():
    return pd.DataFrame(
        {
            "fecha": ["2026-08-01", "2026-09-23", "2026-07-07"],
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

def test_validar_datos_correctos():
    ventas = crear_datos_prueba()

    validar_datos(ventas)


def test_validar_datos_rechaza_cantidad_negativa():
    ventas = crear_datos_prueba()
    ventas.loc[0, "cantidad"] = -1

    with pytest.raises(ValueError):
        validar_datos(ventas)
    

def test_ventas_por_categoria():
    ventas = crear_datos_prueba()

    calcular_ventas_totales(ventas)

    categorias = ventas_por_categoria(ventas)

    total_categoria = categorias['Electronica']
    # print(total_categoria)

    # for categoria, valor in categorias.items():
    #     if categoria.lower() == "electronica":
    #         total = total + valor
    assert total_categoria == 3500


def test_validar_datos_rechaza_precio_negativo():
    ventas = crear_datos_prueba()
    ventas.loc[0, "precio_unitario"] = -1000

    with pytest.raises(ValueError):
        validar_datos(ventas)
    #Es un poco mas extenso la forma de abajo, pero funciona,
    #El pyteste nos da una funciona mas simple, arriba
    # try:
    #     validar_datos(ventas)
    # except ValueError:
    #     assert True
    # else:
    #     assert False


def test_validar_datos_rechaza_cantidad_vacia():
    ventas = crear_datos_prueba()
    ventas.loc[0, "cantidad"] = None

    with pytest.raises(ValueError):
            validar_datos(ventas)

def test_prueba():
    ventas = crear_datos_prueba()

    print(ventas.columns)

    calcular_ventas_totales(ventas)

    print(ventas.columns)