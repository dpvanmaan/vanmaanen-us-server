from django.db import models

# Create your models here.
class Image(models.Model):
    name=models.CharField(max_length=255)
    pic=models.ImageField(upload_to='misc/')
    category=models.ForeignKey('Category',related_name='images')
    def __unicode__(self):
        return unicode('%s: %s'%(self.name,self.pic))
class Text(models.Model):
    name=models.CharField(max_length=255)
    body=models.TextField()
    text_type=models.CharField(max_length=50,choices=[('md','markdown'),('htm','html')])
    category=models.ForeignKey('Category',related_name='texts')
    def __unicode__(self):
        return unicode('%s'%self.name)
class Category(models.Model):
    name=models.CharField(max_length=255)
    def __unicode__(self):
        return unicode('%s'%self.name)
class File(models.Model):
    name=models.CharField(max_length=255)
    filename=models.FileField(upload_to='misc/')
    category=models.ForeignKey('Category',related_name='files')
    def __unicode__(self):
        return unicode('%s: %s'%(self.name,self.filename))
