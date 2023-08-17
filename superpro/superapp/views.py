from django.http import HttpResponse
from django.shortcuts import render
from .models import place, teams


# Create your views here.
def home(request):
    obj=place.objects.all()
    obj1=teams.objects.all()
    return render(request,"index.html",{'result':obj,
                                        'result1':obj1})