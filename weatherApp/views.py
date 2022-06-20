from django.shortcuts import render
import urllib.request
import json
from templates.main import *

# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=2fa60db72acc08df5206871499a30ba9').read()
        list_of_data=json.loads(source)
        data={
            "country_code":str(list_of_data['sys']['country']),
            "coordinate":str(list_of_data['coord']['lon'])+','+str(list_of_data['coord']['lat']),
            "temp":str(list_of_data['main']['temp']),
            "pressure":str(list_of_data['main']['pressure']),
            "humidity":str(list_of_data['main']['humidity']),
            "main":str(list_of_data['weather'][0]['main']),
            "description":str(list_of_data['weather'][0]['description']),
            "icon":str(list_of_data['weather'][0]['icon']),
            "city":str(list_of_data['name']),
            "city_code":list_of_data['id'],

        }

    else:
        data={}
    
    return render(request,"main/index.html",data)
