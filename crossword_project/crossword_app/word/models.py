from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Question(models.Model):
    question = models.TextField(max_length=150)
    categories = models.ForeignKey(Category)

    def __str__(self):
        return self.question


class Word(models.Model):
    name = models.CharField(max_length=30)
    length = models.IntegerField()
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.name