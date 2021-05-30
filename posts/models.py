from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from . import answer
from . import comments
from . import like

class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    answer = models.ForeignKey(Answer, on_delete=model.CASCADE)
    like = models.ForeignKey(Like)
    # comment

    def __str__(self):
        return self.question


    



