from bs4 import BeautifulSoup
import requests
import codecs

# list of films
list_films = {}

# url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
# HEADER = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
# fp = requests.get(url, headers=HEADER)

# with open('file.html', 'w', encoding="utf-8") as file:
#     file.write(fp.text)

fileObj = codecs.open("file.html", "r", "utf_8_sig")
soup = BeautifulSoup(fileObj, 'html.parser')
fileObj.close()

ul_tag = soup.find('ul', 'ipc-metadata-list')
li_all_tag = ul_tag.find_all('li')
with open('result.txt', 'w', encoding="utf-8") as file:
    for li in li_all_tag:

        image = li.find('img', 'ipc-image').get('src')
        name = li.find('h3', 'ipc-title__text').text

        with open(f'parseimdb/{name}.jpg', 'wb') as target:
            a = requests.get(image)
            target.write(a.content)

        #all_span_tag = li.find_all('span', 'sc-b189961a-8 kLaxqf cli-title-metadata-item')

        year = li.find_all('span', 'sc-b189961a-8 kLaxqf cli-title-metadata-item')[0].text
        time = li.find_all('span', 'sc-b189961a-8 kLaxqf cli-title-metadata-item')[1].text

        try:
            age = li.find_all('span', 'sc-b189961a-8 kLaxqf cli-title-metadata-item')[2].text
        except:
            pass

        rating = li.find('span', 'ipc-rating-star').text
        file.write(f'{image}, {name}, {year}, {time}, {age}, {rating}\n')

