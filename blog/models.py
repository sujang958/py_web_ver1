from django.db import models

class Post(models.Model):
    title = models.CharField(blank=False, null=False, max_length=50)
    image = models.ImageField(blank=True)
    description = models.CharField(blank=False, null=False, max_length=350, help_text="Description!")

    def __str__(self):
        return self.title