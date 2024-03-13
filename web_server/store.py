
import requests

def get_categories():
    r = requests.get('https://www.mymsfep.com/ranking')
    print(r.status_code)
    print(r.text)
    categories = r.json()
    for category in categories:
        print(category["name"])