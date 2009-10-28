'''
Custom tags and filters for stereoit.djangoapps.news application
this include tags:

	* render_news - will render 1 news
	* news_as_li - will iterate on news_list and render it as <ul><li></li></ul>
'''

from django import template
from stereoit.djangoapps.news.models import News

register = template.Library()

@register.inclusion_tag('templatetags/news.html')
def show_news(number=5):
    news = News.objects.all().order_by('-date_add')[:number]
    return {'news': news }


@register.inclusion_tag('templatetags/news.html')
def show_css_news(items=5, css_class=''):
	context = show_news(items)
	context['css_class'] = css_class
	return context

