from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from stereoit.djangoapps.news.models import News

def detail(request, slug):
	'returns news in detail including full body'
	news = get_object_or_404(News, slug=slug, published=True)
	return render_to_response('news/detail.html', {'news': news})
