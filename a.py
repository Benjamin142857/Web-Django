import requests

if __name__ == '__main__':
    req = requests.get(url='https://raw.githubusercontent.com/Benjamin142857/Web-Django/master/templates/Django%20ORM.md')

    with open('a.md', 'wb') as f:
        f.write(req.content)
        f.close
    
