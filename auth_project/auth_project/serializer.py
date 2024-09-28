from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']

    def create(self,validated_data):
        user = User(username = validated_data['username']) 
        user.set_password(validated_data['password']) 
        user.save
        return user 

