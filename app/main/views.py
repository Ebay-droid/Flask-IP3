from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_article


@main.route('/')
def News():
  '''
  returns News page and data
  '''

  #Getting gen news
  general_news = get_sources('general')
  #Getting sports news
  sports_news = get_sources('sports')
  #Getting entertainment news
  entertainment_news = get_sources ('entertainment')
  
  return render_template('sources.html',general =general_news,sports= sports_news,entertainment=entertainment_news)
 
 
@main.route('/Articles')
def Article():
  
   general = get_article('general')
   sports = get_article('sports')
   entertainment = get_article('entertainment')
  
   return render_template('articles.html',general=general, sports= sports, entertainment= entertainment) 

# @main.route('/r') 