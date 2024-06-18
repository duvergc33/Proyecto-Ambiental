import pandas as pd
import matplotlib.pyplot as plt
from Data.generators.generadorEnergia import generadorEnergia

def constrirDFGenerador():
    # Traigo los datos generados en el mock
    datosGenerador = generadorEnergia()

    # Construyo el dataframe y agrego el nombre a las columnas
    generadorDF = pd.DataFrame(datosGenerador, columns=['nombreEmpresa', 'consumoDiario', 'capacidadDePaneles', 'fecha', 'nombreEncuestado', 'id'])

    # Agrupando datos
    datosAgrupados = generadorDF.groupby("nombreEmpresa")["consumoDiario"].mean()

    # Graficando datos
    plt.figure(figsize=(20, 20))
    datosAgrupados.plot(kind='bar', color='skyblue')
    plt.title('Capacidad de generacion (KWP)')
    plt.xticks(rotation=360)
    plt.savefig('./assets/img/grafica2.png', format='png', dpi=300)
    plt.show()

constrirDFGenerador()
