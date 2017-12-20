from django.db import models



class Photo(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/photos/')
    description = models.TextField(blank=False, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    


class PhotoCategory(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/categories/')
    active = models.BooleanField(default=True)
    photos = models.ManyToManyField(Photo)
    featured = models.BooleanField(default=False) 
    
    def __str__(self):
        return self.name

    def active_photo_count(self):
    	return self.photos.filter(show=True).count()
