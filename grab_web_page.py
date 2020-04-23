#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup



URL = "https://www.python.org/"

def main():
    page_html = get_html(URL)
    print(page_html)
    soup = BeautifulSoup(page_html, features='lxml')
    print(soup.find_all('div', class_='copyright'))


    # response = requests(
    #     'my url',
    #     auth=('user', 'p@$$w0rd'),
    #     proxies={'http': 'http://www.mycompanyproxy.com:2020'},
    #     cookies={'foo': 'bar'},
    #     params={'spam':5, 'ham': 'toast'},
    #     data={'first_name': 'Joe', 'last_name': 'Schmoe'},
    #     headers={'X-JohnStrickler': 'NERD'},
    #     timeout=10,
    # )

def get_html(url):
    try:
        response = requests.get(url)
    except requests.HTTPError as err:
        print(err)
        exit(1)
    else:
        if response.status_code == requests.codes.OK: # is it 200??
            return response.content.decode()  # convert bytes to str

if __name__ == '__main__':
    main()
