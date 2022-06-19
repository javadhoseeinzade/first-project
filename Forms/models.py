from django.db import models


class info(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField()
    slug = models.CharField(max_length=20, unique=True, null=True)
    
    def __str__(self):
        return self.fname + " " + self.lname
class UploadFile(models.Model):
    upl = models.FileField(upload_to="upload-file")


