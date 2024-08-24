import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/products')
    #r=requests.delete()
    print(r.status_code)
    #print(r.text)
    print(type(r))
    categories=r.json()
    #print('******'*5,categories)
    for category in categories:
        print(category['id'])

