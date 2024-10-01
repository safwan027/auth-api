from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    #class Meta:
    #    model = User
    #    fields = ('username', 'email', 'password')
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField() 
    def validate(self,data):
        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError('Username already exists') 
         
        if data['email']:
            if User.objects.filter(email=data['email']).exists():  
                raise serializers.ValidationError('Email already exists')  
             
        return data


    def create(self,validated_data):
       user = User(username = validated_data['username'],email = validated_data['email'])  
       user.set_password(validated_data['password']) 
       user.save
       return user 


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField() 



        

   