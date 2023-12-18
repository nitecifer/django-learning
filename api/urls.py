from django.urls import path
from . import views


urlpatterns = [

    path('', views.getAllStudent),

    path('add/', views.postData),
]