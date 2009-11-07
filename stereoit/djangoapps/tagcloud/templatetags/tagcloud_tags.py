'''
Custom tags and filters for stereoit.djangoapps.tagcloud application
this include tags:

'''

from django import template
from stereoit.djangoapps.tagcloud.models import Tag, TagCloud

register = template.Library()

@register.inclusion_tag('templatetags/tagcloud.html')
def render_tagcloud(name):
	try:
		cloud = TagCloud.objects.filter(name=name)[0]
		tags = cloud.tags.all()
#		assert False, cloud
	except TagCloud.DoesNotExist:
		pass 
	return {'cloud': cloud, 'tags': tags }

@register.inclusion_tag('templatetags/tag.html')
def render_tag(name):
	try:
		tag = Tag.objects.filter(name=name)[0]
	except Tag.DoesNotExist:
		pass # die silently
	return { 'tag': tag }
	

@register.inclusion_tag('templatetags/tag_detail.html')
def render_tag_detail(name):
	try:
		tag = Tag.objects.filter(name=name)[0]
	except Tag.DoesNotExist:
		pass # die silently
	return { 'tag': tag}

#def show_css_news(items=5, css_class=''):
#	context = show_news(items)
#	context['css_class'] = css_class
#	return context

