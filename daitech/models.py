from distutils.command.upload import upload
from turtle import title
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length =100)
    pic1 = models.ImageField(upload_to ="images/")
    pic2 = models.ImageField(upload_to ="images/")
    pic3 = models.ImageField(upload_to ="images/")
    body = models.TextField()
    date =models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= "comments")
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.comment        
    
class Salesrep(models.Model):
    pic = models.ImageField(upload_to= "images/")
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    

class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)  
    
    class Meta:
        verbose_name_plural = 'Productcategories'  

    def __str__(self):
        return self.name 

       
class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="products")
    title = models.CharField(max_length=50)
    composition = models.TextField(max_length=500)
    indication = models.TextField(max_length=500)
    dosage = models.TextField(max_length=500)
    pic1 = models.ImageField(upload_to ="images/")
    pic2 = models.ImageField(upload_to ="images/")
    pic3 = models.ImageField(upload_to ="images/")

    class Meta:
        ordering = ['id']  

    def __str__(self):
        return self.title
    

class SubscribedUsers(models.Model):
    email = models.CharField(unique=True, max_length=50)

    class Meta:
        verbose_name_plural = 'SubscribedUsers'