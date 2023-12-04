from django.shortcuts import render,redirect
from myweb1.models import book_details
from myweb1.models import blogs
from .models import Insert
# Create your views h   


def Insertrecord(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('subject') and request.POST.get('notes'):
            saveRecord=Insert()
            saveRecord.name=request.POST['name']
            saveRecord.email=request.POST['email']
            saveRecord.subject=request.POST['subject']
            saveRecord.notes=request.POST['notes']
            saveRecord.save()
            return redirect('index')
def index(request):
    blog=blogs.objects.all()[0:3]
    b1=book_details.objects.all()[0:6]

    return render(request,'index.html',{'blogs':blog,'pro':b1})

def about(request):
    return render(request,'about.html')

def blogpost(request,pk):
    blog=blogs.objects.all().filter(name=pk).get()
    return render(request,'blog-post.html',{'blog':blog})

def blog(request):
    blog=blogs.objects.all()

    return render(request,'blog.html',{'blogs':blog})

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('subject') and request.POST.get('notes'):
            saveRecord=Insert()
            saveRecord.name=request.POST['name']
            saveRecord.email=request.POST['email']
            saveRecord.subject=request.POST['subject']
            saveRecord.notes=request.POST['notes']
            saveRecord.save()
            return redirect('contact')
    else:
        return render(request,'contact.html')

def productdetails(request,pk):
    posts=book_details.objects.all().filter(title=pk).get()

    return render(request,'productdetails.html',{'posts':posts})

def products(request):
    pro=book_details.objects.all()
    return render(request,'products.html',{'pro':pro})

def terms(request):
    return render(request,'terms.html')

def testimonials(request):
    return render(request,'testimonials.html')
