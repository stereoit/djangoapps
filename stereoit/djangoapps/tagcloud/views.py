# Create your views here.
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
