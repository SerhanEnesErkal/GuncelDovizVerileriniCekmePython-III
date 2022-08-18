import requests
from bs4 import BeautifulSoup

# this function scrapes the given site
def scrape(url:str, finder_template:dict):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")

    isim = soup.find_all(finder_template['part1']['tag'], finder_template['part1']['selector'])
    kur = soup.find_all(finder_template['part2']['tag'], finder_template['part2']['selector'])

    liste = []

    for i in range(len(isim)):
        isim[i] = (isim[i].text).strip("\n").strip()
        kur[i] = (kur[i].text).strip("\n").replace("\nTL"," TL").strip()
        liste.append([isim[i],kur[i]])


    print(liste)


urls = ["https://bigpara.hurriyet.com.tr/doviz/dolar/", "https://bigpara.hurriyet.com.tr/doviz/euro/", "https://uzmanpara.milliyet.com.tr/gram-altin-fiyati/","https://finans.mynet.com/borsa/"]
finder_templates = [
    {
        'part1':{
            'tag': 'h1',
            'selector': {"class":"pageTitle mBot10 pageTitleDoviz"}
        },
        'part2':{
            'tag': 'span',
            'selector': {"class":"value up"}
        }
    },
    {
        'part1':{
            'tag': 'h1',
            'selector': {"class":"pageTitle mBot10 pageTitleDoviz"}
        },
        'part2':{
            'tag': 'span',
            'selector': {"class":"value up"}
        }
    },
    {
        'part1':{
            'tag': 'span',
            'selector': {"style":"margin-top: 6px !important;display: flex;"}
        },
        'part2':{
            'tag': 'span',
            'selector': {"class":"yesilBold"}
        }
    },
    {
        'part1':{
            'tag': 'h1',
            'selector': {"class":"mr-3"}
        },
        'part2':{
            'tag': 'span',
            'selector': {"class":"dynamic-price-XU100"}
        }
    }
]

for url, finder_template in zip(urls, finder_templates):
    scrape(url, finder_template)