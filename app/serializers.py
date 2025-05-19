from rest_framework import serializers

from app.models import Passport


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Passport
        fields=['id','first_name','last_name','phone_number','email','created_ad']
        read_only_fields=['created_ad']