import os

class Config:
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?&category={}&apiKey={}'
  
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  
  ARTICLES_API_BASE = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
  
class ProdConfig(Config):
  pass
  
  
  
class DevConfig(Config):  
  DEBUG = True
  
  
config_options = {
  'development': DevConfig,
  'production': ProdConfig
}    