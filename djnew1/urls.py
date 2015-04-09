from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework import routers
from blog.views import PostPubViewSet,PostPrivViewSet, TagViewSet, CategoryViewSet, UserViewSet, CommentViewSet, BlogImageViewSet
from resume.views import ExperienceViewSet,SkillViewSet, SkillLevelViewSet, ExperienceCategoryViewSet, EducationViewSet, CourseViewSet
from projects.views import ProjectViewSet,ProjectTagViewSet, LinkViewSet, ScreenshotViewSet
router = routers.DefaultRouter()
router.register(r'blog/posts', PostPubViewSet,base_name='post')
router.register(r'blog/posts_admin', PostPrivViewSet,base_name='post-priv')
router.register(r'blog/tags',TagViewSet,base_name='tag')
router.register(r'blog/categories',CategoryViewSet)
router.register(r'blog/users',UserViewSet)
router.register(r'blog/comments',CommentViewSet)
router.register(r'blog/image',BlogImageViewSet)
router.register(r'resume/experience', ExperienceViewSet)
router.register(r'resume/skills', SkillViewSet)
router.register(r'resume/skill_levels', SkillLevelViewSet)
router.register(r'resume/exp_cats', ExperienceCategoryViewSet)
router.register(r'resume/education', EducationViewSet)
router.register(r'resume/courses', CourseViewSet)
router.register(r'projects/projects', ProjectViewSet)
router.register(r'projects/tags', ProjectTagViewSet)
router.register(r'projects/links', LinkViewSet)
router.register(r'projects/screens', ScreenshotViewSet)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djnew1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'api/',include(router.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

