
from django.urls import include

from django.contrib import admin
from django.urls import path
from pages.views import Home, Login, Register, Logout
from django.contrib.auth import views as auth_views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('dash/', include('pages.urls'), name='home'),

    # path('login',auth_views.LoginView.as_view(template_name='login.html'), name='login_view'),

    path('home', Home, name='home'),
    path('logout', Logout, name='logout'),
    path('login',Login, name='login'),
    path('register', Register, name='register'),
]

urlpatterns += staticfiles_urlpatterns()
