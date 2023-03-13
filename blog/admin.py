from django.contrib import admin
from .models import Blog,Category
from django.utils.safestring import mark_safe

#admin modellerimizi bu dizine aktarcaz
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=("title","is_active","is_home","slug","selected_categories",)
    list_editable=("is_active","is_home",)# admin üzerinden bu şeklilde kolayca değisştirilebilir
    search_fields=("title",)
    readonly_fields=("slug",) # bunları bir liste oalarak kabul etmesi için sonuna , koyuyor olmamız gerek
    list_filter=("is_active","is_home","categories",)

    def selected_categories(self,obj):
        html ="<ul>"
        for category in obj.categories.all():
            html += "<li>" + category.name + "</li> " 

        html +="</ul>"
        return mark_safe(html)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)

