import random

def generadorCompanias():
    listaDatos = []

    for i in range(800):
        nombreEmpresa = random.choice(['Bancolombia', 'EPM', 'Chocolates', 'Bioversity-CIAT', 'Ecopetrol'])
        panelesCompanias = random.randint([0,545000])
        capacidadDePaneles = random.randint([200, 125])
        fecha = random.choice(['2024-05-14', '2024-05-15'])
        nombreEncuestado = random.choice(['Pedro', 'Sandra', 'Martina', 'Kevin', 'Valentina', 'Juan'])
        id = random.randint(0, 5000000)
        
        generadorDeCompanias = [nombreEmpresa, panelesCompanias, capacidadDePaneles, fecha, nombreEncuestado, id]
        
        listaDatos.append(generadorDeCompanias)
    
    return listaDatos
