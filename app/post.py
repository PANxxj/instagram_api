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
      
      
class LikePost(APIView):
    serializer_class =PostSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self, request,pk):
        try:
            post=Post.objects.get(id=pk)
            new_post_like=PostLikes.objects.get_or_create(user=request.user,post=post)
            if not new_post_like[1]:
                new_post_like[0].delete()
                return Response({'status':True,'msg':'we have unlike the post'})
            else:
                return Response({'status':True,'msg':'we have like the post'})
        except Exception as e:
            print(e)
            return Response({'status':False,'msg':'something went wrong'})
        
            
class CommentPost(generics.CreateAPIView):
    queryset=Post.objects.all()
    serializer_class =CommentSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request,pk):
        try:
            post=Post.objects.get(id=pk)
            comments=PostComment.objects.filter(post=post)
            ser=self.serializer_class(comments,many=True)
            return Response({'status':True,'comments':ser.data})
            

        except Exception as e:
            print(e)
            return Response({'status':False,'msg':'something went wrong'})


    def post(self,request,pk):
        try:
            context={
                'request':request
            }
            post=Post.objects.get(id=pk)
            # request.data['post']=post
            ser=self.serializer_class(context=context,data=request.data)
            if ser.is_valid():
                ser.save(post=post)
                return Response({'status':True,'msg':'comment added'})
            else:
                return Response({'status':False,'msg':'got error to addng comment'})

        except Exception as e:
            print(e)
            return Response({'status':False,'msg':'something went wrong'})
