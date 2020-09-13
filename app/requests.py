import urllib.request,json
from models import Sources

#Getting api key
api_key = None
#Get base url
base_url = None

def configure_request(app):
  global api_key,base_url
  api_key =app.config['NEWS_API_KEY']
  base_url =app.config['News_API_BASE_URL']
  
  
  
def get_sources(category):
  
  get_sources_url =  base_url.format(category,api_key)  
  
  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.load.read()
    get_sources_response = json.loads(get_sources_data)
    
    sources_results = None
    
    if get_sources_response ['results']:
      sources_results_list = get_sources_response['results']
      sources_results = process_results(sources_results_list)
      
    return sources_results  
  
def process_results(sources_list):
  sources_results = []
  for source in sources_list:
    id = source.get('id')
    name = source.get ('name')
    description = source.get('description')
    url = ('url')
    category = ('category')
    language = ('language')
    country = ('country')
    
    return sources_results
    
  
  
  