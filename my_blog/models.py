from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    status_choices = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=status_choices, default='draft')
    view_count = models.IntegerField(default=0)

    tags = TaggableManager()

    class Meta: 
        ordering = ('-publish',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('my_blog:detail_view', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def increment_view_count(self):
        self.view_count += 1
        self.save()

    def get_view_count(self):
        return f'{self.view_count:,}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=256)
    email = models.EmailField(default=None)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)