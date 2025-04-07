from django.shortcuts import render


def index(request):
    data = {
        'caption':"airplanes"
    }
    return render(request,  'main/index.html', data)

def new(request):
    return render(request,  'main/new.html')

def user(request):
    return render(request,  'main/user.html')


