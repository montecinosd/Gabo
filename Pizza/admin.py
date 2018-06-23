from django.contrib import admin
from .models import Mass, Ingredients, User, Pizza, Order, Direction
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(Mass)
class MassAdmin(admin.ModelAdmin):
    list_display = ('name','description','image','code','price',)


@admin.register(Pizza)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name','description','image','code','price',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','birthday','email','direction','rut',)

    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
            % (obj.picture.url))
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','total_cost','order_direccion','pizza',)
