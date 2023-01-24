from django.contrib import admin
from .models import Post, Comment, ProductCategory, Salesrep, Product, SubscribedUsers
# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_display = ("title", "date", "pic1", "pic2", "pic3")    

class AdminComment(admin.ModelAdmin):
    list_display = ("name", "date", "comment")

class AdminSalesrep(admin.ModelAdmin):
    list_display = ("name", "email", "region")

class AdminProductCategory(admin.ModelAdmin):
    list_display = ("name",)  

class AdminProduct(admin.ModelAdmin):
    list_display = ("category","title","composition", "indication", "dosage", "pic1")  

class AdminSubscribedUsers(admin.ModelAdmin):
    list_display = ("email",)          


admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)
admin.site.register(Salesrep, AdminSalesrep)
admin.site.register(ProductCategory, AdminProductCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(SubscribedUsers, AdminSubscribedUsers)