from django.urls import path
from Api.views import *
urlpatterns = [
    path('',EndpointView,name='endpoints'),
    path('post/',Bloglistview,name='posts'),
    path('post/<uuid:pk>/',BlogDetailview,name='posts'),
    
]
