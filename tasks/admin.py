from django.contrib import admin
from .models import PublicTask, TeamTask, PrivateTask

admin.site.register(PublicTask)
admin.site.register(TeamTask)
admin.site.register(PrivateTask)