from django.db.models.signals import post_save,pre_delete
from .models import Order,Product, ProductImage
from django.dispatch import receiver
import ast 


def order2saleCount(text):
    text=ast.literal_eval(text)
    data=[]
    for i in text:
        data.append({"id":i["id"],"quantity":i["quantity"]})
    return data
  
@receiver(post_save,sender=Order)
def count_sale_product(sender,instance,created,**kwargs):
    id_and_quantity=order2saleCount(instance.name_and_quantity)

    if instance.status=="Received":
        for i in id_and_quantity:
            query=Product.objects.get(id=i["id"])
            query.sale_count=int(query.sale_count)+int(i["quantity"])
            query.save()



@receiver(pre_delete,sender=Product)
def delete_product_image(sender,instance,*args,**kwargs):
    instance.image.delete()
    print("deleted")

@receiver(pre_delete,sender=ProductImage)
def delete_product_image(sender,instance,*args,**kwargs):
    instance.image.delete()
    print("deleted")
