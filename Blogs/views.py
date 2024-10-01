from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def blogs_one(request):
    return render(request, "Blogs/index.html")

def blogs_post(request):
    return render(request, "Blogs/index.html")
    # Post = "Something i don't want"
    # return HttpResponse(Post)

def blogs_post_details(request):
    pass
    # Details ="no details right now"
    # return HttpResponse(Details)