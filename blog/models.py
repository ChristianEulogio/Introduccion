from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()

    #para ponerle el nombre del titulo
    def __str__(self):
        return self.title
    