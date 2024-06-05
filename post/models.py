from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts',blank=True,verbose_name='автор')
    description=models.TextField(blank=True,verbose_name='описание')
    title=models.CharField(max_length=50,verbose_name='название')
    image=models.ImageField(upload_to='post_img',blank=True,verbose_name='фото')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='дата создание')
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    




    


# Create your models here.
