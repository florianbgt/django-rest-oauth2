from django.urls import path
from .views import ListPublicTask, DetailPublicTask, ListTeamTask, DetailTeamTask, ListPrivateTask, DetailPrivateTask

urlpatterns = [
    path('public/', ListPublicTask.as_view()),
    path('public/<int:pk>', DetailPublicTask.as_view()),
    path('team/', ListTeamTask.as_view()),
    path('team/<int:pk>', DetailTeamTask.as_view()),
    path('private/', ListPrivateTask.as_view()),
    path('private/<int:pk>', DetailPrivateTask.as_view())
]