import yfinance as yf

class Stock:
    def __init__(self,data):
        self.ticker = data['symbol']
        self.name = data['shortName']
        self.current_price = data['regularMarketPrice']
        self.previous_close = data['previousClose']
        self.bid = data['bid']
        self.bid_size = data['bidSize']
        self.ask = data['ask']
        self.ask_size = data['askSize']
        self.day_low = data['dayLow']
        self.day_high = data['dayHigh']
        self.fifty_two_week_high = data['fiftyTwoWeekHigh']
        self.fifty_two_week_low = data['fiftyTwoWeekLow']
        self.volume = data['volume']
        self.avg_volume = data['averageVolume']
        self.market_cap = data['marketCap']
        self.change = self.current_price - self.previous_close

    @classmethod
    def get_news(self, data):
        story_array = []
        for story in data:
            article = {
                'title': story['title'],
                'link': story['link']
            }
            if 'thumbnail' in story:
                article['image'] =  story['thumbnail']['resolutions'][0]['url']

            current_story = News(article)
            story_array.append(current_story)
        return story_array

    # @classmethod
    # def calcDown(current,previous):
    #     up_or_down = current - previous
    #     if int(up_or_down) > 0:
    #         return f'▲ {up_or_down}'
    #     else:
    #         return f'▼ {up_or_down}'

class News:
    def __init__(self,data):
        self.title = data['title']
        self.image = data.get('image', '')
        self.link = data['link']


tickers = yf.Tickers('msft aapl goog')
ticker = 'TSLA'
stock_info = yf.Ticker(ticker).info
sp500 = yf.Ticker('SI=F').info
mysp500 =Stock(sp500)
myStock = Stock(stock_info)
stock_news = yf.Ticker(ticker).news
# news = stock_news
news = Stock.get_news(stock_news)
print(mysp500.name)
print(str(mysp500.change)[:5])











