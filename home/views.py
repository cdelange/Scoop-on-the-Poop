from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import BathroomBreak, Dog, Person
from datetime import datetime


@csrf_exempt
def buttons(request):
    if request.method == 'POST':
        dog = request.POST.get('Dog')
        typeOfBreak = request.POST.get('typeOfBreak')
        walker = request.POST.get('walker')

        if not Dog.objects.filter(name=dog).exists():
            dogEntry = Dog(name=dog)
            dogEntry.save()
        else:
            dogEntry = Dog.objects.filter(name=dog).first()

        if walker == 1:
            person = "Casey"
        else:
            person = "Allie"

        if not Person.objects.filter(name=person).exists():
            personEntry = Person(name=person)
            personEntry.save()
        else:
            personEntry = Person.objects.filter(name=person).first()

        bathroomBreakEntry = BathroomBreak(dog=dogEntry, type_of_bathroom=typeOfBreak, person=personEntry)
        bathroomBreakEntry.save()
        return HttpResponse(person)

    else:
        return HttpResponse('Not a post request')


@csrf_exempt
def delete_button(request):
    most_recent = BathroomBreak.objects.last().delete()
    return HttpResponse(most_recent)


def home(request):
    context = {
        'totalpoops': BathroomBreak.objects.filter(type_of_bathroom='Poop').count(),
        'totalpees': BathroomBreak.objects.filter(type_of_bathroom='Pee').count(),
        'zuripoops': BathroomBreak.objects.filter(dog__name='Zuri', type_of_bathroom='Poop'),
        'zuripees': BathroomBreak.objects.filter(dog__name='Zuri', type_of_bathroom='Pee'),
        'novapoops': BathroomBreak.objects.filter(dog__name='Nova', type_of_bathroom='Poop'),
        'novapees': BathroomBreak.objects.filter(dog__name='Nova', type_of_bathroom='Pee'),
        'recentnovapee': BathroomBreak.objects.filter(dog__name='Nova', type_of_bathroom='Pee').last(),
        'recentnovapoop': BathroomBreak.objects.filter(dog__name='Nova', type_of_bathroom='Poop').last(),
        'recentzuripoop': BathroomBreak.objects.filter(dog__name='Zuri', type_of_bathroom='Poop').last(),
        'recentzuripee': BathroomBreak.objects.filter(dog__name='Zuri', type_of_bathroom='Pee').last(),
        'now': datetime.now(),
    }
    response = render(request, 'home/home.html', context, {'title': 'Home'})
    return response
