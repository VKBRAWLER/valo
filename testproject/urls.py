from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.index),
  path('api/v1/', include('api.urls')),
  # path('members/', include('django.contrib.auth.urls')),
  path('members/', include('members.urls')),
]