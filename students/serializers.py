from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    def validate_year(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Year must be between 1 and 5.")
        return value

    def validate(self, data):
        instance = self.instance

        if instance:
            if Student.objects.exclude(id=instance.id).filter(
                roll_number=data['roll_number']
            ).exists():
                raise serializers.ValidationError({
                    "roll_number": "Roll number already exists."
                })

            if Student.objects.exclude(id=instance.id).filter(
                email=data['email']
            ).exists():
                raise serializers.ValidationError({
                    "email": "Email already exists."
                })
        else:
            if Student.objects.filter(roll_number=data['roll_number']).exists():
                raise serializers.ValidationError({
                    "roll_number": "Roll number already exists."
                })

            if Student.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError({
                    "email": "Email already exists."
                })

        return data


    class Meta:
        model = Student
        fields = '__all__'
