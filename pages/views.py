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

    obj={}


    for day in forcast:
        i,j=forcast[day]

        s=i-j

        if(0<=s<5):
            w="sunny.png"
        elif(5<=s<10):
            w="cloud.png"
        else:
            w="drop.png"
        
        obj[day]=w    


    return render(request,'home.html',{"obj":obj})






# def home(request):
    
#     try:
#         obj=requests.get("http://ipinfo.io")
#         g=True
#     except Exception as e:
#         g=False
#         status="no"
#         obj={}

#     # obj='{"bla":2,"status_code":200}'
#     if(g and obj.status_code == 200 ):
#         obj=json.loads(obj.text)
#         status="yes"

#     else:
#         status="no"

#     return render(request,'home.html',{"obj":obj,"status":status})


# def search(request):

#     if (request.method=="POST"):

#         form=Form(request.POST)
#         print(form)

#         if(form.is_valid):
#             ip=form.cleaned_data['ip']

#             try:
#                 obj=requests.get("http://ipinfo.io/"+ip)
#                 g=True
#             except Exception as e:
#                 g=False
#                 status="no"
#                 obj={}

#             if(g and obj.status_code == 200):
#                 obj=json.loads(obj.text)
#                 status="yes"
#             else:
#                 status="no"
  

#             return render(request,'home.html',{"obj":obj,"status":status})


#     else:
#         form=Form()

#     return render(request,'search.html',{"form":form})

