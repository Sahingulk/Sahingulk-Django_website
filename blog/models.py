from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

#abc.com/category/yazılım 
class Category(models.Model):
    name= models.CharField(max_length=160)
    slug= models.SlugField(null=False, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)

        super().save(*args, **kwargs) 
    def __str__(self):
        return self.name
    


# model için klas oluşturmalıyız.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    image =models.CharField(max_length=50)
    description = RichTextField()
    is_active = models.BooleanField(default=True)
    is_home = models.BooleanField(null=True)
    slug= models.SlugField(null=False, blank=True , unique=True, db_index=True ,editable=False)
   # category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category)

# unique her blok için özel tanımlanmış bir alan gibi çalısr    
    def __str__(self):
          return f"{self.title}"
    
# save i eziyoruz burda
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)

        super().save(*args, **kwargs) 


#18 tane migrations py manage.py migrate migrations yüklenir
#migrations islemei yapmamız gerekiyor
#yaptığımız bu işlemler veri tabanına eklenmeli





    

