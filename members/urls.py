from django.urls import path, include
from . import views
urlpatterns = [
  path('login/', views.login_user, name='login'),
  path('register/', views.register_user, name='register'),
  path('api/v1/', include('api.urls')),
]