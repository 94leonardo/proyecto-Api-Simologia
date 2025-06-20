from django.db import models

# Create your models here.

class Feature(models.Models):
    external_id = models.CharField(max_length=100, unique=True)
    magnitude = models.DecimalField(max_digits=4, decimal_places=1)
    place = models.CharField(max_length=255)
    time = models.DateField()
    tsunami = models.BooleanField()
    mag_type = models.CharField(max_length=10)
    title = models.TextField()
    longitude = models.DecimalField(max_digits=9,decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    url = models.URLField()

    def __str__(self):
        return f"{self.title} ({self.magnitude})"

class Comment(models.Model):
    Feature = models.ForeignKey(Feature, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.Feature.id} : {self.body[:30]}..."
    