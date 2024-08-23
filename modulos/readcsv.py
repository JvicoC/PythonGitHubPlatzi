import csv
import matplotlib.pyplot as pl # as reduce la importacion

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader= csv.reader(csvfile, delimiter=',')
        primer_fila=next(reader)  
        #print(primer_fila)    
        data=[]  
        for row in reader:
            listas_unidas=zip(primer_fila,row)
            #print('*******'*5)
            #print(list(listas_unidas))
            country_dict={ikey:jvalue for ikey, jvalue in listas_unidas}
            data.append(country_dict)
        return data

def encontrar_pais(pais,data):    
    pais_encontrado=[]
    for i in data:
        if i['Country/Territory']==pais:
            pais_encontrado.append(i)
    return pais_encontrado

def encontrar_pais2(pais,data):
    pais_encontrado = list(filter(lambda i: i['Country/Territory'] == pais, data))
    return pais_encontrado

def datos_population(dicc):
    resultados = {}
    for clave, valor in dicc.items():
        if 'Population' in clave:
            if '19' in clave:
                resultados[clave] = valor
            elif '20' in clave:
                resultados[clave] = valor
    return resultados

def generate_bar_chart(diccionario):
    labels=[]
    values=[]
    for clave, valor in diccionario.items():
        labels.append(clave)
        values.append(int(valor))
    print(labels)
    print(values)
    figura, coor = pl.subplots()
    coor.bar(labels, values)
    nombre_imagen=input("Ingrese el nombre con el que se guardara el archivo: ")+".png"
    pl.savefig(nombre_imagen)
    print(f'El archivo fue guardado correctamente con el nombre {nombre_imagen}',)
    pl.show()

if __name__ =='__main__':
    data=read_csv('./data.csv')
    print('***********************'*5)
    datos_un_pais=encontrar_pais(input('Ingresar pais a selecionar:'),data)
    print('Pais encontrado=',datos_un_pais)
    dicc_poblacion=datos_population(datos_un_pais[0])
    print('Diccionario con poblacion=',dicc_poblacion)
    #print(len(dicc_poblacion))
    generate_bar_chart(dicc_poblacion)