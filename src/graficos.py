from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

from analisis import ventas_por_categoria

REPORTS_DIR = Path("reports")

def __ini__():
    REPORTS_DIR.mkdir(exist_ok=True)

def generar_grafico_categorias(ventas: pd.DataFrame) -> None:
    #REPORTS_DIR.mkdir(exist_ok=True)
    #datos = ventas.groupby("categoria")["total"].sum()
    datos = ventas_por_categoria(ventas)

    datos.plot(kind="bar")

    plt.title("Ventas por categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Ventas ($)")

    plt.tight_layout()
    #plt.savefig("ventas_por_categoria.png")
    plt.savefig(REPORTS_DIR / "ventas_por_categoria.png")
    plt.close()

def generar_grafico_productos_mas_vendidos(ventas: pd.DataFrame) -> None:
    datos = ventas.groupby("producto")["cantidad"].sum()
    #datos = datos.sort_values(ascending=False)  # mayor -> menor
    datos = datos.sort_values(ascending=True)  # menor -> mayor

    datos.plot(kind="bar")

    plt.title("Productos más vendidos")
    plt.xlabel("Producto") 
    plt.ylabel("Cantidad") 
    plt.xticks(rotation=45) 
    plt.tight_layout() 
    plt.savefig(REPORTS_DIR / "productos_mas_vendidos.png") 
    plt.close()
