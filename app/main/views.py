from flask import render_template, redirect, url_for, request
from . import main
from ..models import Sources
from ..requests import get_articles, get_sources, topheadlines

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = "Home - News From Various News Sources"

    general_category = get_sources('general')
    business_category = get_sources('business')
    entertainment_category = get_sources('entertainment')
    sports_category = get_sources('sports')
    technology_category = get_sources('technology')
    science_category = get_sources('science')
    health_category = get_sources('health')

    return render_template('index.html', title = title, general = general_category, business = business_category, entertainment = entertainment_category, sports = sports_category,tech = technology_category, science = science_category, health = health_category)


@main.route('/articles/<source_id>&<int:per_page>')
def articles(source_id, per_page):
    '''
    Function that returns articles based on their sources
    '''
    news_source = get_articles(source_id, per_page)
    title = f'{source_id} | All Articles'

    return render_template('articles.html', title = title, name = source_id, news = news_source)


@main.route('/topheadlines&<int:per_page>')
def headlines(per_page):
    '''
    Function that returns top headlines articles
    '''
    topheadlines_news = topheadlines(per_page)
    title = 'Top Headlines'

    return render_template('topheadlines.html', title = title, name = 'Top Headlines', news = topheadlines_news)