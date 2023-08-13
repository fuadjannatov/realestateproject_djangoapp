# Create your views here.
from django.shortcuts import render
from . predict import getPrediction

# Create your views here.
def home(request):
    return render(request, 'home.html')


def result(request):
    floor = int(request.GET['Floor'])
    highestfloor = int(request.GET['HighestFloor'])
    area = int(request.GET['Area'])
    rooms = int(request.GET['Rooms'])
    renovation = int(request.GET['Renovation'])
    document = int(request.GET['Document'])
    subway = (request.GET['Subway'])

    result = getPrediction(floor, highestfloor, area, rooms, renovation, document, subway)
    return render(request, 'result.html', {'result': result})