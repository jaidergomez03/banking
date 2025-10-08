from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Country
from .forms import CountryForm

from django .http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is my first view")

#def countries(request):
#    return HttpResponse("This is my countries")


#def depart(request):
#    return HttpResponse("This is my departments")

#def cities(request):
#   return HttpResponse("This is my cities")


def country_list(request):
    countries = Country.objects.all().order_by('name')
    return render(request, "authentication_app/country_list.html", {"countries": countries})

# authentication_app/views.py

# ... (cuerpo de la función country_edit)

def country_edit(request, pk):
    country = get_object_or_404(Country, pk=pk)
    
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            messages.success(request, 'País actualizado correctamente.')
            return redirect('country_list')
        else:
            countries = Country.objects.all().order_by('name') 
            return render(request, "authentication_app/country_list.html", {"countries": countries, "form": form})  
    else:
        form = CountryForm(instance=country)     
        countries = Country.objects.all().order_by('name')        
        return render(request, "authentication_app/country_list.html", {"countries": countries, "form": form})
