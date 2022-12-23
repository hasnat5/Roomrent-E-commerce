from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location = 'static/img/')

class Product(models.Model):
    namaProduct = models.CharField(max_length=50)
    keterangan = models.TextField(max_length=200)
    owner = models.CharField(max_length=50)
    gambar = models.ImageField(blank=True,null=True,upload_to='static/img/')

    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.namaProduct)