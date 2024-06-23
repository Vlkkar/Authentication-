from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
# Create your views here.
def index(request):
    user=Users.objects.filter(name='Kikot')
    code=Users.objects.get(code)
    code.code = 4568
    code.save()
    return render(request, 'main/index.html', {'user': user, 'code':code})

def about(request):
    return HttpResponse("<h4>About me<h4>")