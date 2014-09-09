from django.db import models


class Difficulty(models.Model):
    difficulty = models.IntegerField()

    def __str__(self):
        return str(self.difficulty)


class Question(models.Model):
    question = models.TextField(max_length=150)
    difficulty = models.ForeignKey(Difficulty)

    def __str__(self):
        return self.question


class Word(models.Model):
    name = models.CharField(max_length=30)
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.name
