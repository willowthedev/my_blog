from django.shortcuts import render
from .forms import ColorForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            form.change_color()
    else:
        form = ColorForm()

    return render(request, 'my_lifx/index.html', {'form': form})