from receipes.models import Receipe, Cuisine, Ingredient
from rest_framework.serializers import ModelSerializer, ReadOnlyField




class CuisineSerializer(ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['id', 'submited_by', 'name', 'other_details', 'added_on']






class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'submited_by', 'name', 'quantity', 'added_on']






class ReceipeSerializer(ModelSerializer):
    submited_by = ReadOnlyField(source='submited_by.username')
    cuisine = CuisineSerializer(many=False)
    ingredients = IngredientSerializer(many=True)
    class Meta:
        model = Receipe
        fields = ['id', 'submited_by', 'name', 'details', 'receipe_tags', 'category', 
            'is_premium', 'is_public', 'is_submited', 'added_on', 'cuisine', 'ingredients']

    def perform_create(self):
        pass

