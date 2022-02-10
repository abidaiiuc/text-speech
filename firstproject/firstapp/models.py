from django.db import models

class book(models.Model):
    book_id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=2000)
    author=models.CharField(max_length=2000)
    tags=models.CharField(max_length=100)
    # image=models.ImageField(upload_to='document')
    book=models.FileField(upload_to='document')

    def __str__(self):
        return self.name

# Create your models here.
