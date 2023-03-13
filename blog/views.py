from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Blog, Category


data={
     "blogs":[
     {
          "id":1,
          "title":"Uludağ üniversitesi",
          "image":"1.png",
          "description":"6 aylık web geliştirme + stay para",
          "is_active":True,
          "is_home":True,

     },
     {
          "id":2,
          "title":"Bursa teknik üniversitesi",
          "image":"2.png",
          "description":"6 aylık web geliştirme + stay para",
          "is_active":True,
          "is_home":True,
     },
     {
          "id":3,
          "title":"İstanbul üniversitesi",
          "image":"3.png",
          "description":"6 aylık web geliştirme + stay para",
          "is_active":True,
          "is_home":True,
     }
     ,{
          "id":4,
          "title":"Orta Doğu Teknik üniversitesi",
          "image":"4.png",
          "description":"6 aylık web geliştirme + stay para",
          "is_active":True,
          "is_home":False,
     },
     {
          "id":5,
          "title":"Samsun üniversitesi",
          "image":"5.png",
          "description":"6 aylık web geliştirme + stay para",
          "is_active":True,
          "is_home":True,
     }
     ]
}

# Create your views here.
def index(request):
    context={ #data["blogs"]#blogs data içinden tektek alıyoruz
         "blogs":Blog.objects.filter(is_active=True,is_home=True) ,
          "categories":Category.objects.all()

          
    }
    return render(request,"blog/index.html",context)

def blogs(request):
     context={
         "blogs":Blog.objects.filter(is_home=True), #data["blogs"]# blog dinamamik bir tasarımla aktarmak için
         "categories":Category.objects.all()
    }
     return render(request,"blog/blogs.html",context)

def blogs_details(request,slug):
    
     blog =Blog.objects.get(slug=slug)
     
     # sayfadaki id miz value değerlerimize den gelen yerden o sayfa bilgisini çekiyor
    #selectedBlog =[blog for blog in blogs if blog["id"] == id][0]     



     return render(request,"blog/details.html",{
          "blog":blog
     })

def blogs_by_categoty(request,slug):
      context={
          "blogs":Category.objects.get(slug=slug).blog_set.filter(is_home=True),
        # "blogs":Blog.objects.filter(is_home=True, category__slug=slug), #data["blogs"]# blog dinamamik bir tasarımla aktarmak için
         "categories":Category.objects.all(),
         "selected_category": slug
    }
      return render(request,"blog/blogs.html",context)










     #  blogs =data["blogs"]
     #  selectedBlog = None
     # for blog in blogs:
     #      if blog["id"] == id:
     #      selectedBlog=blog