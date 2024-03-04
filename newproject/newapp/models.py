from django.db import models



# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class needs(models.Model):
    n_name=models.CharField(max_length=250)
    n_img=models.ImageField(upload_to='pics')
    n_desc=models.TextField()

    def __str__(self):
     return self.n_name

