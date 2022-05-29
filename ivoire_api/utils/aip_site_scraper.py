import requests, string
from datetime import datetime
from bs4 import BeautifulSoup
from news.models import Article





print('Start time: ' + str(datetime.now()))
def scrape_aip_website():
    language = 'fr'
    website = 'https://www.aip.ci/'
    ponctuations = set(string.punctuation)

    url = 'https://www.aip.ci/category/depeches/'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    print('Starting scraping AIP website')
    print('Start time: ' + str(datetime.now()))
    for article in soup.find_all('article'):
        try:
            title = article.div.header.h2.a.text
            publish_date = soup.find('time', class_='entry-published')['datetime']
            summary = soup.find('div', class_='entry-summary').p.text
            full_url = soup.find('a', class_='entry-featured-img-link')['href']
            picture_url = soup.find('img', class_='entry-content-featured-img')['srcset']
            tags = soup.find('div', class_='entry-byline-cats').a.text
            author = soup.find('span', class_='entry-author').text

            category_list = ''.join(tag for tag in tags if tag not in ponctuations).split()
            category = category_list[-1]

            details = requests.get(full_url).text
            details_soup = BeautifulSoup(details, 'lxml')

            content_div = details_soup.find('div', class_='entry-the-content')
            contents = content_div.find_all('p')
            content = ''
            for text in contents:
                content = f'{text} {text}'

            news_article = Article.objects.create(
                title=title,
                author=author,
                picture_url=picture_url,
                content=content,
                summary=summary,
                tags=tags,
                category=category,
                published_on=publish_date,
                language=language,
                website=website,
                full_url=full_url
            )
            print('\n\n=========================================\n\n\n')
            print(f'Article created successfully: {news_article}')
            print(title)
            print(author)
            print(picture_url)
            print(category)
            print(tags)
            print(publish_date)
            print(language)
            print(website)
            print(full_url)
            print(summary)
            print(content)
            print('=========================================')
        
        except:
            Article.objects.create(
                is_public=False,
                language=language,
                website=website,
            )
            pass





scrape_aip_website()



print('End time: ' + str(datetime.now()))

