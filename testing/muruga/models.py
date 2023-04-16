from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class User_credential(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('data_detail', kwargs={'pk': self.pk})

