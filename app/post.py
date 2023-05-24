from rest_framework import generics
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

class CreatePost(generics.CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    

class RetrivePost(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    

class UpdatePost(APIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    
    def put(self, request,pk):
        post=Post.objects.get(id=pk)
        ser=PostSerializer(post,data=request.data,partial=True)
        if ser.is_valid():
            ser.save(user=request.user)
            return Response({'success': True,'msg':'post updated successfully'})
        else:
            print(ser.errors)
            return Response({'success': False,'msg':'something went wrong'})

class DeletePost(generics.DestroyAPIView):
    queryset=User.objects.all()
    serializer_class=Userserializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def destroy(self, request,pk):
        try:
            post=Post.objects.get(id=pk)
            if post.user.id ==request.user.id:
                self.perform_destroy(post)
                return Response({'status':'post destroyed'})
            else:
                return Response({'status':'something went wrong'})
        except Exception as e:
            print(e)
            
class View(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        post_list=Post.objects.filter(user=request.user.id)
        print(post_list)
        ser=self.serializer_class(post_list,many=True)
        return Response({'status':'success','post':ser.data})
        # if ser.is_valid():
        # else:
        #     print(ser.errors)
        #     return Response({'status':'error',})
            
        