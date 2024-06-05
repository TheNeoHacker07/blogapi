from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Comment
from .serilizer import CommentSerializer
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny

from django.shortcuts import get_object_or_404

from .permissions import IsOwnerOrReadOnly
from post.models import Post
from .models import Comment,Like





class CommentViewSet(ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    def get_permissions(self):
        if self.action in ['list','retrieve']:
            self.permission_classes=[AllowAny]
        elif self.action in ['create']:
            self.permission_classes=[IsAuthenticated]
        elif self.action in ['update','partial_update','destroy']:
            self.permission_classes=[IsOwnerOrReadOnly]

        return [permission() for permission in self.permission_classes]



@api_view(['POST'])
def toggle_like(request,id):
    user=request.user
    if not user.is_authenticated:
        return Response(401)
    post=get_object_or_404(Post,id=id)
    if Like.objects.filter(user=user,post=post).exists():
        Like.objects.filter(user=user,post=post).delete()
    else:
        Like.objects.create(user=user,post=post)
    return Response(201)









# Create your views here.
