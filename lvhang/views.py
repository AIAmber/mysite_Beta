from django.shortcuts import render
from django.shortcuts import HttpResponse, Http404
from lvhang import models
import datetime
import pymysql
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
    message_list = models.Message.objects.all()
    return render(request, "messageBoard.html", {"data" : message_list})

def ks(request):
    ks_demo = models.KSinfo.objects.all()
    return render(request, "ks.html", {"ks_info" : ks_demo})

def ks_info(request, offset):
    try:
        offset = str(offset)
    except:
        raise Http404()

    # ks_list = ['ahks', 'bjks', 'fjks', 'gsks', 'gxks', 'hbks', 'hebks', 'jsks', 'jxks', 'nmks', 'shks', 'tjks']
    # ks_detail = []
    # ans = 0


    # ks_select_list = {
    #     'ahks' : models.KSinfo_ahks.objects.all(),
    #     'bjks' : models.KSinfo_bjks.objects.all(),
    #     'fjks' : models.KSinfo_fjks.objects.all(),
    #     'gsks' : models.KSinfo_gsks.objects.all(),
    #     'gxks' : models.KSinfo_gxks.objects.all(),
    #     'hbks' : models.KSinfo_hbks.objects.all(),
    #     'hebks' : models.KSinfo_hebks.objects.all(),
    #     'jsks' : models.KSinfo_jsks.objects.all(),
    #     'jxks' : models.KSinfo_jxks.objects.all(),
    #     'nmks' : models.KSinfo_nmks.objects.all(),
    #     'shks' : models.KSinfo_shks.objects.all(),
    #     'tjks' : models.KSinfo_tjks.objects.all(),
    # }
    # ks_select = ks_select_list.get(offset, 'nothing')()

    ks_infor_list = {
        'ahks': {"ks_info_ah": models.KSinfo_ahks.objects.all()},
        'bjks': {"ks_info_bj": models.KSinfo_bjks.objects.all()},
        'fjks': {"ks_info_fj": models.KSinfo_fjks.objects.all()},
        'gsks': {"ks_info_gs": models.KSinfo_gsks.objects.all()},
        'gxks': {"ks_info_gx": models.KSinfo_gxks.objects.all()},
        'hbks': {"ks_info_hb": models.KSinfo_hbks.objects.all()},
        'hebks': {"ks_info_heb": models.KSinfo_hebks.objects.all()},
        'jsks': {"ks_info_js": models.KSinfo_jsks.objects.all()},
        'jxks': {"ks_info_jx": models.KSinfo_jxks.objects.all()},
        'nmks': {"ks_info_nm": models.KSinfo_nmks.objects.all()},
        'shks': {"ks_info_sh": models.KSinfo_shks.objects.all()},
        'tjks': {"ks_info_tj": models.KSinfo_tjks.objects.all()},
    }

    # ks_info_list = {
    #     'ahks': {"ks_info_ah": ks_select},
    #     "ks_info_bj": ks_select,
    #     "ks_info_gj": ks_select,
    #     "ks_info_gs": ks_select,
    #     "ks_info_gx": ks_select,
    #     "ks_info_hb": ks_select,
    #     "ks_info_heb": ks_select,
    #     "ks_info_js": ks_select,
    #     "ks_info_jx": ks_select,
    #     "ks_info_nm": ks_select,
    #     "ks_info_sh": ks_select,
    #     "ks_info_tj": ks_select,
    # }
    ks_info = ks_infor_list.get(offset, "nothing")

    # html = "<div class='title'><div class='info'><table border='1'><thead><th>期数</th><th>形态</th><th>和值</th><th>大小</th><th>单双</th></thead><tbody>{% for line in ks_info %}<tr><td>{{ line.date }}</td><td>{{ line.status }}</td><td>{{ line.hezhi }}</td><td>{{ line.BigS }}</td><td>{{ line.SigD }}</td></tr>{% endfor %}</tbody></table></div></div>"
    #
    html_name = offset+".html"
    return render(request, html_name, ks_info)