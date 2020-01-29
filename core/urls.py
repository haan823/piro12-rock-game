from django.urls import path

from . import views
from .views import play_user, rps_list

urlpatterns =[
    path('list/', rps_list, name='rps_list'),
    path('play_user/<int:pk>', play_user, name='play-user')
]