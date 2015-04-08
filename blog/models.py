import django.db.models
from django.contrib.auth.models import User
from django.conf import settings
class Post(django.db.models.Model):
  title= django.db.models.CharField(max_length=255)
  abstract = django.db.models.CharField(null=True, max_length=500)
  body = django.db.models.TextField(default='')
  created = django.db.models.DateTimeField(auto_now=True)
  author = django.db.models.ForeignKey(User, related_name='blogs')
  tags = django.db.models.ManyToManyField('Tag', null=True, related_name='posts')
  posted = django.db.models.BooleanField(default=False)
  category = django.db.models.ForeignKey('Category', related_name='posts')
  class Meta:
    ordering =('created',)
  def __unicode__(self):
    return unicode('Post: %s'%self.title)
    
class Tag(django.db.models.Model):
  name = django.db.models.CharField(max_length=255)

  def __unicode__(self):
    return unicode('%s'%self.name)

class Category(django.db.models.Model):
  name = django.db.models.CharField(max_length=255)
  class Meta:
    verbose_name_plural = "Categories"
  def __unicode__(self):
    return unicode('%s'%self.name)

class Comment(django.db.models.Model):
  name = django.db.models.CharField(max_length=255)
  email = django.db.models.CharField(max_length=500)
  body = django.db.models.TextField(default='')
  replyto = django.db.models.ForeignKey('Comment', related_name='replies', null=True)
  post = django.db.models.ForeignKey('Post', related_name='comments')
  created = django.db.models.DateTimeField(auto_now=True)
  class Meta:
    ordering = ('created',)
  def __unicode__(self):
    return unicode('Comment from %s'%(self.name,self.post))
    
class BlogImage(django.db.models.Model):
  image_file = django.db.models.ImageField(upload_to='blog/')
  post = django.db.models.ForeignKey('Post', related_name='images')
  def __unicode__(self):
    return unicode('Image: %s>'%self.image_file)
