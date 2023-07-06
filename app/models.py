from django.db import models


# Create your models here.
class NoteBook(models.Model):

    objects = None
    notes = models.CharField(max_length=200)
    date = models.DateTimeField()
