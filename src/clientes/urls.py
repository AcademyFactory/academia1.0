from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^entrada/', views.entrada, name='entrada'),
    url(r'^saida/', views.saida, name='saida')
]