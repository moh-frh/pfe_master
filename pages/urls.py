
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
# from users import views as user_views


from pages.views import Home, Login, Register

urlpatterns = [
    path('', views.Home),
]

urlpatterns += staticfiles_urlpatterns()
