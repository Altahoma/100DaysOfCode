from bs4 import BeautifulSoup
import requests


web_page = 'https://news.ycombinator.com/'
response = requests.get(web_page)
soup = BeautifulSoup(response.content, 'html.parser')
articles = soup.find_all(name='a', class_='titlelink')

article_titles = []
article_limks = []
for article in articles:
    title = article.get_text()
    article_titles.append(title)

    link = article.get('href')
    article_limks.append(link)

article_scores = [int(score.get_text().split()[0]) for score in soup.find_all(name='span', class_='score')]
largest_score = max(article_scores)
largest_score_index = article_scores.index(largest_score)

print(article_titles[largest_score_index])
print(article_limks[largest_score_index])
