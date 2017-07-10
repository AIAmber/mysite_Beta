from django.shortcuts import render
from django.shortcuts import HttpResponse
from lvhang import models
# Create your views here.

user_list = [
    {"user" : "jack", "pwd" : "abc"},
    {"user" : "tom", "pwd" : "ABC"},
]

def lvhang(request):
    # request.POST
    # request.GET
    return render(request, "lvhang.html",)
def login(request):
    if request.method == 'POST':
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # Put into the database...(write)
        # temp =  {"user" : username, "pwd" : password}
        # ser_list.append(temp)
        models.UserInfo.objects.create(user = username, pwd = password)

    # Pull from the database...(read)
    user_list = models.UserInfo.objects.all()
    return render(request, "login.html", {"data" : user_list})