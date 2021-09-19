from django.urls import path
from .views import send_email_view,homeview

urlpatterns = [
    path('home/',homeview,name='home'),
    path('send-mail/',send_email_view,name='send-mail'),
]