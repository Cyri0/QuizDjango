from django.db import models

class BasicQuiz(models.Model):
    question = models.CharField(max_length=200)
    good = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)