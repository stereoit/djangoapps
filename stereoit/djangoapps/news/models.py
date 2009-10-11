from django.db import models

# Create your models here.

class News(models.Model):
	'''
	Represents 'News' object which includes things like:

		* title - short and descriptive
		* slug - urlized title
		* author - owner of the title
		* summary - short descriptin text of the news
		* content - long text with the news
		* date - date of creation of the date
	'''
	title = models.CharField(max_length=30, 
			help_text='Short and description caption of the News')
	slug = models.SlugField(max_length=30,
			help_text="URL'ized version of the title, automatic")
	author = models.CharField(max_length=60, help_text="Author's name")
	summary = models.TextField('Short Content',help_text="Short content of the News")
	content = models.TextField(null=True,blank=True,
			help_text="Complete content of the News, is optional")
	date_add = models.DateTimeField('Date created',help_text='Day published')
	published = models.BooleanField(default=True, help_text='Is the news published?')

	class Meta:
		verbose_name_plural = 'News'
		ordering = ['date_add']

	def __unicode__(self):
		'returns some prettified output of itself'
		return '%s' % self.title

	@models.permalink
	def get_absolute_url(self):
		return ('news_detail', [str(self.slug)])
	#	return ('stereoit.djangoapps.news.views.detail', [str(self.slug)])
	
