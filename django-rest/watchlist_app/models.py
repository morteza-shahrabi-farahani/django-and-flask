from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class StreamPlatform(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    website = models.URLField(max_length=255)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=255)
    storyline = models.TextField()
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    

class Review(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField()
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="review")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.rating) + " - " + self.watchlist.title