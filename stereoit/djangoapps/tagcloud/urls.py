from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list

from stereoit.djangoapps.tagcloud.models import Tag, TagCloud

tags_dict = {
	'queryset' : Tag.objects.all()
}

urlpatterns = patterns('stereoit.djangoapps.tagcloud.views',
	(r'^$', direct_to_template, {'template': 'tagcloud/index.html'}),
    url(r'ajax/description/(?P<slug>[-\w]+)/$', 'tag_tooltip_description', name="ajax-tag-description"),
    url(r'ajax/(?P<slug>[-\w]+)/$', 'tag_tooltip', name="ajax-tag"), #show tag detail
    url(r'^cloud/(?P<slug>[-\w]+)/$', 'tagcloud_detail', name="tagcloud_detail"), #show the coud detail
    url(r'(?P<slug>[-\w]+)/$', 'tag_detail', name="tag_detail"), #show tag detail
)
