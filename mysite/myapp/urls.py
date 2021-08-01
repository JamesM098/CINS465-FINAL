from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
  path('', views.index),
  path('log-in-page/', views.login),
  path('welcome', views.welcome),
  path('hikes/', views.hikes, name = 'hikes_url'),
  path('hikes/all-hikes/', views.all_hikes, name = "all-hikes"),
  path('live-chat/', views.live_chat),
  path('about/', views.about),
  path('help/', views.help),
  path('admin/', admin.site.urls),
  path('show_hike/<hike_id>', views.show_hikes, name = "show-hike"),
  path('add_hike', views.add_hike, name = "add-hike"),
  path('add_location', views.add_location, name = "add-location"),



]