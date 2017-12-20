from bs4 import BeautifulSoup
import re
import urllib.request

def weather():
    attempts = 5
    while attempts:
        try:
            get = urllib.request.Request('https://weather.com/weather/today/l/42.00,21.43')
            with urllib.request.urlopen(get) as response:
                html = response.read().decode('utf-8')
                degree = re.search('<span class="">(.*?)<sup>', html).group(1)
                group = re.search('class="today_nowcard-phrase">(.*?)<', html).group(1)
                weather = degree + '°C, ' + group
            break
        except ConnectionResetError or TimeoutError :
            print('Соединение потеряно!')
            time.sleep(30)
            attempts -=1
    if not attempts:
        print('Попытки закончились')
        weather = 'unknown'
    return weather

def download(d):
    values = d.values()
    top=[]
    for i in range (10):
        maxim=max(values)
        for k, v in d.items():
            if v == maxim:
                if k not in a:
                    a.append(k)
                    d.pop(k)
                break
        values.remove(maxim)
    return a

def module():
    attempts = 5
    while attempts:
        try:
            get = urllib.request.Request('https://nplus1.ru/')
            with urllib.request.urlopen(get) as response:
                html = response.read().decode('utf-8')
                soup = BeautifulSoup(html, 'html.parser')
                text = soup.get_text()
                rus = re.findall('[А-ЯЁа-яё ]{2,}', text)
                s = {}
                for w in rus:
                    w = w.strip()
                    if w:
                        if w not in s:
                            s[w] = 1
                        else:
                            s[w] += 1
                top = get_top10(s)
                rus = ' '.join(s.keys())
            break
        except ConnectionResetError or TimeoutError :
            print('Соединение потеряно!')
            time.sleep(30)
            rus = []
            attempts -=1
    if not attempts:
        print('Попытки закончились')
        rus = []
    return rus, top

def dictionary():
    attempts = 5
    while attempts:
        try:
            get = urllib.request.Request('http://www.dorev.ru/ru-index.html?l=c0')
            with urllib.request.urlopen(get) as response:
                html = response.read().decode('Windows-1251')
                soup = BeautifulSoup(html, 'html.parser')
                text = soup.get_text()
                links = []
                link_items = soup.find_all('a')
                for a in link_items:
                    links.append(a.get('href'))
                letter_links = []
                for link in links:
                    if link:
                        if 'ru-index.html?l=' in link:
                            letter_links.append(link)
                d = set(letter_links)
            break
        except ConnectionResetError or TimeoutError :
            print('Соединение потеряно')
            time.sleep(30)
            attempts -=1
    if not attempts:
        print('Попытки закончились')
        dic = set()
    return dic
