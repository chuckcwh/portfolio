from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from website.forms import EmailForm
from website.models import Email


def home(request):
    return render_to_response("home.html")

def about_me(request):
    return render_to_response("about_me.html")

def projects(request):
    data = {'projects': Project.objects.order_by('?')[:1]}

    return render_to_response(request, "projects.html", data)

def comments(request):
    return render_to_response("comments.html")

def email(request):
    data = {"email_form": EmailForm()}
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            new_mailer = Email(subject = form.cleaned_data['subject'], message= form.cleaned_data['message'],
                               sender= form.cleaned_data['sender'], receiver= "chuckcwh@gmail.com")
            send_mail(subject= new_mailer.subject, message= new_mailer.message,
                      from_email= new_mailer.sender, recipient_list= ["chuckcwh@gmail.com"], fail_silently=False)
        else:
            HttpResponse("wrong email")
    return render(request, "email.html", data)