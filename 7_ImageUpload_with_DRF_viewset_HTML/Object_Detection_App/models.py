from django.db import models

# Create your models here.
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
