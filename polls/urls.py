from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:picture_id>/', views.picture, name='picture'),
    path('<int:user_id>/user/', views.user, name="user"),
    ]
