from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from .models import Header, Card


# Create your views here.
# def index(request):
#     return render(request, 'my_home/index.html')
def index(request): 
    header = Header.objects.first()
    cards = Card.objects.all()
    return render(request, 'my_home/index.html', {'header': header, 'cards': cards})

def contact(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST)
        if form.is_valid():
            body = { 
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }
            try: 
                send_mail(f'New Message From: {body["name"]}', f"Name: {body['name']}\nEmail: {body['email']}\nSubject: {body['subject']}\nMessage: {body['message']}", body['email'], ['willowthedev@protonmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found.')
            return redirect('/success')
    else:
        form = ContactForm()
        return render(request, 'my_home/contact.html', {'form': form})

def success(request):
    return render(request, 'my_home/success.html')