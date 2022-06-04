from django.shortcuts import render
from main.models import Droid

def get_main(request):
    droids = Droid.objects.all
    context = {
        'droids' : droids,
    }



    return render(request, 'main.html')



# Create your views here.
