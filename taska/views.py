from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    template=loader.get_template("login.html")
    return HttpResponse(template.render())
def index1(request):
    template=loader.get_template("task.html")
    return HttpResponse(template.render({},request))
def index2(request):
    template=loader.get_template("signup.html")
    return HttpResponse(template.render({},request))