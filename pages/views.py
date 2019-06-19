from django.shortcuts import render
import requests
import json
from .forms import Form

# Create your views here.

forcast={
    "mon":[71,61],"tue":[70,68],"wed":[73,66],"thu":[83,80],"fri":[77,70],"sat":[78,64],"sun":[77,62],

}



def home(request):

    rep=requests.get("https://api.openweathermap.org/data/2.5/forecast?q=Kochi,in&appid="+api)
    repjson=json.loads(rep.text)
    repjson=repjson['list']
    day=['mon','tue','wed','thu','fri','sat','sun']

    obj={}
    
    for k,i in enumerate(repjson,day):
        j=i['main']
        h=j['temp_max']
        l=j['temp_min']
        
        s=h-l

        if(0<=s<5):
            w="sunny.png"
        elif(5<=s<10):
            w="cloud.png"
        else:
            w="drop.png"
        
        obj[k]=w    


    return render(request,'home.html',{"obj":obj})

##### Hard coded ##############

#     for day in forcast:
#         i,j=forcast[day]

#         s=i-j

#         if(0<=s<5):
#             w="sunny.png"
#         elif(5<=s<10):
#             w="cloud.png"
#         else:
#             w="drop.png"
        
#         obj[day]=w    


#     return render(request,'home.html',{"obj":obj})




