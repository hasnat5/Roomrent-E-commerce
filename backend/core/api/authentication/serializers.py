from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    widgets = {
        'username':serializers.CharField(validators=[MinLengthValidator(3), MaxLengthValidator(50)])
    }