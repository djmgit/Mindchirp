from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    post_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    username = models.CharField(max_length=200,default="anonymous")
    image=models.FileField(upload_to='images/%Y/%m/%d',default='no image available for this post')
    def __str__(self): 
        return self.post_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
        


'''
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
'''        


class Comment(models.Model):
	post=models.ForeignKey(Post,on_delete=models.CASCADE)
	username=models.CharField(max_length=200,default='none')
	comment_text=models.CharField(max_length=200)
    	
	def __str__(self):
		return self.comment_text
	

