from django.db import models

# Create your models here.

class Post(models.Model):
	"""docstring for Post"""
	create_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length = 100)
	content = models.TextField()

	def __unicode__(self):
		return str(self.id) + "||" + str(self.title) + "||\n" + str(self.content)


class Resume(models.Model):
	create_at = models.DateTimeField(auto_now_add= True)
	title = models.CharField(blank = True, null = True,max_length = 100)
	address = models.CharField(blank = True, null = True,max_length = 100)
	phone = models.CharField(blank = True, null = True,max_length = 100)
	email = models.CharField(blank = True, null = True,max_length = 100)
	git_link = models.CharField(blank = True, null = True,max_length = 100)
	objective = models.CharField(max_length = 100)
	ob_content = models.TextField()
	projects = models.CharField(max_length = 100)
	pr_content = models.TextField()
	skills = models.CharField(max_length = 100,blank =True, null =True)
	sk_content = models.TextField(blank=True, null =True)
	research = models.CharField(max_length = 100)
	re_content = models.TextField()
	education = models.CharField(max_length = 100)
	ed_content = models.TextField()

	def __unicode__(self):
		return str(self.id)


