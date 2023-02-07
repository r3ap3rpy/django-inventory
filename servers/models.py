from django.db import models
from uuid import uuid4
# Create your models here.
class Server(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null = True, blank = True)
    cpu = models.IntegerField()
    ram = models.IntegerField()
    storage = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid4, unique= True, editable= False, primary_key= True)
    tags = models.ManyToManyField('Tag', blank = True,)

    def __str__(self):
        return  f"{self.name}(cpu = {self.cpu}, ram = {self.ram} GB, storage = {self.storage})"

class Tag(models.Model):
    CHOICES = (
        ('prod','Production'),
        ('test','Testing'),
        ('dev','Development')
    )
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid4, unique= True, editable= False, primary_key= True)

    def __str__(self):
        return self.name