from django.shortcuts import render
from .models import Card

# Create your views here.
# def index(request):
#     return render(request, 'my_home/index.html')
def index(request): 
    cards = Card.objects.all()
    return render(request, 'my_home/index.html', {'cards': cards})