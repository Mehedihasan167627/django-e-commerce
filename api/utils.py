import ast 
def string_to_list(text,model):
    queryset=ast.literal_eval(text)
    obj_list=[]
    for obj in queryset:
        pro=model.objects.get(id=obj["id"])
        if pro.discount_price:price=pro.discount_price
        else:price=pro.price
        obj_list.append({
            "id":obj["id"],"name":pro.title,"quantity":obj["quantity"],
            "image":pro.image.url,"price":price,
            "sub_total":price*obj["quantity"]
            })

    return obj_list 