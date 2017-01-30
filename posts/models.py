

from django.db import models
'''
from comments.models import Comment
'''
from PIL import Image
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to=r'/home/navaneetha/Pictures', null=True, blank=True)
    published = models.DateField(auto_now=False, auto_now_add=False, null=True)
    name = models.CharField(max_length=200)
    subscibers = models.IntegerField(default=0)
    subscribe = models.EmailField()
    draft = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
    	ordering = ['published','updated']

'''
@property
def comments(self):
    instance = self
    qs = Comment.objects.filter_by_instance(instance)
    return qs
'''