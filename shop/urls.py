from django.urls import path
from .views import *


urlpatterns = [
    path('', view_home, name='home'),
    path('products/', view_products, name="products"),
    path('add_products/', view_add_product, name="add_products"),
    path('new_arrivals/', view_new_arrivals, name="new_arrivals"),
    path('collections/', view_callections, name="collections"),
    path('about_us/', view_about_us, name="about_us"),
    path('blog/', view_blog, name="blog"),
    path('contact_us/', view_contact_us, name="contact_us"),
]
