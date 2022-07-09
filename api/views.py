from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import LoginSerializer
from api.serializers import OrderCreateSerializer, OrderListSerializer, ProductDetailSerializer, ProductListSerializer 
from rest_framework.permissions import IsAuthenticated
from .utils import string_to_list
from products.models import Product,Order
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import ast 

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class ProductListView(mixins.ListModelMixin,generics.GenericAPIView):
    queryset=Product.objects.filter(is_active=True).order_by("-id")
    serializer_class=ProductListSerializer

    def get(self,request,format=None):
        return self.list(request)

class ProductDetailView(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset=Product.objects.filter(is_active=True).order_by("-id")
    serializer_class=ProductDetailSerializer

    def get(self,request,pk,format=None):
        return self.retrieve(request)


class SubCategoryListView(generics.GenericAPIView,APIView):
    def get(self,request,pk):
        queryset=Product.objects.filter(sub_category__pk=pk,is_active=True).order_by("-id")
        serializer=ProductListSerializer(queryset,many=True)
        return Response(serializer.data)

class LoginView(APIView):
    def post(self,request,format=None):
        serializer=LoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get("email")
            password=serializer.data.get("password")
            user=authenticate(email=email,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({"token":token,"msg":"login success"})
            else:
                return Response({"errors":"email or password incorrect"})
        return Response(serializer.errors)


class OrderView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        queryset=Order.objects.filter(order_by=request.user)
        data_list=[]
        for i in queryset:
            data_list.append({
                "id":i.id,"order_id":i.unique_id,"total":i.total,"status":i.status,
                "product_list":string_to_list(i.name_and_quantity,Product),"paid":i.paid 
            })
        return Response(data_list,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer=OrderCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            pass
           

            return Response({"msg":"save"},status=status.HTTP_200_OK)



        
        