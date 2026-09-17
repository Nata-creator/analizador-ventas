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