from django.shortcuts import redirect,render
from demo.models import Member

# Create your views here.
def com(request):
    mem=Member.objects.all()
    return render(request,"com.html",{'mem':mem})
def add(request):
    return render(request,"add.html",)
def addrec(request):
    x=request.POST['First']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member(firstname=x,lastname=y,country=z)
    mem.save()
    return redirect("/")