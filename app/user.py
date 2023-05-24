from rest_framework import generics
from app.serializers import *
from app.models import User
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class CreateUser(generics.CreateAPIView):
    queryset=User.objects.all() 
    serializer_class=Userserializer
    
class UserLogin(APIView):
    
    def post(self,request):
        ser=UserLoginSerializer(data=request.data)
        if ser.is_valid():
            try:
                user=User.objects.get(email=ser.validated_data['email'])
                if user.password==ser.validated_data['password']:
                    token=Token.objects.get_or_create(user=user)
                    return Response({'success': True, 'token':token[0].key})
                else:
                    return Response({'success': False, 'msg': 'Invalid password'})
            except :
                return Response({'success': False, 'msg':'user does not exist'})
            

class RetriveUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class=Userserializer
    
class UpdateUser(APIView):
    queryset=User.objects.all()
    serializer_class=Userserializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def put(self, request):
        ser=self.serializer_class(request.user,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'success': True,',msg':'updated successfully'})
        else:
            print(ser.errors)
            return Response({'success': False,'msg':'some error occurred'})
                
                
class DeleteUser(generics.DestroyAPIView):
    queryset=User.objects.all()
    serializer_class=Userserializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def destroy(self, request,pk):
        try:
            user=User.objects.get(id=pk)
            if pk ==request.user.id:
                self.perform_destroy(request.user)
                return Response({'status':'user destroyed'})
            else:
                return Response({'status':'something went wrong'})
        except Exception as e:
            print(e)
        