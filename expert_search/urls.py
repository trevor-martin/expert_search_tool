from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='expert_search_home'),
    path('<int:pk>/', views.expert_detail, name='expert_detail'),
]
