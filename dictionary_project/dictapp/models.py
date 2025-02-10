from django.db import models

# Create your models here.

class Dictionary(models.Model):
    word = models.CharField( max_length=50)
    meaning = models.CharField( max_length=200)
    example = models.CharField( max_length=200)

    def __str__(self):
        return self.word
