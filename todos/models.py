from django.db import models
from django.utils import timezone


# Create your models here.

class TodosManager(models.Manager):
    def add(self, title, description):
        todo = self.create(title= title, description=description, publish_date=timezone.now())
        return todo

class Todos(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(default=0, db_comment="0 = todo, 1 = progress, 2 = done")
    publish_date = models.DateTimeField()

    objects = TodosManager()

    def __str__(self):
        return self.id