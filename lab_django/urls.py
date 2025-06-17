from django.urls import path, re_path
from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^products/$', views.products),
    re_path(r'^products/(?P<productid>\d+)/$', views.products),
    re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/$', views.users),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
]