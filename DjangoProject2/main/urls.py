
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contacts', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
]
