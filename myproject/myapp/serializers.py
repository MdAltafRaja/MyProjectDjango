from rest_framework import serializers
from myapp.models import book
from django.contrib.postgres.fields import ArrayField

class bookSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    isbn=serializers.CharField(max_length=14)
    authors=serializers.ListField(child=serializers.CharField())
    number_of_pages=serializers.IntegerField()
    publisher=serializers.CharField(max_length=100)
    country=serializers.CharField(max_length=25)
    release_date=serializers.DateField()

    def create(self, validated_data):
        return book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.authors = validated_data.get('authors', instance.authors)
        instance.number_of_pages = validated_data.get('number_of_pages', instance.number_of_pages)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.country = validated_data.get('country', instance.country)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.save()
        return instance