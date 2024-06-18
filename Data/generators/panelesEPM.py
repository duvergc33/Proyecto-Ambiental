import random

def panelesEPM():
    listaDatos=[]
    for i in range(1800):
        lugar=random.choice(['Plaza mayor etapa 1','Plaza mayor etapa 2','Parque comercial el tesoro'])
        cantidadPaneles=random.randint([0,504,600,700,900,1200,1400,1568])
        fecha=random.choice(['2024-05-14','2024-05-15'])
        nombreEncuestado=random.choice(['Pedro','Sandra','Martina','Kevin','Valentina','Juan'])
        id=random.randint(0,100)

        informacionPaneles=[lugar,cantidadPaneles,fecha,nombreEncuestado,id]

        listaDatos.append(informacionPaneles)
    return listaDatos

