from django.test import TestCase
from collections import OrderedDict

from rest_framework.test import APIRequestFactory,force_authenticate
from rest_framework.utils .serializer_helpers import ReturnDict,ReturnList

from .views import PostViewSet
from .models import  Post

from django.contrib.auth import get_user_model

User=get_user_model()

class PostTest(TestCase):
    def setUp(self):
        self.factory=APIRequestFactory()
        user=User.objects.create_user(email='admin@gmail.com',password=1)
        posts=[
            Post(title='new post',author=user),
            Post(title='bought car',author=user),
            Post(title='porch',author=user)
        ]
        Post.objects.bulk_create(posts)

    def test_list(self):
        request=self.factory.get('/posts/')
        view=PostViewSet.as_view({'get':'list'})
        response=view(request)

        assert response.status_code==200
        assert type(response.data['results'])==ReturnList
        assert response.data['results'][0]['title']=='new post'

    # def test_retrieve(self):
    #     id=Post.objects.all()[0].id
    #     request=self.factory.get(f'/post/{id}/')
    #     view=PostViewSet.as_view({'get':'retrieve'})
    #     response=view(request,pk=id)

    #     assert response.status_code==200
    #     assert type(response.data)==ReturnDict
    #     assert response.data['title']=='new post'

    # def test_auth(self):
    #     data={
    #         'data':'new new new post'
    #     }
    #     request=self.factory.post('/post/',data,format='json')
    #     view=PostViewSet.as_view({'post':'create'})
    #     response=view(request)

    #     assert response.status_cide==401


    # def test_create(self):
    #     user=User.objects.all()[0]
    #     data={'title':'dsf'}
    #     request=self.factory.post('/post/',data,format='json')
    #     force_authenticate(request,user)
    #     view=PostViewSet.as_view({'post':'create'})
    #     response=view(request)

    #     assert response.status_code==201
    #     assert response.data['title']==data['title']
    #     assert response.data['author']==data['author']
    #     assert Post.objects.filter(author=user,title=data['title']).exists()

    # def test_update(self):
    #     user=User.objects.all()
    #     data={'title':'ferrari'}
    #     post=Post.objects.all()[2]
    #     request=self.factory.patch(f'/post/{post.id}/',data,format='json')
    #     force_authenticate(request,user)
    #     view=PostViewSet.as_view({'patch':'partial_update'})
    #     response=view(request,data,pk=post.id)

    # def test_delete(self):
    #     user=User.objects.all()[0]
    #     post=Post.objects.all()[2]
    #     request=self.factory.delete(f'/post/{post.id}/')
    #     force_authenticate(request,user)
    #     view=PostViewSet.as_view({'delete':'destroy'})
    #     response=view(request,pk=post.id)

    #     assert response.status_code==204
    #     assert not Post.objects.filter(id=post.id).exists()











    








# Create your tests here.