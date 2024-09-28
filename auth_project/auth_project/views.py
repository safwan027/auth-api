from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from . serializer import UserSerializers
from  rest_framework import status



class User1(APIView):
    def get(self, request):
        data = User.objects.all()
        serializer = UserSerializers(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        data = request.data
        serializer = UserSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)



 









#@api_view(['POST'])
#def sample(request):
#    data = request.data  # This should be a list of dictionaries
#
#    # Ensure that the data is a list
#    if isinstance(data, list):
#        serializer = UserSerializers(data=data, many=True)  # Allow multiple objects
#
#        if serializer.is_valid():
#            serializer.save()  # Save all valid user data
#            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created data
#
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid
#    else:
#        return Response({"error": "Expected a list of user data."}, status=status.HTTP_400_BAD_REQUEST)



#@api_view (['GET','POST'])
#def signup(request):
#    serializer = SampleSerializer(data=request.data)  
#    if serializer.is_valid():
#        user = User.objects.create(username=request.data['username']) 
#        user.set_password(request.data['password']) 
#        user.save() 
#        token = Token.objects.create(user=user)
#        return Response({"token":token.key,"user":serializer.data})
#    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)