from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about', views.about, name='about'),
	path('terms', views.terms, name='terms'),
	path('privacy', views.privacy, name='privacy'),
	
]
