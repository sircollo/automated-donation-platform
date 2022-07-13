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
from rest_framework.response import Response
from .serializer import *


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
        fields = ('id', 'beneficiary_name', 'contact', 'location','country','donation_received','charity')
   
        
class AnonymousDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonymousDonation
        fields = '__all__'
        
        
class CharityPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        # fields = ['__all__']   
        fields = ['charity_name','charity_image','email','location','country','description','date_formed','target_amount','deadline','mission']
        # exclude = ('user')            
        
        
class CharityDetailsUpdateSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return CharitySerializer(instance).to_representation(instance)

    class Meta:
        model = Charity
        fields = ('email')
