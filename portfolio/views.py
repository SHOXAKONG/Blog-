from django.contrib import messages
from django.shortcuts import render, redirect
from portfolio.forms import ContactForm


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/home.html')


def skills(request):
    return render(request, 'home/home.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your contact was sent successfully!")
        else:
            messages.error(request, "Something went wrong. Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {"form": form})  # Ensure correct template name
