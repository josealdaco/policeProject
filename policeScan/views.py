from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
import json
import requests
import string

# Create your views here.


def refreshHome(request):
    #  This will help determine what city we will be ranking
    pass


def home(request):
    #  zipCode = 95110
    police_Departments = {"sanjose": 5}
    try:
        if request.GET['cityResponse'] is True or request.GET['cityResponse'] == "true":
            city = request.GET['City'].translate({ord(c): None for c in string.whitespace})
            print("City Response", city)
            #request = request.GET['Comment']
            #print("This is the city", city)
        #    obj = Comments.objects.create(comment=comment, city=city)
            #secondObject = obj
            #obj.save()
            #print("This is the comment being saved", secondObject.comment)
            return JsonResponse({"city": city.upper(), "rate": police_Departments[city.lower()]})
    except Exception:
        print("Did not go trough")
        pass
    return render(request, 'home.html', {"rate": police_Departments['sanjose'], 'city': 'sanjose'.upper()})
