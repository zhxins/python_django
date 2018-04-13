from django.conf.urls import url
# from myDjango.views import index
from . import views

# 每个url后面需要加"/"
urlpatterns = [
    url(r'^index/', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^toAdd/(?P<article_id>[0-9]+)$', views.article_addgage, name='toAdd'),
    url(r'^add/', views.article_add, name='add'),



]