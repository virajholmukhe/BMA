from AdminApp.models import Categories,Idol, ContactMe
from django.contrib import admin

# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    list_display=('id','name','description_min')

admin.site.register(Categories,CategoriesAdmin)

class IdolAdmin(admin.ModelAdmin):
    list_display=('id','model_no','model_name','price','height','category_id')
admin.site.register(Idol,IdolAdmin)

admin.site.register(ContactMe)