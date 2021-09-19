from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


def homeview(request):
    template_name='home.html'
    context={}
    return render(request,template_name,context)


def send_email_view(request):
    print('in send_email_view')

    send_mail(
        'subject of mail',
        'message in the mail,hello im from django',
        'nik7testing@gmail.com',
        ['nik7testing@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse('see mailbox')
