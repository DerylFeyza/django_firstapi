from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Question, Choice
from .serializer import QuestionSerializer, ChoiceSerializer

class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveAPIView):
    queryset = Question.objects.prefetch_related('choices')
    serializer_class = QuestionSerializer

class QuestionCreate(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionUpdate(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDelete(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceList(generics.ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ChoiceDetail(generics.RetrieveAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ChoiceCreate(generics.CreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ChoiceUpdate(generics.UpdateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ChoiceDelete(generics.DestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer