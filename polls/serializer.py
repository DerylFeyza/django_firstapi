from rest_framework import serializers
from .models import Question, Choice
from user.models import User

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields =  ['id', 'choice_text', 'votes', 'question_id']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = '__all__'

class CreateQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        
    def validate(self, attrs):
        user: User = self.context["request"].user
        attrs['author_id'] = user.id
        return super().validate(attrs)
