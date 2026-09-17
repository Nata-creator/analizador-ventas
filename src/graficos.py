import matplotlib.pyplot as plt
import pandas as pd


def generar_grafico_categorias(ventas: pd.DataFrame) -> None:
    datos = ventas.groupby("categoria")["total"].sum()

    datos.plot(kind="bar")

    plt.title("Ventas por categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Ventas ($)")

    plt.tight_layout()
    plt.savefig("ventas_por_categoria.png")
    plt.close()
