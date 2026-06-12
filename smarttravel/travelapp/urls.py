from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('hotels/', views.hotels, name='hotels'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('popularplaces/', views.popularplaces, name='popularplaces'),
    path('directions/', views.directions, name='directions'),
    path('weather/', views.weather, name='weather'),
    path('atms/', views.atms, name='atms'),
    path('hospitals/', views.hospitals, name='hospitals'),
    path('policestations/', views.policestations, name='policestations'),
    path('travel_chatbot/', views.travel_chatbot, name='travel_chatbot'),
    path('budget/', views.budget, name='budget'),
]
