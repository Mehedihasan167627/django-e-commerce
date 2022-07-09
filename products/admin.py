from django.contrib import admin
from .models import* 

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}
    list_display=["name"]

@admin.register(SubCategory)
class SubCategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}
    list_display=["name","category"]




@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_display=["title","get_all_images","price","discount_price","sale_count","men_or_women","is_active"]
    list_editable=("is_active",)

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display=["unique_id",'customer_details',"product_list","total","paid","status"]
    list_editable=("paid","status")

admin.site.register(ProductImage)
admin.site.register(Address)
admin.site.register(Review)
