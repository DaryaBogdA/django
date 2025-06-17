from django.urls import path
from . import views
urlpatterns = [
       path('', views.home, name='home'),
       path('kids_dance', views.kids_dance, name='kids_dance'),
       path('all_styles', views.all_styles, name='all_styles'),
       path('rdc', views.rdc, name='rdc'),
       path('hiphop_7_9', views.hiphop_7_9, name='hiphop_7_9'),
       path('junior_team', views.junior_team, name='junior_team'),
       path('adult_team', views.adult_team, name='adult_team'),
       path('registration/', views.registration, name='registration'),
       path('rules/', views.rules, name='rules'),
]
