from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'index.html')


def mail_team(request):
    email = request.POST.get('email')
    name = request.POST.get('name')
    message = request.POST.get('message')

    send_mail(name, message, email, ['bmwasaru@gmail.com', 'ruthkaveke@gmail.com', 'joelmwas199@gmail.com'],
              fail_silently=False)

    return render(request, 'thank_you.html')
