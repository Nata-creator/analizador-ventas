import pandas as pd
from pathlib import Path
from analisis import ( 
    cantidad_total_productos, 
    producto_mas_vendido, 
    ventas_por_categoria,
    calcular_ventas_totales
    )

REPORTS_DIR = Path("reports")
FILE = 'resumen.txt'
REPORTS_DIR.mkdir(exist_ok=True)

def generar_reporte(ventas: pd.DataFrame) -> None:
    total_ventas = calcular_ventas_totales(ventas)
    producto = producto_mas_vendido(ventas)
    cantidad = cantidad_total_productos(ventas)
    categorias = ventas_por_categoria(ventas)
   
    with open(REPORTS_DIR / FILE, 'w') as fp:
        fp.write("================================\n")
        fp.write("       REPORTE DE VENTAS       \n")
        fp.write("================================\n")
        fp.write(f"Ventas totales: ${total_ventas:,}\n")
        fp.write(f"Producto más vendido: {producto}\n")
        fp.write(f"Cantidad total de productos: {cantidad}\n")
        fp.write("Ventas por categoría:\n")

        for categoria, valor in categorias.items():
            fp.write(f"{categoria}: ${valor:,}\n")

