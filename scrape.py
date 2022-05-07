import requests
from bs4 import BeautifulSoup

def create_custom_news(links, subtext):
    news = []
    for indx, item in enumerate(links):
        title = links[indx].getText()
        href = links[indx].get('href', None)
        vote = subtext[indx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(" points", ''))

            if points > 99:
                news.append({'title': title, 'link': href, 'votes': points})

    return news

all_news = []

for page in range(1,4):
    res = requests.get(f'https://news.ycombinator.com/news?p={page}')
    soup = BeautifulSoup(res.text, 'html.parser') 

    links = soup.select('.titlelink')
    subtext = soup.select('.subtext')
    
    all_news.extend(create_custom_news(links, subtext)) 

all_news.sort(key = lambda a: a['votes'], reverse = True)

print()
for item in all_news:
    print(item['votes'], 'votes')
    print(item['title'])
    print(item['link'], end = '\n\n')