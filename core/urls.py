from django.urls import path
from .views import home, fast, search
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('post_detail/<slug:slug>/', views.fast, name='post_detail'),
    path('search/', search, name='search'),
]