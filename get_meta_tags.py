import requests
from bs4 import BeautifulSoup


def main():
    r = requests.get('http://127.0.0.1:8000/seo-toronto/')
    soup = BeautifulSoup(r.content, features="html.parser")

    meta = soup.find_all('meta')

    for tag in meta:
        print(tag)


if __name__ == '__main__':
    main()
