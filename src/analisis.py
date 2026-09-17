import pandas as pd


def calcular_ventas_totales(ventas: pd.DataFrame) -> float:
    ventas["total"] = ventas["cantidad"] * ventas["precio_unitario"]
    return ventas["total"].sum()


def producto_mas_vendido(ventas: pd.DataFrame) -> str:
    cantidades = ventas.groupby("producto")["cantidad"].sum()
    return cantidades.idxmax()


def cantidad_total_productos(ventas: pd.DataFrame) -> int:
    return int(ventas["cantidad"].sum())


def ventas_por_categoria(ventas: pd.DataFrame) -> pd.Series:
    return ventas.groupby("categoria")["total"].sum()

def validar_datos(ventas: pd.DataFrame) -> None:
    columnas_requeridas = {
        "fecha",
        "producto",
        "categoria",
        "cantidad",
        "precio_unitario",
    }

    columnas_faltantes = columnas_requeridas - set(ventas.columns)

    if columnas_faltantes:
        raise ValueError(
            f"Faltan columnas requeridas: {columnas_faltantes}"
        )

    if ventas["cantidad"].isnull().any():
        raise ValueError("Existen cantidades vacías.")

    if ventas["precio_unitario"].isnull().any():
        raise ValueError("Existen precios vacíos.")

    if (ventas["cantidad"] <= 0).any():
        raise ValueError("La cantidad debe ser mayor que cero.")

    if (ventas["precio_unitario"] <= 0).any():
        raise ValueError("El precio debe ser mayor que cero.")
