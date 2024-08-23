import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader= csv.reader(csvfile, delimiter=',')# usamos csv.reader para convertir a un archivo de tipo csv para su mejor trabajabilidad donde cada fila es una lista
        for row in reader:
            print('*******'*5)
            print(row)
        '''print('##################################')#aqui probamos como un tipo de archivo de texto plano y el resultado es lineas de texto plano
        print(type(csvfile))
        print(csvfile)
        print('##################################')     
        print('lista',list(csvfile.readline()))
        print(csvfile.readline())
        print(csvfile.readline())
        print(csvfile.readline())'''


if __name__ =='__main__':
    read_csv('./modulos/data.csv')