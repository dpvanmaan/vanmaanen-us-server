import django.db.models

class Skill(django.db.models.Model):
  skill = django.db.models.CharField(max_length=255)
  exp_level = django.db.models.ForeignKey('SkillLevel', related_name='skills')

  def __unicode__(self):
    return unicode('%s'%self.skill)

class SkillLevel(django.db.models.Model):
  name = django.db.models.CharField(max_length=255)

  def __unicode__(self):
    return unicode('%s'%self.name)

class Experience(django.db.models.Model):
  class Meta:
    ordering = [ 'order' ]
  job_title = django.db.models.CharField(max_length=500)
  company = django.db.models.CharField(max_length=500)
  description = django.db.models.TextField(default='')
  start = django.db.models.DateField()
  end = django.db.models.DateField(null=True)
  current = django.db.models.BooleanField(default=False)
  location = django.db.models.CharField(max_length=500)
  order = django.db.models.IntegerField(unique=True)
  category = django.db.models.ForeignKey('ExperienceCategory', related_name='jobs')

  def __unicode__(self):
    return unicode('%s at %s'%(self.job_title,self.company))

class ExperienceCategory(django.db.models.Model):
  name = django.db.models.CharField(max_length=255)
  class Meta:
        verbose_name_plural = "Experience categories"
  def __unicode__(self):
    return unicode('%s'%self.name)

class Education(django.db.models.Model):
  class Meta:
        verbose_name_plural = "Education"
  school = django.db.models.CharField(max_length=255)
  grad_date = django.db.models.DateField(null=True)
  degree = django.db.models.CharField(max_length=500)
  description = django.db.models.TextField(default='')

  def __unicode__(self):
    return unicode('%s from %s '%(self.degree,self.school))

class Course(django.db.models.Model):
  name = django.db.models.CharField(max_length=500)
  school = django.db.models.ForeignKey('Education', related_name='courses')

  def __unicode__(self):
    return unicode('%s'%(self.name))
