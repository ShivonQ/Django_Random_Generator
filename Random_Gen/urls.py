from django.conf.urls import url

from . import views
app_name = 'Random_Gen'
urlpatterns =[
    url(r'^', views.base, name='base'),
    url(r'^(?P<enc_level>[0-9]+)', views.treasure_result, name='treasure_result')
]
