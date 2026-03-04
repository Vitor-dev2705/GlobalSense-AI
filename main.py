import os
from dotenv import load_dotenv
from src.collectors.news_api import NewsCollector
from src.brain.sentiment import MarketBrain

load_dotenv() # Carrega as chaves do .env

def run_system():
    print("--- GlobalSense AI Iniciado ---")
    
    # 1. Coleta
    collector = NewsCollector()
    news_list = collector.fetch_global_news("Central Bank")
    
    # 2. Processamento (Exemplo com a primeira notícia)
    if news_list:
        brain = MarketBrain()
        top_news = news_list[0]
        
        print(f"Analisando: {top_news['title']}")
        relatorio = brain.analyze_impact(top_news['title'])
        
        print("\n--- RELATÓRIO DE CENÁRIO ---")
        print(relatorio)

if __name__ == "__main__":
    run_system()