# import serializer from rest_framework and import model from models.py
from .models import Question, Choice
from rest_framework import serializers
 

# Create a model serializer
class QuestionSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Question
        fields = '__all__'


# Create a model serializer
class ChoiceSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Choice
        fields = ('question_id', 'choice_text', 'votes')