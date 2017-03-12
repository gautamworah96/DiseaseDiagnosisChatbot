__author__ = 'ghw'


from django.conf.urls import url
from django.contrib import admin
from Main import views
app_name ='Main'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    ]
