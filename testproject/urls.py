from django.contrib import admin
from django.urls import path, include
from . import views
from members import views as members_views
urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.index),
  path('api/v1/', include('api.urls')),
  # path('members/', include('django.contrib.auth.urls')),
  path('members/', include('members.urls')),
  path('logout/', views.logout_user, name='logout'),
  path('login/', members_views.login_user, name='login'),
]