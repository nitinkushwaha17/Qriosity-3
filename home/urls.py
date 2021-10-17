from django.urls import path, include
from . import views

app_name = 'home'


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('rules/', views.rules, name="rules"),
    path('abadakadabra/qualifiedlist/', views.page, name="page"),
    path('khankimaagi/', views.email_users, name="player")
]
