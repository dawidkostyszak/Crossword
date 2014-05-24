from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=30)
    question = models.TextField(max_length=150)
    category = models.CharField(max_length=20)