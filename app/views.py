from django.shortcuts import render

# Create your views here.
def num(request):
    d={'a':25}
    return render(request,'num.html',d)