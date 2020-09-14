from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_source


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
 
 
# @main.route('/Articles/cnn')
# def cnn_articles():
  
#     cnn_news = get_article('cnn')
   
  
#     return render_template('articles.html',cnn= cnn_news) 

# @main.route('/Articles/reuters')
# def  reuters_articles():
  
#   reuters = get_article('reuters')
  
#   return render_template('articles.html', reuters =reuters)


# @main.route('/Articles/bloomberg')
# def bloomberg_articles():
  
#   bloomberg = get_article('bloomberg')
  
#   return render_template('articles.html', bloomberg=bloomberg)

@main.route('/Articles/<id>')
def Articles(id):
    
    article = get_source(id)
   
    

  
    return render_template('articles.html', article =article)