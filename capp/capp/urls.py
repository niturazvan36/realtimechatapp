
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('chat.urls')),

    path('login',views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',views.LogoutView.as_view(template_name='logout.html'),name='logout')
]
