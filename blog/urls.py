from django.urls import path
from .import views 
# http://127.0.0.1:8000/        =>index sayfası
# http://127.0.0.1:8000/index   =>index sayfası
# http://127.0.0.1:8000/blogs   =>blogs sayfası
# http://127.0.0.1:8000/blogs/6   =>details sayfası
#kendimiz ekledik bu sayfayı


urlpatterns =[
    path("",views.index, name="home"),
    path("index",views.index),
    path("blogs",views.blogs,name= "blogs"),
    path("category/<slug:slug>",views.blogs_by_categoty,name= "blogs_by_categoty"),
    path("blogs/<slug:slug>",views.blogs_details, name="_details")
]