from django.shortcuts import render, redirect
from .models import Post

# views for myblog 
def index(request):
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def post(request,pk):
    posts=Post.objects.get(id=pk)
    return render(request,'posts.html',{'posts':posts})

