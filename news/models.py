from django.db import models

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='news/images/', null=True, blank=True)
    url = models.URLField(null=True)

    # better name in admin site
    def __str__(self):
        return self.headline