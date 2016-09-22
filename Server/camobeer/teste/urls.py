from django.conf.urls import url

from . import views

urlpatterns = [
            url(r'^temp/', views.index, name='index'),
            ]
