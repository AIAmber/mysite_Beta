from django.shortcuts import render
from django.shortcuts import HttpResponse
from lvhang import models
# Create your views here.

message_list = [
    {"user" : "jack", "mail" : "xyzz@vip.qq.com", "message" : "Hello!"},
    {"user" : "tom", "mail" : "chomei@gmail.com", "message" : "Hi~"},
]

def lvhang(request):
    # request.POST
    # request.GET
    return render(request, "lvhang.html",)
def messageBoard(request):
    if request.method == 'POST':
        name = request.POST.get("name", None)
        email = request.POST.get("Email", None)
        content = request.POST.get("content", None)
        # Put into the database...(write)
        # temp =  {"user" : username, "pwd" : password}
        # ser_list.append(temp)
        models.Message.objects.create(user = name, mail = email, message = content)

    # Pull from the database...(read)
    user_list = models.Message.objects.all()
    return render(request, "messageBoard.html", {"data" : message_list})