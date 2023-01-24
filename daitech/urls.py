from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("companyinfo/", views.companyinfo, name="companyinfo"),
    path("vision/", views.vision, name="vision"),
    path("mission/", views.mission, name="mission"),
    path("services/", views.services, name="services"),
    path("products/", views.products, name="products"),
    path("product_details/<id>", views.productdetails, name="product_details"),
    path("sales-representatives/", views.salesrep, name="salesrep"),
    path("events/", views.events, name="events"),
    path("post_details/<id>", views.post_details, name="post_details"),   
    path("contact/", views.contact, name="contact"),
    path("search/", views.search, name="search"),
    path("newsletter/", views.newsletter, name="newsletter"),
    path("validate/", views.validate_email, name="validate_email"),
]
