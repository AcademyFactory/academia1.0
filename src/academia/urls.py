from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    #url(r'^saida/', views.saida, name='saida')
]