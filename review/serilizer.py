from .models import Comment
from rest_framework.serializers import ModelSerializer



class CommentSerializer(ModelSerializer):
    class Meta:
        model=Comment
        exclude=['author']

    def validate(self, attrs):
        super().validate(attrs)
        request=self.context.get('request')
        attrs['author']=request.user
        return attrs