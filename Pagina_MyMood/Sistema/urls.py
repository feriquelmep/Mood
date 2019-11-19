from django.conf.urls import url
from django.urls import path
from . import views

#Urls para las páginas que existen
urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^formulario/$',views.registroPersona,name="formulario"),
    url(r'^login/$',views.ingreso, name="login"),
    url(r'^olvido/$',views.olvidocontraseña, name="olvido"),
    url(r'^restablecer/$',views.restablecer, name="restablecer"),
    url(r'^registroAdmin/$',views.registroAdmin, name="registroAdmin"),
    url(r'^salir/$',views.salir,name="logout"),
]