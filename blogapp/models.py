from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()

    # New
    def __str__(self):
        return self.title

    

