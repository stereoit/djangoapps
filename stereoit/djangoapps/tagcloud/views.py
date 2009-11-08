# Create your views here.
from django.http import HttpResponse
from django.utils import simplejson
from django.shortcuts import render_to_response, get_object_or_404
from stereoit.djangoapps.tagcloud.models import Tag, TagCloud

def tag_detail(request, slug):
    'returns tag in detail including full body'
    tag = get_object_or_404(Tag, slug=slug, active=True)
    return render_to_response('tagcloud/tag_detail.html', {'tag': tag})

def tagcloud_detail(request, slug):
    'returns tag-cloud in detail including full body'
    cloud = get_object_or_404(TagCloud, slug=slug, active=True)
    return render_to_response('tagcloud/cloud_detail.html', {'tagcloud': cloud})

class JsonResponse(HttpResponse):
	def __init__(self, data):
		HttpResponse.__init__(self, 
						content=simplejson.dumps(data),
#						mimetype='application/json'	
		)


def tag_tooltip(request, slug, mode='JSON'):
	'''
	finds info about the tag
	'''
	try:
		tag = Tag.objects.filter(slug=slug)[0]
	except Tag.DoesNotExists:
		return 'no info found'
	#return render_to_response('datadata', {'data': tag.description })
#	return HttpResponse("%s" % tag.description)
	if mode == 'JSON':
		return JsonResponse({'description':tag.description})
	else:
		return HttpResponse("%s" % tag.description)

def tag_tooltip_description(request, slug):
	return tag_tooltip(request, slug, mode="description")

