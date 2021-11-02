from django.db import models

# Create your models here.
class Header(models.Model): 
    title = models.CharField(max_length=256)
    subtitle = models.TextField()

class Card(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.URLField()
    link = models.URLField()
    source = models.URLField(default="https://willowthe.dev")
    date = models.DateTimeField(auto_now_add=True)
    placement = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta: 
        ordering = ('placement',)

