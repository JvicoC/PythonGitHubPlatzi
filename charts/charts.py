import matplotlib.pyplot as pl

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = pl.subplots()
    ax.pie(values, labels=labels)
    nombre_imagen=input("Ingrese el nombre con el que se guardara el archivo: ")+".png"
    pl.savefig(nombre_imagen)
    print(f'El archivo fue guardado correctamente con el nombre {nombre_imagen}',)
    pl.close()