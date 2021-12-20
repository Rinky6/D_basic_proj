from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


def index(request):
    return HttpResponse("Hello...")


def index1(request):
    response = """<p> hi maam what are you doing</p>"""
    return HttpResponse(response)


def index2(request, p_no):
    response = """<h1> You are in """ + p_no +"""</h1>"""
    return HttpResponse(response)

def index3(request):
    return render(request, 'myapp/index.html')

def index4(request,number):
    template_name ='myapp/main.html'
    context = {'number': number}
    return render(request,template_name,context)

def index5(request):
    name = ['Rinky', 'Pinky','Ram']
    id = [3,6,7]
    sal = [25000,85000,42000]
    info = zip(name,id,sal)
    context= {'infos':info}
    return render(request,'myapp/info.html', context)


class Fst_Cls(View):
    def get(self,request):
        return HttpResponse("My first proj with class")



class Scd_Cls(View):
    def get(self,request,p_no):
        context = {'p_no': p_no}
        return render(request,'myapp/block.html', context)


