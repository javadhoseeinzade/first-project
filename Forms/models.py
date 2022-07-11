from django.db import models

class darmangar(models.Model):
    choics = [
        ("طلاق","طلاق"),
        ("فرزند","فرزند"),
        ("خانواده","خانواده"),
    ]
    keyword = models.CharField(max_length=20, choices=choics, default=1)
    fname = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, unique=True )
    lname = models.CharField(max_length=100)
    description = models.TextField()
    pic = models.ImageField(upload_to="darmanger-image")


    def __str__(self):
        return self.fname + " " + self.lname 

class info(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.EmailField()
    slug = models.CharField(max_length=20, unique=True, null=True)

    talk_about = models.TextField()
    rel_info = models.ForeignKey(darmangar, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.fname + " " + self.lname

class UploadFile(models.Model):
    upl = models.FileField(upload_to="upload-file")



class darmanjo_form(models.Model):
    talk_about = models.TextField(null=True, blank=True)
    information = models.ForeignKey(info, on_delete=models.CASCADE,null=True)
    rel_info = models.ForeignKey(darmangar, on_delete=models.CASCADE,null=True, blank=True)
    #picture = models.forignkey(darmangar, models/CASCADE)
    def __str__(self):
        return self.talk_about

class Choice_Model(models.Model):
    choics = [
        ("طلاق","طلاق"),
        ("فرزند","فرزند"),
        ("خانواده","خانواده"),
    ]
    keyword = models.CharField(max_length=20, choices=choics, default=1)
    information = models.ForeignKey(info, on_delete=models.CASCADE,null=True)
    sessions = models.CharField(max_length=200)
