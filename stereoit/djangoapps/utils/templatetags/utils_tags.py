'''
Custom tags and filters for stereoit.djangoapps.tagcloud application
this include tags:

'''

from django import template

register = template.Library()

@register.inclusion_tag('templatetags/utils/go_home.html')
def go_home(url="/"):
	return {'url': url}

