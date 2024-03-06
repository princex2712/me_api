from rest_framework import serializers
from .models import TaskModel

class TastModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        # fields = ['title','content']
        fields = '__all__'