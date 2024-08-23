import utils

lista1 = [
    {
        'pais':'col',
        'population':500
    },
    {
        'pais':'bol',
        'population':300
    },
    {
        'pais':'per',
        'population':200
    }
]

def run01():
    keys, values=utils.get_population()

    print(f'Keys es {keys},y lo valores es {values}')

    pais=input('Tipo de pais: ')

    print(f'el resultado es :{utils.pop_by_country(lista1,pais)}.')

if __name__ =='__main__':
    run01()