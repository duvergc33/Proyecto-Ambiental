import pandas as pd
import matplotlib.pyplot as plt
from Data.generators.generadorCompaniasSolares import generadorCompanias

def construirDFCompaniasSolares():
    # Traigo los datos generados en el mock
    datosCompanias = generadorCompanias

    # Construyo el dataframe y agrego el nombre a las columnas
    companiasDF = pd.DataFrame(datosCompanias, columns=['nombreEmpresa', 'panelesCompanias', 'capacidadDePaneles', 'fecha', 'nombreEncuestado', 'id'])

    # Agrupando datos
    datosAgrupados = companiasDF.groupby("nombreEmpresa")["panelesCompanias"].mean()

    # Graficando datos
    plt.figure(figsize=(20, 20))
    datosAgrupados.plot(kind='bar', color='skyblue')
    plt.title('Compañias Solares')
    plt.xticks(rotation=360)
    plt.savefig('./assets/img/grafica1.png', format='png', dpi=300)
    plt.show()

construirDFCompaniasSolares()
