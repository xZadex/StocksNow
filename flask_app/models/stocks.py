from flask_app import app

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

class News:
    def __init__(self,data):
        self.title = data['title']
        self.image = data.get('image', 'https://heuft.com/upload/image/400x267/no_image_placeholder.png')
        self.link = data['link']