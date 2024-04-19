from django.urls import path, include
from . import views
urlpatterns = [
  path('', views.login_user),
  path('api/v1/', include('api.urls')),
]