from django.http import HttpResponse
from django.shortcuts import render

from.models import place
from.models import needs


# Create your views here.
def demo(request):
    obj=place.objects.all()
    objs=needs.objects.all()


    return render(request,"index.html",{'result':obj,'results':objs})

    # return HttpResponse("hello world")
    #  name="india"
    # return render(request,"oindexx.html",{"obj":name})
# def  addition(request):
#      x=int(request.GET['num1'])
#      y=int(request.GET['num2'])
#      res_add=x+y
#      res_sub=x-y
#      res_div=x/y
#      res_mul=x*y
# return render(request,"addition.html",{'result1':res_add,'result2':res_sub,'result3':res_div,'result4':res_mul})
# def contact(request):
#    return render(request,"contact.html")
