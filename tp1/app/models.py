from django.db import models

# Create your models here.
class Cours(models.Model):
    title = models.CharField(max_length=60)
    former = models.CharField(max_length=60)
    hours = models.IntegerField()
    first_lesson = models.DateTimeField()
    note = models.FloatField(default=10.0)
    numberOfNote = models.IntegerField(default=0)


