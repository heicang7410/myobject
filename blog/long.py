import hashlib
from blog.models import Url
def Long_url(l_url):     
    url=Url.objects.filter(long_url__exact = l_url)
    if url:
        sl_url=url[0].short_url
        return sl_url
    else:
        l_url=hashlib.sha1(l_url).hexdigest()
        s_url=l_url[0:6]
        url=Url.objects.create(long_url=l_url,short_url='127.0.0.1:8000'+s_url)
        return s_url

