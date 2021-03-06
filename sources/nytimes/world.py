from sources.generic import FeedSource


class Source(FeedSource):

    SOURCE = {
        'name': 'The New York Times',
        'category': 'world',
        'url': 'https://www.nytimes.com',
    }

    FEED_URL = 'http://rss.nytimes.com/services/xml/rss/nyt/World.xml'
