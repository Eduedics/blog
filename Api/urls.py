from django.urls import path
from Api.views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('',EndpointView,name='endpoints'),
    path('post/',Bloglistview,name='posts'),
    path('post/<uuid:pk>/',BlogDetailview,name='posts'),
    path('api/token/', MyTokenObtainPairSerializer.as_view(), name='token_obtain_pair'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
