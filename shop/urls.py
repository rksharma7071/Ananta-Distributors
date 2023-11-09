from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('print/<int:user_id>/', generate_user_profile_pdf, name='profile_print'),
]
