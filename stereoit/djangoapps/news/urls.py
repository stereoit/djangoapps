from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list


from stereoit.djangoapps.news.models import News


news_dict = {
	'queryset' : News.objects.all()
}

urlpatterns = patterns('stereoit.djangoapps.news.views',
#     (r'show/1/$', 'news_test'), #show news detail
	(r'^$', direct_to_template, {'template': 'news/index.html'}),
	(r'^archive/$', object_list, dict(
				news_dict, 
				paginate_by=20,
				template_object_name='news',
			)),
    url(r'^(?P<slug>[-\w]+)/$', 'detail', name="news_detail"), #show news detail
)
