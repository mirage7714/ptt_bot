import requests
from bs4 import BeautifulSoup as soup
import sys


main_url = 'https://www.ptt.cc'


def get_page_links(url, main_url):
    page_req = requests.get(url)
    cont = soup(page_req.text, 'lxml')
    links = cont.find_all('div',{'class':'title'})
    link_list = []
    for link in links:
        try:
            urls = link.find_all('a')
            for u in urls:
                link_list.append(main_url+u.attrs['href'])
        except:
            continue
    return link_list


def get_page_content(url):
    po_cont = []
    req = requests.get(url)
    tree = soup(req.text, 'lxml')
    meta = tree.find_all('span',{'class':'article-meta-value'})
    po_cont.append({
            'Author' : meta[0].text,
            'Name' : meta[2].text,
            #'Time' : datetime.strptime(meta[3].text, '%a %b %d %H:%M:%S %Y'),
            'Time': meta[3].text,
            'Url': url
            })
    return po_cont


if __name__ == "__main__":
    board = sys.argv[1]
    keyword = sys.argv[2]
    interval = sys.argv[3]
