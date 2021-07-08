from rest_framework import serializers
from .models import PublicTask, TeamTask, PrivateTask

class PublicTaskSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = PublicTask
        fields = '__all__'


class TeamTaskSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = TeamTask
        fields = '__all__'


class PrivateTaskSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = PrivateTask
        fields = '__all__'