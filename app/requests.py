import urllib.request,json
from .models import Sources,Articles

#Getting api key
api_key = None
#Get base url
base_url = None
#Get article url
article_url = None

def configure_request(app):
  global api_key,base_url,article_url
  api_key =app.config['NEWS_API_KEY']
  base_url =app.config['NEWS_API_BASE_URL']
  article_url =app.config['ARTICLES_API_BASE']
  
  
def get_sources(category):
  
  get_sources_url =  base_url.format(category,api_key)  
  
  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)
    
    sources_results = None
    
    if get_sources_response ['sources']:
      sources_results_list = get_sources_response['sources']
      sources_results = process_results(sources_results_list)
      
      
  return sources_results  
  
def process_results(sources_list):
  news_results = []
  for source_item in sources_list:
    id = source_item.get('id')
    name = source_item.get ('name')
    description = source_item.get('description')
    url =source_item.get('url')
    category = source_item.get('category')
    language = source_item.get('language')
    country = source_item.get('country')
    
    sources_object = Sources(id,name, description,url,category,language,country)
    news_results.append(sources_object)
    
  
    
    return news_results
  
  
def get_article(source):
  get_articles_url = article_url.format(source, api_key)
  
  with urllib.request.urlopen(get_articles_url) as url:
    source_articles_data=url.read()
    source_articles_response= json.loads(source_articles_data)
    
    article_results =None
    
  if source_articles_response ['articles']:
        articles_results_list = source_articles_response['articles']
        article_results = process_articles(articles_results_list)

        return article_results
    
    
    
def process_articles(articles_list):
    articles_results = []
    for article_item in articles_list:
        source= article_item.get('source')
        author = article_item.get('author')
        title = article_item.get ('title')
        description = article_item.get('description')
        url =article_item.get ('url')
        urlToImage=article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        
        articles_object = Articles(source,author,title,description,url,urlToImage,publishedAt)
        articles_results.append(articles_object)
        
    
  
    
    return articles_results
      
      
      
      
      
      
      
       

 
  
      
  
  
  