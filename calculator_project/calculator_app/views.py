from django.shortcuts import render, redirect
# Create your views here.
def frontpage(request):
    return render(request, "home/frontpage.html")
def index(request):
    return render(request,"home/index.html")
def simpleinterest(request):
    return render(request,"home/simpleinterest.html")
def compoundinterest(request):
    return render(request,"home/compoundinterest.html")
def age(request):
    return render(request,"home/age.html")
def fatp(request):
    return render(request,"home/fatp.html")
def percentage(request):
    return render(request,"home/percentage.html")
def cgpa(request):
    return render(request,"home/cgpa.html")
def hour(request):
    return render(request,"home/hour.html")
def loan(request):
    return render(request,"home/loan.html")
def salary(request):
    return render(request,"home/salary.html")