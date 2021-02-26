import requests,json
from .models import Sources,Articles
from datetime import datetime

apiKey = None
sources_url = None
articles_url = None
topheadlines_url = None
everything_url = None
everything_search_url = None

def configure_request(app):
    global apiKey, sources_url, articles_url, topheadlines_url
    apiKey = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_BASE_URL']
    articles_url = app.config['ARTICLE_SOURCE_BASE_URL']
    topheadlines_url = app.config['TOP_HEADLINES_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json repsonse to out url request
    '''
    get_sources_url = 'https://newsapi.org/v2/top-headlines?country=us&category={}&sortBy=publishedAt&apiKey={}'.format(category,apiKey)

    get_sources_response = requests.get(get_sources_url).json() 
    
    sources_results = None
    
    if get_sources_response['articles']:
        get_sources_list = get_sources_response['articles']
        sources_results = process_results(get_sources_list)

    return sources_results


def process_results(sources_list):
    '''
    Function that process our json results
    '''
    sources_results = []

    for source in sources_list:
        author = source.get('author')
        title = source.get('title')
        urlToImage = source.get('urlToImage')
        description = source.get('description')
        url = source.get('url')
        publishedAt = source.get('publishedAt')

        if urlToImage:
            source_object = Articles(author, title, description, url, urlToImage, publishedAt)
            sources_results.append(source_object)

    return sources_results


def get_articles(source_id, article):
    '''
    Function that gets articles based on the source id
    '''
    get_article_location_url = articles_url.format(source_id, article, apiKey)

 
    articles_location_response = requests.get(get_article_location_url).json()

    articles_location_results = None

    if articles_location_response['articles']:
        articles_location_list = articles_location_response['articles']
        articles_location_results = process_articles(articles_location_list)

    return articles_location_results


def process_articles(my_articles):
    '''
    Fucntion that processes the json reults for the articles
    '''
    article_location_list = []

    for article in my_articles:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        date_published = article.get('publishedAt')

        publishedAt = datetime(year=int(date_published[0:4]), month=int(date_published[5:7]), day=int(date_published[8:10]), hour=int(date_published[11:13]), minute=int(date_published[14:16]))

        if urlToImage:
            article_source_object = Articles(author, title, description, url, urlToImage, publishedAt)
            article_location_list.append(article_source_object)

    return article_location_list


def topheadlines(category):
    '''
    Function that gets articles based on the source id
    '''
    get_topheadlines_url = topheadlines_url.format(apiKey)

    
    topheadlines_response = requests.get(get_topheadlines_url).json()

    topheadlines_results = None
        
    if topheadlines_response['articles']:
        topheadlines_list = topheadlines_response['articles']
        topheadlines_results = process_articles(topheadlines_list)

    return topheadlines_results

def get_news_sources():
    '''
    '''
    get_news_sources_url = 'http://newsapi.org/v2/sources?apiKey={}'.format(apiKey)

    get_news_sources_response = requests.get(get_news_sources_url).json()

    get_news_sources_results = None

    if get_news_sources_response['sources']:
        news_sources_list = get_news_sources_response['sources']
        get_news_sources_results = process_sources(news_sources_list)

    return get_news_sources_results

def process_sources(news_list):
    '''
    '''
    get_news_sources_results = []
    for news in news_list:
        id = news.get('id')
        name = news.get('name')

        if id:
            news_object = Sources(id, name)
            get_news_sources_results.append(news_object)

    return get_news_sources_results


