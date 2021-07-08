from rest_framework import generics
from .models import PublicTask, TeamTask, PrivateTask
from .serializers import PublicTaskSerializer, TeamTaskSerializer, PrivateTaskSerializer


class ListPublicTask(generics.ListCreateAPIView):
    queryset = PublicTask.objects.all()
    serializer_class = PublicTaskSerializer


class DetailPublicTask(generics.RetrieveDestroyAPIView):
    queryset = PublicTask.objects.all()
    serializer_class = PublicTaskSerializer


class ListTeamTask(generics.ListCreateAPIView):
    queryset = TeamTask.objects.all()
    serializer_class = TeamTaskSerializer


class DetailTeamTask(generics.RetrieveDestroyAPIView):
    queryset = TeamTask.objects.all()
    serializer_class = TeamTaskSerializer


class ListPrivateTask(generics.ListCreateAPIView):
    queryset = PrivateTask.objects.all()
    serializer_class = PrivateTaskSerializer


class DetailPrivateTask(generics.RetrieveDestroyAPIView):
    queryset = PrivateTask.objects.all()
    serializer_class = PrivateTaskSerializer