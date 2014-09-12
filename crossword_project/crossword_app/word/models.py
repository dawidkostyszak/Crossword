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

    def question_name(self):
        return self.question

    def question_difficulty(self):
        return self.difficulty


class Word(models.Model):
    name = models.CharField(max_length=30)
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.name
