from django.shortcuts import render
def homePage(request):
    return render(request,"index.html")
def loginpage(request):
    return render(request,"login.html")
def contactPage(request):
    return render(request,"contactus.html")
def aboutuspage(request):
    return render(request,"aboutus.html")
def registerationPage(request):
    return render(request,"register.html")


