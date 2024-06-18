import pandas as pd
import matplotlib.pyplot as plt
from Data.generators.panelesEPM import panelesEPM

def construirDFPanelesEPM():
    #Traigo los datos generados en el mock
    datosPaneles=panelesEPM()

    #Construyo el dataframe y agrego el nombre a las columnas
    panelesDF=pd.DataFrame(datosPaneles,columns=['lugar','cantidadPaneles','fecha','nombreEncuestado','id'])

    #Agrupando datos
    datosAgrupados=panelesDF.groupby("lugar")["cantidadPaneles"].mean()

    #Graficando datos
    plt.figure(figsize=(20,20))
    datosAgrupados.plot(kind='bar',color='skyblue')
    plt.title('EPM')
    plt.xticks(rotation=360)
    plt.savefig('./assets/img/grafica3.png', format='png',dpi=200)
    plt.show()

construirDFPanelesEPM()

