from django.shortcuts import render
from django.shortcuts import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
import cmdb.models
import datetime
import pymysql
# Create your views here.

def tangshi(request):
    # request.POST
    # request.GET
    #return HttpResponse("Hello, world!")
    return render(request, 'tangshi.html')

def time(request):
    now = datetime.datetime.now()
    html = "<html> <body> It is now %s </body> </html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body> In %s hour(s), it will be %s.</body></html>" % (offset, dt)

    return HttpResponse(html)

def demo(request):
    now = datetime.datetime.now()
    #t = get_template('demo.html')
    #cont = Context({'current_date' : str(now)})
    #html = t.render(cont)
    #html2 = render_to_string('demo.html', cont)
    #return HttpResponse(html)

    cont = {'current_date' : now}
    return render(request, 'demo_ex_time.html', cont)

    #return render(request, "demo.html", {"current_date" : now})

def ptmpdb_list(request):
    ptmpdb = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = 'Bang103.',
        db = 'ptmpdb',
    ) # Please save in Django's configure.
    cursor = ptmpdb.cursor()
    cursor.execute('SELECT name FROM student ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    ptmpdb.close()
    return render(request, 'tangshi.html', {'names' : names})

def photo(request):
    return render(request, 'viewport.html')

