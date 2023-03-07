from django.urls import re_path
from . import views
from django.conf import settings

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^about/$', views.about_me, name='about'),
    re_path(r'^portfolio/$', views.portfolio, name='portfolio'),
    
]
