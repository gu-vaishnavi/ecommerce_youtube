from django.db import models

class TodoList(models.Model):
    item = models.CharField(max_length=255)
