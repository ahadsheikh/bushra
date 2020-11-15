from djongo import models
from django.utils import timezone


class NewsArticle(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=500, unique=True)
    headline = models.CharField(max_length=500)
    body = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.headline
