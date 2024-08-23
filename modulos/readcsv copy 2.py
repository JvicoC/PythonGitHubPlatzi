import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader= csv.reader(csvfile, delimiter=',')# usamos csv.reader para convertir a un archivo de tipo csv para su mejor trabajabilidad donde cada fila es una lista
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



if __name__ =='__main__':
    data=read_csv('./modulos/data.csv')
    print(data[0])