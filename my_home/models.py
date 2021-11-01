from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.URLField()
    link = models.URLField()
    source = models.URLField(default="https://willowthe.dev")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

