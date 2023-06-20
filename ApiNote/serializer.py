from ApiNote.models import Teacher
from rest_framework import serializers

class TeacherSerializer(serializers.Serializer):
    name       = serializers.CharField(max_length=50)
    age        = serializers.IntegerField()
    salary     = serializers.IntegerField()
    experience = serializers.BooleanField()

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)
    
    def update(self, instance, validated_data): 
        instance.name       = validated_data.get('name',       instance.name)
        instance.age        = validated_data.get('age',        instance.age)
        instance.salary     = validated_data.get('salary',     instance.salary)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.save()
        return instance