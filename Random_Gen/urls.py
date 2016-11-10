from django.conf.urls import url

from . import views
app_name = 'Random_Gen'
urlpatterns =[
    url(r'^$', views.base, name='base'),
    url(r'^treasure', views.treasure_result, name='treasure_result')
]
