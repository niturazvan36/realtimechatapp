
from django.urls import path
from . import views
from .views import Room, ChartData
from django.contrib.auth.views import LogoutView
from django.conf import settings
urlpatterns = [
    path('', views.home,name='home'),
    path('register',views.register, name='register'),
    path('<str:room_name>/', Room.as_view(), name='room'),
    path('api/data', views.get_data, name='api-data'),
    path('api/chart/data', ChartData.as_view()),
    path('logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]
