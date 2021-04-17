from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    url = models.URLField(blank=False, null=False)

    def __str__(self):
        return self.title