from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from stereoit.djangoapps.news.models import News


class NewsAdmin(admin.ModelAdmin):
	search_fields = ['title', 'author', 'date', 'summary']
	date_hierarchy = 'date_add'
	list_filter = ['author','date_add','published']
	list_display = ['title','date_add','author', 'published']
	verbose_name = 'News'
	verbose_name_plural = 'News'
	prepopulated_fields = {'slug': ('title',)}

	fieldsets = (
		(None, { 
			'fields': (
					'title','slug','author',
					'summary','date_add','published'
			)
		}),
		('Advanced', {	
			'classes': ('collapse',),
			'fields': ('content',)
		}),
	)


admin.site.register(News, NewsAdmin)
