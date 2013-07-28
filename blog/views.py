from django.shortcuts import render_to_response
from blog.models import Url,User
from blog.forms import UrlForm
from blog.long import Long_url

def index(req):
    if req.method=='POST':
        uf=UrlForm(req.POST)
        l_url=req.POST.get('long_url')
        l = Long_url(l_url)
        ym='127.0.0.1:8000/%s' % l
        return render_to_response('1.html',{'ym':ym,'uf':uf})
    else:
        uf=UrlForm()
        return render_to_response('1.html',{'uf':uf})

def turn(req,s_url):
    short='127.0.0.1:8000/%s' %s_url
    l_url=Url.objects.filter(short_url__exact=short)
    long=l_url[0].long_url
    if long[0:4]!='http':
        long='http://'+long
    return HttpResponseRedirect(long)
