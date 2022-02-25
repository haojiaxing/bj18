from django.http import HttpResponse
from djiang.shortcuts import redirect

def index(request):
    return HttpResponse('index')
def index(request):
    return redirect('index')
