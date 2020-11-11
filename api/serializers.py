from rest_framework import serializers
from .models import Passport, Document, Qualification


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = '__all__'
        read_only_fields = ('investor',)


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('title', 'file')
        read_only_fields = ('investor',)


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Qualification
