import google.generativeai as genai
import os

class MarketBrain:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analyze_impact(self, news_text):
        prompt = f"""
        Como analista sênior, avalie a probabilidade de impacto desta notícia:
        Notícia: {news_text}
        
        Retorne:
        - Sentimento (-10 a 10)
        - Ativos possivelmente afetados
        - Justificativa breve baseada em cenários.
        """
        response = self.model.generate_content(prompt)
        return response.text