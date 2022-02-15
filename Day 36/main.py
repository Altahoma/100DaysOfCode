import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

url_stock = 'https://www.alphavantage.co/query'
params_stock = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': 'example'
}
response_stock = requests.get(url_stock, params_stock)
response_stock.raise_for_status()
data_stock = response_stock.json()['Time Series (Daily)']
data_stock_list = [value for value in data_stock.values()]

yesterday_data = data_stock_list[0]
yesterday_close_price = float(yesterday_data['4. close'])

day_before_yesterday_data = data_stock_list[1]
day_before_yesterday_close_data = float(day_before_yesterday_data['4. close'])

difference = round(yesterday_close_price - day_before_yesterday_close_data, 2)
difference_in_percent = abs(round(yesterday_close_price / day_before_yesterday_close_data * 100 - 100, 2))

if difference_in_percent > 5:
    if difference < 0:
        result = '🔻'
    else:
        result = '🔺'
    title = f'{STOCK}: {result}{difference}$\n'

    url_news = 'https://newsapi.org/v2/everything'
    params_news = {
        'q': COMPANY_NAME,
        'searchIn': 'title',
        'sortBy': 'publishedAt',
        'apiKey': 'example'
    }
    response_news = requests.get(url_news, params_news)
    articles = response_news.json()['articles']
    first_three_articles = articles[:3]
    formatted_articles = [f"Headline: {article['title']}.\n" 
                          f"Brief: {article['description']}" for article in first_three_articles]

    for sms in formatted_articles:
        account_sid = 'example'
        auth_token = 'example'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                    body=title + sms,
                    from_='example',
                    to='example'
            )
        print(message.status)
