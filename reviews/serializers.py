from rest_framework.serializers import ModelSerializer
from .models import Comment



class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = 'all'

    def to_representation(self, instance:Comment):
        return super().to_representation(instance)
        rep["author"] = instance.author.username
        del rep("post")
        return rep