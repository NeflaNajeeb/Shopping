from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
#def home(request):
 #   return HttpResponse("hello  im the home page")

#def about(request):
 #   return render(request,'about.html')

#def contact(request):
 #   return HttpResponse('Contact inmakes for python classes:9842657426')

#def details(request):
 #   return render(request,'detail.html')

#def thanks(request):
 #   return render(request,'thanks.html')

def home(request):
    return render(request,'home.html')
def arithmetic(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return render(request,'Arithmetic.html',{'addition':add,'subtraction':sub,'multiply':mul,'division':div})
   # return render(request,'Arithmetic.html',{'subtraction':sub})
#def substraction(request):
