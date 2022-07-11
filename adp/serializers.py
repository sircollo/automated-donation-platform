from dataclasses import field
from readline import get_current_history_length
from urllib import response
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator 
from django.contrib.auth.password_validation import validate_password
from .models import *
from .models import AbstractUser


# get user token
class GetTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(GetTokenPairSerializer, cls).get_token(user)

        token['username'] = user.username
        print(user.is_donor)
        return token      
      
# Register Donor 
class RegisterDonorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email','password1', 'password2')

        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password1": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_donor=True
        )

        
        user.set_password(validated_data['password1'])
        user.is_donor = True
        user.save()

        return user 

# Register Charity  
class RegisterCharitySerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password1": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            is_charity=True
        )

        
        user.set_password(validated_data['password1'])
        user.is_charity = True
        user.save()

        return user
    

# Register Administrator
class RegisterAdminSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email','password1', 'password2')

        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password1": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_superuser=True,
            is_staff = True
        )

        
        user.set_password(validated_data['password1'])
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user 
    
class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = '__all__'
        
        
class BeneficiariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        # fields = '__all__'
        fields = ('id', 'name', 'contact', 'location','country','donation_received')
        
        
class AnonymousDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonymousDonation
        fields = '__all__'
        
        
class CharityPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        # fields = ['__all__']   
        fields = ['charity_name']
        # exclude = ('user')        
        
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id',instance.id)
        instance.charity_name = validated_data.get('charity_name', instance.charity_name)
        instance.email = validated_data.get('email', instance.email)
        instance.location = validated_data.get('location', instance.location)
        instance.country = validated_data.get('country', instance.country)
        instance.description = validated_data.get('description', instance.description)
        instance.charity_image = validated_data.get('charity_image', instance.charity_image)
        instance.date_formed = validated_data.get('date_formed', instance.date_formed)
        instance.date_joined = validated_data.get('date_joined', instance.date_joined)
        instance.target_amount = validated_data.get('target_amount', instance.target_amount)
        instance.current_amount = validated_data.get('current_amount', instance.current_amount)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.mission = validated_data.get('mission', instance.mission)    
        instance.save()
        # return super().update(instance, validated_data)
        return response
