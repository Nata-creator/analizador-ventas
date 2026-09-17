import pandas as pd
from analisis import (
    calcular_ventas_totales, 
    cantidad_total_productos, 
    producto_mas_vendido, 
    ventas_por_categoria
    )

from graficos import generar_grafico_categorias, generar_grafico_productos_mas_vendidos

def main():

    ventas = pd.read_csv("data/ventas.csv")

    calcular_ventas_totales(ventas)

    total_ventas = ventas["total"].sum()
    producto = producto_mas_vendido(ventas)
    cantidad = cantidad_total_productos(ventas)
    categorias = ventas_por_categoria(ventas)

    print("=== ANALIZADOR DE VENTAS ===")
    print()
    print(f"Ventas totales: ${total_ventas:,.0f}")
    print(f"Producto más vendido: {producto}")
    print(f"Cantidad total de productos: {cantidad}")
    print()
    print("Ventas por categoría:")
    print(categorias)

    generar_grafico_categorias(ventas)
    generar_grafico_productos_mas_vendidos(ventas=ventas)



if __name__ == "__main__":
    main()
