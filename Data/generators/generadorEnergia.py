import random

def generadorEnergia():
    listaDatos = []

    for i in range(500):
        nombreEmpresa = random.choice(['Bancolombia', 'EPM', 'Chocolates', 'Bioversity-CIAT', 'Ecopetrol'])
        consumoDiario = random.choice(['1500w', '2500w', '3000w', '5000w', '11000w'])
        capacidadDePaneles = random.choice(['200', '125', '670'])
        fecha = random.choice(['2024-05-14', '2024-05-15'])
        nombreEncuestado = random.choice(['Pedro', 'Sandra', 'Martina', 'Kevin', 'Valentina', 'Juan'])
        id = random.randint(0, 5000000)
        
        # Elimina 'w' y convierte consumoDiario a entero
        consumoDiario = int(consumoDiario.replace('w', ''))
        # Convierte capacidadDePaneles a entero
        capacidadDePaneles = int(capacidadDePaneles)
        
        generadorDeEnergia = [nombreEmpresa, consumoDiario, capacidadDePaneles, fecha, nombreEncuestado, id]
        
        listaDatos.append(generadorDeEnergia)
    
    return listaDatos
