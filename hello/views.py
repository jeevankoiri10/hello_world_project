from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello, world. <a href="https://www.google.com">Google</a></h1>')
