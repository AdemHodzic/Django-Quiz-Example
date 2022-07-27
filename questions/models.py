
from django.db import models

class Question(models.Model):
    question = models.TextField(
        null=False,
        blank=False,
    )

class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        related_name="answers",
        on_delete=models.CASCADE,
    )

    text = models.CharField(
        max_length=150,
    )
    correct = models.BooleanField(default=False)
