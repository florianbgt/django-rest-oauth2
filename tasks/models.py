from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class PublicTask(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    createAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class TeamTask(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    createAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class PrivateTask(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    createAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)