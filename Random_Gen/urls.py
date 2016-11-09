from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^', views.base, name='base'),
    url(r'^(<enc_level>[0-9]+)/$', views.treasure_result, name='treasure_result')
]
