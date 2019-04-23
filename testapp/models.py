from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")
    photo = models.FileField(upload_to='untitled/uploads/', default="")
    def __str__(self):
        return self.name