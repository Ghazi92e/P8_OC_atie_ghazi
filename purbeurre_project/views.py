
from django.shortcuts import render
from products.forms import NameForm

class Home():
    def mentionslegales(request):
        form = NameForm(request.GET)
        return render(request, 'mentionslegales.html', {'form': form})