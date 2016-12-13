from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'Random_Gen'
urlpatterns =[
    url(r'^$', views.base, name='home'),
    url(r'treasure_gen',views.treasure_gen, name='treasure_gen' ),
    url(r'^treasure', views.treasure_result, name='treasure_result')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
