from receipes.models import Receipe, Cuisine, Ingredient
from rest_framework.serializers import ModelSerializer, ReadOnlyField




class CuisineSerializer(ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['name', 'other_details']






class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity']






class ReceipeSerializer(ModelSerializer):
    submited_by = ReadOnlyField(source='submited_by.username')
    cuisine = CuisineSerializer(many=False)
    ingredients = IngredientSerializer(many=True)
    class Meta:
        model = Receipe
        fields = ['name', 'details', 'receipe_tags', 'category', 'cuisine', 
            'ingredients']

    def perform_create(self):
        pass

    def create(self, validated_data):
        """Create and return a new `Receipe` instance, given the validated data."""
        pass
    