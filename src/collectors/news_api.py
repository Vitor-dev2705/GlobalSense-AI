import requests
import os

class NewsCollector:
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")
        self.base_url = "https://newsapi.org/v2/everything"

    def fetch_global_news(self, query="economy"):
        params = {
            'q': query,
            'sortBy': 'publishedAt',
            'apiKey': self.api_key,
            'language': 'en'
        }
        response = requests.get(self.base_url, params=params)
        return response.json().get('articles', [])