from django.urls import path
from Api.views import *
urlpatterns = [
    path('post/',Bloglistview,name='posts'),
    path('post/<str:pk>/',BlogDetailview,name='posts')
]
