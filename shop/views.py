from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import SellerModel , StoreModel , StuffModel
from .serializers import SellerSerializer , StoreSerializer , StuffSerializer

# Create your views here.

class SellerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SellerSerializer

    def get_queryset(self):
        return SellerModel.objects.filter(user=self.request.user)
    
    def get_serializer_context(self):
        return {'user_id' : self.request.user.id}


class StoreViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = StoreSerializer

    def get_serializer_context(self):
        seller = SellerModel.objects.get(user =self.request.user )
        return { 'request': self.request.data , 'owner' : seller}
    
    def get_queryset(self):
        return StoreModel.objects.filter(owner = SellerModel.objects.get(user =self.request.user ))
    

    @action(detail=True , methods=['GET' , 'POST' , 'PUT'] , permission_classes=[IsAuthenticated] , serializer_class = StuffSerializer)
    def add_stuff(self,request , pk , stuff_id = None):
        # serializer = StuffSerializer
        store = StoreModel.objects.get(id=pk)
        stuffs  = StuffModel.objects.filter(store_id= pk)

        if request.method == 'GET':
            serializer = StuffSerializer(stuffs , many = True)
            return Response(serializer.data)
        
        elif request.method == 'POST':
            serializer = StuffSerializer( data= request.data  )
            serializer.is_valid(raise_exception= True)

            serializer.save(store =  store)
            return Response(serializer.data)
        
        # def put

class StuffViewset(ModelViewSet):
    http_method_names = ['get' , 'put' , 'delete']
    permission_classes = [IsAuthenticated]
    serializer_class = StuffSerializer

    def get_queryset(self):
        return  StuffModel.objects.filter(store__owner__user = self.request.user )
    
    # def get(self,request , pk=None):
    #     queryset = StuffModel.objects.filter(store__owner__user = self.request.user)

    #     serializer = StuffSerializer(queryset , many = True)
    #     return Response(serializer.data)
    
