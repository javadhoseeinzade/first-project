from django.db import models


class info(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    codemeli = models.IntegerField()

class UploadFile(models.Model):
    upl = models.FileField(upload_to="upload-file")


