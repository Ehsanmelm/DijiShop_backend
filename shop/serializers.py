from rest_framework import serializers
from rest_framework.response import Response
from .models import SellerModel , StoreModel , StuffModel


class SellerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only = True)
        
    class Meta:
        model = SellerModel
        fields = ['id' , 'user_id' , 'phone']

    def create(self, validated_data):
        user_id = self.context['user_id']
        return SellerModel.objects.create(user_id = user_id , **validated_data)
    
class StoreSerializer(serializers.ModelSerializer):
    owner = SellerSerializer(read_only = True)

    class Meta:
        model = StoreModel
        fields = ['id' , 'name' , 'address' , 'owner'] 

    def create(self, validated_data):

        owner = self.context['owner']
        name = validated_data['name']

        if StoreModel.objects.filter(name = name).exists() :
            raise serializers.ValidationError("There is a such a store with same name")
        
        return StoreModel.objects.create(owner= owner, **validated_data)


class StuffSerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only = True)

    class Meta:
        model = StuffModel
        fields = ['id' , 'name' , 'description' , 'price' , 'capacity' , 'store']

