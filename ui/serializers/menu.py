from rest_framework import serializers
from ui.models import Category, Menu


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name',
                                          read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'
