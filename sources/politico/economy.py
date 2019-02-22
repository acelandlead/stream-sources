from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'Politico',
        'category': 'economy',
        'url': 'https://www.politico.com',
    }

    FEED_URL = 'https://www.politico.com/rss/economy.xml'
