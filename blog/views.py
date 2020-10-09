from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'blog/home.html')


def contact_form(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f"Message from {form.cleaned_data['name']}"
            sender = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            recipients = ["fayga7777777@gmail.com"]
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            return HttpResponse("Success...Your email has been sent")

    return render(request, 'blog/contact.html', {'form':form})


def resume(request):
    return render(request, 'blog/resume.html')
