from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):

    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    text = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    price = models.FloatField()

    def post_detail(self):
        return reverse('core:fast', args = [self.slug])

    def __str__(self):
        return self.title