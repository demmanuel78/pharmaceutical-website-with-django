from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator
from .forms import CForm
from django.http import JsonResponse
import re
from django.conf import settings


from .models import Post, Comment, ProductCategory, Salesrep, Product, SubscribedUsers

from smtplib import SMTP_SSL, SMTP, SMTPAuthenticationError
from ssl import create_default_context


# Create your views here.

def index(request):
    return render(request, "daitech/index.html")

def companyinfo(request):
    return render(request, "daitech/companyinfo.html")    

def vision(request):
    return render(request, "daitech/vision.html")   

def mission(request):
    return render(request, "daitech/mission.html")    

def services(request):
    return render(request, "daitech/services.html")   

def products(request):
    products = Product.objects.all().order_by("title")
    productcategories = ProductCategory.objects.all().order_by("name")

    data = {
        "productcategories": productcategories,
        "products": products
    }
    return render(request, "daitech/products.html", data)        

def productdetails(request, id):
    product = get_object_or_404(Product, id=id)
    productcategories = ProductCategory.objects.all().order_by("id")

    data = {
        "product": product,
        "productcategories": productcategories
    }
    return render(request, "daitech/product_details.html", data)  

def salesrep(request):
    salesreps = Salesrep.objects.all().order_by("id")

    data = {
        "salesreps": salesreps,
    }
    return render(request, "daitech/salesrep.html", data)    

def events(request):
    posts = Post.objects.all().order_by("-id")
    latestposts = Post.objects.all().order_by("-id")[:5]

    p = Paginator(posts, 2)

    p_num = request.GET.get("p")

    try:
        page = p.page(p_num)
    except:
        page = p.page(1)
    finally:
        num_of_pages = p.num_pages    


    data = {
        "posts": page,
        "latestposts": latestposts,
        "num_of_pages": range(1, num_of_pages+1)
    }
    return render(request, "daitech/events.html", data)   

def post_details(request,id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=id)
    latestposts = Post.objects.all().order_by("-id")[:5]
     
    form = CForm() 
    if request.method == "POST":
        form = CForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post_id = post.id
            comment.save()
            messages.success(request, "Comment Uploaded Successfully")

    data = {
        "post": post,
        "comments": comments,
        "latestposts": latestposts 
    }      
    return render(request, "daitech/post_details.html", data)

def contact(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        message = "From " + request.POST.get("email") + " : " + request.POST.get("name") + " : " + request.POST.get("message")
        sender = request.POST.get("email")
        send_mail(subject,
        message,
        sender,
        ["demmanuel78@yahoo.com", "oladele.odebunmi@daitechpharma.com"],
        fail_silently=False)
        messages.success(request, "Message sent successfully")
    return render(request, "daitech/contact.html")       

def search(request):
    if request.method == "GET":
        search = request.GET.get("searchvalue")
        posts = Post.objects.filter(title__icontains=search).order_by("title")
       
    data = {
        "posts": posts,
        "searchvalue": search
    }      
    return render(request, "daitech/events.html", data) 


def validate_email(request): 
    email = request.POST.get("email", None)   
    if email is None:
        res = JsonResponse({'msg': 'Email is required.'})
    elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        res = JsonResponse({'msg': 'Invalid Email Address'})
    elif SubscribedUsers.objects.filter(email = email).first():
        res = JsonResponse({'msg': 'Email Address already exists'})
    else:
        res = JsonResponse({'msg': ''})
    return res    
    

def newsletter(request):
    if request.method == "POST":
        post_data = request.POST.copy()
        email = post_data.get("email", None)
        subscribedUsers = SubscribedUsers()
        subscribedUsers.email = email
        subscribedUsers.save()
        # send a confirmation mail
        subject = "NewsLetter Subscription"
        message = "Hello " + email +  ", Thanks for subscribing to our newsletter. You will get notification of latest articles posted on our website. Please do not reply on this email."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
        res = JsonResponse({'msg': 'Thanks. Subscribed Successfully!'})
        return res
    return render(request, "daitech/index.html")






