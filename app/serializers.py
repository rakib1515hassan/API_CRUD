from rest_framework import serializers
from app.models import Student, STUDENT_CLASS, GENDER

from rest_framework import serializers



class StudentSerializer(serializers.Serializer):
    name          = serializers.CharField(max_length=100, allow_blank=True, required=False)
    student_class = serializers.ChoiceField(choices=STUDENT_CLASS, default='vi')
    gender        = serializers.ChoiceField(choices=GENDER, default='Male')
    roll          = serializers.IntegerField(allow_null=True, required=False)
    picture       = serializers.ImageField(allow_null=True, required=False)
    email         = serializers.EmailField(max_length=50)
    waiver        = serializers.BooleanField(default=False)
    date_of_birth = serializers.DateField()
    created_at    = serializers.DateField(read_only=True)


    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name          = validated_data.get('name', instance.name)
        instance.student_class = validated_data.get('student_class', instance.student_class)
        instance.gender        = validated_data.get('gender', instance.gender)
        instance.roll          = validated_data.get('roll', instance.roll)
        instance.picture       = validated_data.get('picture', instance.picture)
        instance.email         = validated_data.get('email', instance.email)
        instance.waiver        = validated_data.get('waiver', instance.waiver)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()
        return instance




# Alter Native Way------------------------------------------------------------------
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'
         # fields = ''
