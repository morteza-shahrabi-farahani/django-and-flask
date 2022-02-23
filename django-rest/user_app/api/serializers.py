import email
from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'error': "passwords don't match"})
        
        if User.objects.filter(username=self.validated_data['username']).exists() or User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'username or email is used before'})
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()