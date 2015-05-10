from django.db import models

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=255)
    tags=models.ManyToManyField("Tag",related_name='projects')
    description=models.TextField()
    icon = models.ImageField(upload_to='projects/')
    def __unicode__(self):
        return unicode('%s'%self.title)
class Link(models.Model):
    title=models.CharField(max_length=255)
    url=models.URLField(max_length=400)
    project=models.ForeignKey('Project',related_name='links')
    def __unicode__(self):
        return unicode('%s<%s>'%(self.title,self.url))
class Tag(models.Model):
    name=models.CharField(max_length=255)
    def __unicode__(self):
        return unicode('%s'%(self.name))
class Screenshot(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='projects/screens/')
    project=models.ForeignKey('Project',related_name='screens')
    def __unicode__(self):
        return unicode('%s: %s'%(self.title,self.image))
