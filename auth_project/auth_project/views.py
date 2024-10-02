from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from . serializer import RegisterSerializer,LoginSerializer
from rest_framework import status



class RegisterAPI(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"User created successfully !"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
        
       
        
 

class LoginAPI(APIView):
    def post(self,request):
        data = request.data
        print("Raw data",data)
        serializer = LoginSerializer(data = data) 

        
        if serializer.is_valid():
            user = authenticate(username = serializer.data['username'],password = serializer.data['password']) 
            return Response({"message":"Its valid and authenticated","Result":user})
        return Response(serializer.errors)
        
         
    
        #if not user:
        #    return Response({"message":"Invalid"})
        #token, _  = Token.objects.get_or_create(user=user) 
        #return Response({"message":"Login successfull","token":str(token)})  
       
 



 









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